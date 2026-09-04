# Blend Task - Combinar Estilos de Copywriters

## Purpose
Criar copy híbrido combinando os pontos fortes de 2-4 copywriters diferentes, resultando em peças únicas que capturam o melhor de cada estilo.

## When to Use
- Quando nenhum copywriter individual atende 100% das necessidades
- Para criar um estilo único e diferenciado
- Quando você quer "o storytelling do Halbert com a elegância do Ogilvy"
- Para experimentar combinações criativas

## Inputs

```yaml
required:
  - copywriters: Lista de 2-4 copywriters para combinar
  - proportions: Peso de cada estilo (deve somar 100%)
  - copy_type: Tipo de peça a criar (sales_page, email, ad, headline, etc.)
  - briefing: Briefing completo do projeto

optional:
  - primary_copywriter: Quem define a estrutura base
  - blend_focus: O que combinar (voice, structure, techniques, all)
  - output_length: Curto, médio ou longo
```

## Copywriter Blend Matrix

### Combinações Recomendadas

| Combinação | Resultado | Ideal Para |
|------------|-----------|------------|
| Halbert + Ogilvy | Storytelling sofisticado | Produtos premium com história |
| Schwartz + Kennedy | Consciência + Urgência | Lançamentos em mercado saturado |
| Bencivenga + Sugarman | Bullets + Flow | Long-form com lista de benefícios |
| Kern + Hopkins | Autêntico + Testável | Digital com métricas |
| Benson + Halbert | VSL + Story | Vídeos emocionais |
| Ogilvy + Hopkins | Elegante + Científico | B2B e high-ticket |

### O Que Cada Copywriter Adiciona

| Copywriter | Contribuição Principal |
|------------|----------------------|
| Gary Halbert | Storytelling, emoção crua, headlines magnéticas |
| David Ogilvy | Elegância, pesquisa, credibilidade |
| Eugene Schwartz | Níveis de consciência, big ideas |
| Claude Hopkins | Testabilidade, especificidade, ofertas |
| Dan Kennedy | Urgência, deadlines, conversão direta |
| Gary Bencivenga | Bullets, fascinations, edição |
| Joe Sugarman | Flow, triggers, storytelling suave |
| Frank Kern | Autenticidade, casualidade, valor |
| Jon Benson | VSL structure, emoção, curiosidade |

## Workflow

### Step 1: Define Blend Parameters
```
Coletar:
1. Quais copywriters combinar? (2-4)
2. Qual a proporção de cada? (ex: 60% Halbert + 40% Ogilvy)
3. O que deve ser primário? (estrutura de quem?)
4. Qual tipo de copy criar?
5. Briefing do projeto
```

### Step 2: Extract DNA de Cada Copywriter
```
Para cada copywriter selecionado, extrair:
- Estrutura característica
- Tom de voz
- Técnicas assinatura
- Palavras/frases típicas
- Ritmo e cadência
```

### Step 3: Design Blend Strategy
```
Definir como combinar:

EXEMPLO: 60% Halbert + 40% Ogilvy

De Halbert (60%):
- Abertura com história pessoal
- Tom direto e provocador
- Urgência natural
- Garantia ousada

De Ogilvy (40%):
- Headlines com benefício específico
- Provas em números e fatos
- Tom final sofisticado
- Credibilidade institucional
```

### Step 4: Generate Blended Copy
```
Processo de criação:

1. ESTRUTURA: Use a estrutura do copywriter primário
2. ABERTURA: Aplique o estilo do copywriter com maior peso
3. CORPO: Intercale técnicas conforme proporções
4. FECHAMENTO: Combine CTAs dos dois estilos
5. REVISÃO: Garanta coesão e fluidez
```

### Step 5: DNA Analysis Output
```
Gerar análise mostrando:

## DNA Analysis

### Elementos de [Copywriter 1] (X%)
- [Técnica 1]: Aplicada em [seção]
- [Técnica 2]: Aplicada em [seção]
- Palavras características: "...", "..."

### Elementos de [Copywriter 2] (Y%)
- [Técnica 1]: Aplicada em [seção]
- [Técnica 2]: Aplicada em [seção]
- Palavras características: "...", "..."

### Pontos de Fusão
- [Seção] combina [técnica A] + [técnica B]
- [Transição] usa [estilo X] para [estilo Y]
```

### Step 6: Quality Validation
```
Checklist de blend:

- [ ] Proporções respeitadas?
- [ ] Técnicas-chave de cada copywriter presentes?
- [ ] Transições suaves entre estilos?
- [ ] Copy coeso (não parece "colagem")?
- [ ] DNA Analysis preciso?
- [ ] Resultado é distintivo (não é nenhum dos dois puros)?
```

## Output

```yaml
format: markdown
sections:
  - blend_strategy: Explicação de como foi combinado
  - dna_analysis: Breakdown de elementos de cada copywriter
  - blended_copy: A peça final
  - copywriter_markers: Onde cada estilo aparece
  - fusion_points: Onde os estilos se encontram
  - alternative_blend: Uma variação com proporções diferentes
```

## Examples

### Example 1: Halbert (70%) + Ogilvy (30%)

**Briefing:** Curso de copywriting, $997, para empreendedores

**Blend Strategy:**
- Halbert: História do criador, tom direto, urgência
- Ogilvy: Headlines factuais, prova em números, credibilidade

**Result Preview:**
```
HEADLINE (Ogilvy): "Como Escrever Copy Que Vende:
147 Alunos Já Faturaram R$2.4M Com Este Método"

LEAD (Halbert): "Caro amigo, deixa eu te contar uma história
que vai mudar sua relação com dinheiro para sempre..."

PROVA (Ogilvy): "Nos últimos 18 meses, 147 alunos aplicaram
este método e geraram, em média, R$16.326 cada um..."

CTA (Halbert): "Olha, eu sei que $997 parece muito.
Mas deixa eu te fazer uma pergunta..."
```

### Example 2: Benson (50%) + Bencivenga (50%)

**Briefing:** VSL para suplemento de energia

**Blend Strategy:**
- Benson: Estrutura VSL, emoção, curiosity loops
- Bencivenga: Bullets hipnóticos, fascinations

**Result Preview:**
```
HOOK (Benson): "O que eu vou te mostrar nos próximos
12 minutos pode parecer impossível..."

BULLETS (Bencivenga):
• O "mineral esquecido" que dobra energia em 72 horas
  (e custa menos que um café)
• Por que atletas olímpicos estão abandonando energéticos
  por esta cápsula de 3 gramas
• A descoberta acidental de um bioquímico insone que agora
  dorme 8h e acorda com mais energia que aos 20 anos

CLOSE (Benson): "Você sentiu isso? Essa curiosidade?
É exatamente assim que você vai se sentir toda manhã..."
```

## Blend Ratio Guidelines

### Para Resultados Equilibrados
- **50/50:** Dois estilos igualmente presentes
- **60/40:** Um dominante com toques do outro
- **70/30:** Claramente um estilo com influências sutis

### Para Três Copywriters
- **50/30/20:** Um primário, um secundário, um terciário
- **40/30/30:** Equilíbrio com leve dominância

### Para Quatro Copywriters
- **40/25/20/15:** Hierarquia clara
- **30/30/20/20:** Dois dominantes, dois suporte

## Anti-Patterns (Evitar)

❌ **Colagem óbvia:** Copy parece "cortado e colado"
❌ **Perda de identidade:** Nenhum estilo é reconhecível
❌ **Inconsistência de tom:** Muda abruptamente entre estilos
❌ **Proporções ignoradas:** Promete 60/40 mas entrega 90/10
❌ **Sem DNA Analysis:** Não documenta o que veio de onde

## Notes

- Blend funciona melhor com copywriters de eras próximas
- Combinações muito distantes (Hopkins + Kern) precisam cuidado extra
- O copywriter com maior peso define a "voz narrativa"
- Transições são os pontos mais críticos do blend

---

*Task Version: 1.0*
*CopywriterOS - Elite Copywriting Squad*
