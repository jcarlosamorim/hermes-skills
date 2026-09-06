// POST /api/portal → { url }  Portal do cliente do Stripe: trocar cartão, ver faturas, cancelar o Passe.
import { stripe, json, currentUser, customerFor, SITE } from "./_lib.js";

export async function POST(request) {
  const user = await currentUser(request);
  if (!user) return json({ error: "faça login" }, 401);
  const customer = await customerFor(user);
  const session = await stripe.billingPortal.sessions.create({ customer, return_url: `${SITE}/?conta=1`, locale: "pt-BR" });
  return json({ url: session.url });
}
