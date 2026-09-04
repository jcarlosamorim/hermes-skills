# Unit economics antes do primeiro real

Origem: método do `outputs/meta-ads` (plano a seco, sem API). Tudo aqui é aritmética; a decisão de gastar é humana.

## As oito perguntas, na ordem

1. **Ticket**: quanto entra por venda, líquido da taxa da plataforma.
2. **AOV no dia zero**: ticket + bump + upsell que fecham na mesma compra.
3. **LTV em 12 meses**: o que um cliente vale no ano, se houver recorrência ou recompra. Sem dado, use o AOV e diga que é conservador.
4. **Margem disponível para aquisição**: quanto do AOV você aceita gastar para trazer um cliente. Regra de bolso: até 30% do LTV-12m para produto com recompra; até 50% do AOV para venda única.
5. **CAC-alvo**: a margem do item 4. **CAC-teto**: o ponto em que a venda dá prejuízo (AOV menos custo de entrega menos taxa).
6. **Taxa lead → venda**: se o funil tem lead antes da venda, o histórico dela define o CPL. `CPL-alvo = CAC-alvo × taxa`. Sem histórico, assuma 2% e declare a hipótese.
7. **Orçamento de validação**: gaste ao menos 1× o CAC-teto por conjunto antes de julgar; abaixo disso não há dado, há ruído.
8. **Gatilho de parada**: o número em que a campanha para sem discussão: gasto ≥ 1× CAC-teto sem venda, ou CAC medido acima do teto em janela de 7 dias fechados.

## Saída

Uma tabela em linguagem de negócio ("cada real precisa voltar R$X para empatar") seguida da tabela técnica (CAC-alvo, CAC-teto, CPL-alvo, CPL-teto, orçamento por fase, gatilho de parada). Toda linha técnica vem com a tradução do lado.

## O que este plano não faz
Não prevê resultado. Ele define **quando parar** e **quanto arriscar** antes de saber. Quem promete CAC antes da primeira campanha está chutando.
