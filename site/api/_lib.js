// Compartilhado pelas funções da API (arquivos com "_" não viram rota na Vercel).
// Segredos só por variável de ambiente; nada aqui vai para o navegador.
import Stripe from "stripe";
import { createClient } from "@supabase/supabase-js";

const need = (k) => { const v = process.env[k]; if (!v) throw new Error(`env ${k} ausente`); return v; };

export const SITE = process.env.SITE_URL || "https://agentsflix.ai";

export const stripe = new Stripe(need("STRIPE_SECRET_KEY"), { appInfo: { name: "agentsflix", url: SITE } });

// cliente administrativo: ignora RLS. Só aqui, no servidor.
export const admin = createClient(need("SUPABASE_URL"), need("SUPABASE_SERVICE_ROLE_KEY"), { auth: { persistSession: false, autoRefreshToken: false } });

export const json = (data, status = 200, headers = {}) =>
  new Response(JSON.stringify(data), { status, headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store", ...headers } });

// quem está logado? O navegador manda o access token do Supabase em Authorization: Bearer <jwt>
export async function currentUser(request) {
  const auth = request.headers.get("authorization") || "";
  const token = auth.startsWith("Bearer ") ? auth.slice(7) : null;
  if (!token) return null;
  const { data, error } = await admin.auth.getUser(token);
  if (error || !data?.user) return null;
  return data.user;
}

// cliente Stripe do usuário: cria na primeira compra e guarda em stripe_customers
export async function customerFor(user) {
  const { data } = await admin.from("stripe_customers").select("stripe_customer_id").eq("user_id", user.id).maybeSingle();
  if (data?.stripe_customer_id) return data.stripe_customer_id;
  const c = await stripe.customers.create({ email: user.email, metadata: { supabase_user_id: user.id } });
  await admin.from("stripe_customers").upsert({ user_id: user.id, stripe_customer_id: c.id });
  return c.id;
}

export async function readJson(request) {
  try { return await request.json(); } catch { return {}; }
}
