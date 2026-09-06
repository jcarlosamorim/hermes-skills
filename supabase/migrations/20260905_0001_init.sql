-- AgentsFlix · esquema inicial (2026-09-05)
-- Modelo: a skill continua gratuita no GitHub; o que se vende é o conteúdo exclusivo (vídeos e extras)
-- por item (locadora) ou pelo Passe (assinatura). Identificadores em inglês; RLS em toda tabela pública.
-- Aplicado pela Management API (POST /v1/projects/{ref}/database/query). Idempotente.

create extension if not exists pgcrypto;

-- ---------- perfis (1:1 com auth.users) ----------
create table if not exists public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  email text,
  display_name text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create or replace function public.handle_new_user() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  insert into public.profiles (id, email, display_name)
  values (new.id, new.email, coalesce(new.raw_user_meta_data->>'name', split_part(new.email, '@', 1)))
  on conflict (id) do update set email = excluded.email, updated_at = now();
  return new;
end $$;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created after insert on auth.users
  for each row execute function public.handle_new_user();

-- ---------- catálogo comercial ----------
-- kind: 'skill' = conteúdo exclusivo de uma skill (id = slug da skill); 'pass' = assinatura que libera tudo
create table if not exists public.products (
  id text primary key,
  kind text not null check (kind in ('skill', 'pass')),
  title text not null,
  description text,
  active boolean not null default true,
  stripe_product_id text unique,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

-- id = stripe price id; interval nulo = compra avulsa
create table if not exists public.prices (
  id text primary key,
  product_id text not null references public.products(id) on delete cascade,
  currency text not null default 'brl',
  unit_amount integer not null check (unit_amount >= 0),
  "interval" text check ("interval" in ('month', 'year')),
  active boolean not null default true,
  created_at timestamptz not null default now()
);
create index if not exists prices_product_idx on public.prices(product_id);

-- ---------- Stripe: cliente e idempotência de webhooks ----------
create table if not exists public.stripe_customers (
  user_id uuid primary key references public.profiles(id) on delete cascade,
  stripe_customer_id text not null unique,
  created_at timestamptz not null default now()
);

create table if not exists public.webhook_events (
  id text primary key,               -- evt_… do Stripe
  type text not null,
  received_at timestamptz not null default now(),
  processed_at timestamptz,
  error text,
  payload jsonb not null
);

-- ---------- compras e assinaturas ----------
create table if not exists public.purchases (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references public.profiles(id) on delete cascade,
  product_id text not null references public.products(id),
  price_id text references public.prices(id),
  stripe_checkout_session_id text unique,
  stripe_payment_intent_id text unique,
  amount integer not null,
  currency text not null default 'brl',
  status text not null check (status in ('paid', 'refunded', 'disputed')),
  created_at timestamptz not null default now(),
  refunded_at timestamptz
);
create index if not exists purchases_user_idx on public.purchases(user_id);

create table if not exists public.subscriptions (
  id text primary key,               -- sub_… do Stripe
  user_id uuid not null references public.profiles(id) on delete cascade,
  product_id text not null references public.products(id),
  price_id text references public.prices(id),
  status text not null,              -- active, trialing, past_due, canceled, unpaid, incomplete…
  current_period_end timestamptz,
  cancel_at_period_end boolean not null default false,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create index if not exists subscriptions_user_idx on public.subscriptions(user_id);

-- ---------- direitos: a fonte da verdade do cadeado ----------
-- source: 'purchase' (avulsa), 'subscription' (Passe), 'grant' (cortesia/manual)
create table if not exists public.entitlements (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references public.profiles(id) on delete cascade,
  product_id text not null references public.products(id),
  source text not null check (source in ('purchase', 'subscription', 'grant')),
  source_id text,
  granted_at timestamptz not null default now(),
  expires_at timestamptz,
  revoked_at timestamptz,
  note text,
  unique (user_id, product_id, source, source_id)
);
create index if not exists entitlements_user_idx on public.entitlements(user_id) where revoked_at is null;

-- tem acesso ao conteúdo da skill? direito direto vigente OU Passe vigente
create or replace function public.has_access(p_product_id text) returns boolean
language sql stable security definer set search_path = public as $$
  select exists (
    select 1 from public.entitlements e
    where e.user_id = auth.uid()
      and e.revoked_at is null
      and (e.expires_at is null or e.expires_at > now())
      and (e.product_id = p_product_id
           or e.product_id in (select id from public.products where kind = 'pass'))
  );
$$;

-- lista de produtos liberados para o usuário logado (para a página pintar os cadeados de uma vez)
create or replace function public.my_access() returns table (product_id text, via text, expires_at timestamptz)
language sql stable security definer set search_path = public as $$
  select e.product_id, e.source, e.expires_at
  from public.entitlements e
  where e.user_id = auth.uid() and e.revoked_at is null and (e.expires_at is null or e.expires_at > now());
$$;

-- ---------- conteúdo exclusivo ----------
create table if not exists public.videos (
  id uuid primary key default gen_random_uuid(),
  product_id text not null references public.products(id) on delete cascade,
  title text not null,
  position integer not null default 1,
  bunny_video_id text not null unique,
  duration_seconds integer,
  status text not null default 'processing' check (status in ('processing', 'ready', 'hidden')),
  created_at timestamptz not null default now()
);
create index if not exists videos_product_idx on public.videos(product_id, position);

create table if not exists public.extras (
  id uuid primary key default gen_random_uuid(),
  product_id text not null references public.products(id) on delete cascade,
  title text not null,
  kind text not null check (kind in ('pdf', 'zip', 'link', 'text')),
  storage_path text,                 -- objeto no bucket privado 'extras'
  url text,                          -- para kind = 'link'
  body text,                         -- para kind = 'text'
  position integer not null default 1,
  created_at timestamptz not null default now()
);

-- ---------- métricas de uso da vitrine ----------
create table if not exists public.events (
  id bigint generated always as identity primary key,
  user_id uuid references public.profiles(id) on delete set null,
  anon_id text,                      -- id anônimo do navegador (localStorage)
  kind text not null check (kind in ('card_open', 'copy_command', 'download_zip', 'open_prompt', 'watch_start', 'watch_end', 'checkout_start')),
  product_id text,                   -- slug (pode não estar em products: skill gratuita)
  agent text,                        -- alvo de instalação escolhido
  meta jsonb,
  created_at timestamptz not null default now()
);
create index if not exists events_created_idx on public.events(created_at);
create index if not exists events_product_idx on public.events(product_id, kind);

-- ---------- RLS ----------
alter table public.profiles enable row level security;
alter table public.products enable row level security;
alter table public.prices enable row level security;
alter table public.stripe_customers enable row level security;
alter table public.webhook_events enable row level security;
alter table public.purchases enable row level security;
alter table public.subscriptions enable row level security;
alter table public.entitlements enable row level security;
alter table public.videos enable row level security;
alter table public.extras enable row level security;
alter table public.events enable row level security;

drop policy if exists "profiles: own read" on public.profiles;
create policy "profiles: own read" on public.profiles for select to authenticated using (id = auth.uid());
drop policy if exists "profiles: own update" on public.profiles;
create policy "profiles: own update" on public.profiles for update to authenticated using (id = auth.uid()) with check (id = auth.uid());

drop policy if exists "products: public read" on public.products;
create policy "products: public read" on public.products for select to anon, authenticated using (active);
drop policy if exists "prices: public read" on public.prices;
create policy "prices: public read" on public.prices for select to anon, authenticated using (active);

drop policy if exists "purchases: own read" on public.purchases;
create policy "purchases: own read" on public.purchases for select to authenticated using (user_id = auth.uid());
drop policy if exists "subscriptions: own read" on public.subscriptions;
create policy "subscriptions: own read" on public.subscriptions for select to authenticated using (user_id = auth.uid());
drop policy if exists "entitlements: own read" on public.entitlements;
create policy "entitlements: own read" on public.entitlements for select to authenticated using (user_id = auth.uid());

-- metadados dos vídeos são públicos (título, duração) para a vitrine; a URL assinada só sai da API para quem tem direito
drop policy if exists "videos: public metadata" on public.videos;
create policy "videos: public metadata" on public.videos for select to anon, authenticated using (status = 'ready');
drop policy if exists "extras: entitled read" on public.extras;
create policy "extras: entitled read" on public.extras for select to authenticated using (public.has_access(product_id));

-- eventos: qualquer visitante registra; ninguém lê pelo cliente (leitura só pelo painel, com service_role)
drop policy if exists "events: insert by anyone" on public.events;
create policy "events: insert by anyone" on public.events for insert to anon, authenticated
  with check (user_id is null or user_id = auth.uid());

-- stripe_customers e webhook_events: sem política = só service_role (as funções na Vercel)

-- ---------- storage privado para extras ----------
insert into storage.buckets (id, name, public, file_size_limit)
values ('extras', 'extras', false, 104857600)
on conflict (id) do nothing;

drop policy if exists "extras bucket: entitled read" on storage.objects;
create policy "extras bucket: entitled read" on storage.objects for select to authenticated
  using (bucket_id = 'extras' and public.has_access(split_part(name, '/', 1)));

-- ---------- produto Passe ----------
insert into public.products (id, kind, title, description)
values ('pass', 'pass', 'Passe AgentsFlix', 'Acesso a todo o conteúdo exclusivo enquanto a assinatura estiver ativa.')
on conflict (id) do nothing;
