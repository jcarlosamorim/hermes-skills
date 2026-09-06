// GET /api/video?id=<uuid> → { embed, expires }  URL assinada do Bunny Stream, só para quem tem direito.
// Token Authentication do Bunny: sha256(token_auth_key + video_id + expiration), validade curta.
import { createHash } from "node:crypto";
import { createClient } from "@supabase/supabase-js";
import { admin, json, currentUser } from "./_lib.js";

const TTL_S = 15 * 60;

export async function GET(request) {
  const url = new URL(request.url);
  const id = url.searchParams.get("id");
  if (!id) return json({ error: "id obrigatório" }, 400);
  const user = await currentUser(request);
  if (!user) return json({ error: "faça login" }, 401);

  const { data: video } = await admin.from("videos").select("id, product_id, bunny_video_id, title, status").eq("id", id).maybeSingle();
  if (!video || video.status !== "ready") return json({ error: "vídeo indisponível" }, 404);

  // o direito é avaliado como o usuário (RLS + has_access), não como admin
  const token = (request.headers.get("authorization") || "").slice(7);
  const asUser = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_ANON_KEY, { global: { headers: { Authorization: `Bearer ${token}` } }, auth: { persistSession: false } });
  const { data: ok } = await asUser.rpc("has_access", { p_product_id: video.product_id });
  if (ok !== true) return json({ error: "sem acesso a este conteúdo", product_id: video.product_id }, 403);

  const lib = process.env.BUNNY_STREAM_LIBRARY_ID, key = process.env.BUNNY_TOKEN_AUTH_KEY;
  if (!lib || !key) return json({ error: "vídeo ainda não configurado" }, 503);
  const expires = Math.floor(Date.now() / 1000) + TTL_S;
  const sig = createHash("sha256").update(key + video.bunny_video_id + expires).digest("hex");
  const embed = `https://iframe.mediadelivery.net/embed/${lib}/${video.bunny_video_id}?token=${sig}&expires=${expires}&autoplay=true&preload=true`;
  await admin.from("events").insert({ user_id: user.id, kind: "watch_start", product_id: video.product_id, meta: { video: video.id } });
  return json({ embed, expires, title: video.title });
}
