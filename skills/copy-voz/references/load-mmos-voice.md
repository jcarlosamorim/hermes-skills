# Load MMOS Voice Clone Task

Task para carregar artefatos de clone cognitivo do sistema MMOS e integrar com produção de copy.

## Metadata

```yaml
task:
  name: Load MMOS Voice Clone
  id: load-mmos-voice
  version: "1.0"
  category: voice_integration
  estimated_output: "Voice context loaded"
  dependencies:
    - outputs/minds/{slug}/
    - squads/copy/data/expert-clone-mapping.yaml
```

---

## PHASE 0: CLONE DETECTION

### 0.1 Auto-Detect Expert from Briefing

```yaml
auto_detection:
  triggers:
    - "Nome do expert mencionado no briefing"
    - "Curso/produto associado ao expert"
    - "Domínio específico (ex: cohort-based courses → José Amorim)"

  detection_flow:
    1. Parse briefing for expert name
    2. Check expert-clone-mapping.yaml
    3. If found → auto-load clone
    4. If not found → ask user which clone to use
```

### 0.2 Manual Clone Selection

Se expert não for detectado automaticamente:

```
Perguntar ao usuário:
- "Qual expert deve ser o autor desta copy?"
- "Temos clone disponível? [listar disponíveis]"
- "Deseja usar tom de voz genérico?"
```

---

## PHASE 1: LOAD VOICE ARTIFACTS

### 1.1 Required Artifacts (MUST load)

```yaml
required_artifacts:
  voice_guide:
    path: "outputs/minds/{slug}/artifacts/voice_guide.md"
    purpose: "Quick reference de voz e estilo"
    contains:
      - "Signature phrases"
      - "Espiral expansiva structure"
      - "Rhetorical devices"
      - "Anti-patterns (what NOT to do)"
      - "Voice checklist"

  writing_style:
    path: "outputs/minds/{slug}/artifacts/writing_style.yaml"
    purpose: "Padrões linguísticos detalhados"
    contains:
      - "Sentence structure patterns"
      - "Vocabulary preferences"
      - "Punctuation style"
      - "Neurological patterns in speech"

  communication_templates:
    path: "outputs/minds/{slug}/artifacts/communication_templates.md"
    purpose: "Templates de comunicação por contexto"
    contains:
      - "4 personas situacionais"
      - "Adaptation by audience"
      - "Implementation checklist"

  frameworks_synthesized:
    path: "outputs/minds/{slug}/artifacts/frameworks_synthesized.md"
    purpose: "Frameworks proprietários do expert"
    contains:
      - "Metodologias próprias"
      - "Decision frameworks"
      - "Teaching models"
```

### 1.2 Story Artifacts (SHOULD load)

```yaml
story_artifacts:
  mental_archeology:
    path: "outputs/minds/{slug}/sources/mental_archeology.yaml"
    purpose: "Timeline de eventos, decisões críticas, frases-chave"
    contains:
      - "Life timeline"
      - "Critical decisions"
      - "Linguistic artifacts (catchphrases)"
      - "Patterns (macro, meso, micro)"

  interview_sources:
    path: "outputs/minds/{slug}/sources/interviews/"
    purpose: "Entrevistas com histórias pessoais"
    contains:
      - "Origin stories"
      - "Turning points"
      - "Personal anecdotes"

  general_profile:
    path: "outputs/minds/{slug}/sources/geral.md"
    purpose: "Perfil geral com contexto biográfico"
    contains:
      - "Background"
      - "Values"
      - "Communication style overview"
```

### 1.3 Optional Artifacts

```yaml
optional_artifacts:
  system_prompt:
    path: "outputs/minds/{slug}/system_prompts/system-prompt-generalista.md"
    purpose: "System prompt completo (use se precisar de contexto deep)"
    when_to_load: "Copy muito complexa ou longa"

  language_forensics:
    path: "outputs/minds/{slug}/sources/language_forensics.md"
    purpose: "Análise forense de linguagem"
    when_to_load: "Precisar de voice super-fiel"
```

---

## PHASE 2: EXTRACT USABLE ELEMENTS

### 2.1 Voice DNA Extraction

Após carregar artefatos, extrair:

```yaml
voice_dna:
  signature_phrases:
    - "Frases de abertura (ex: 'Olha só...', 'Vem comigo...')"
    - "Frases de transição (ex: 'E aí que tá...')"
    - "Frases de fechamento (ex: 'Simples assim.', 'Ponto.')"

  rhetorical_patterns:
    - "Metáforas visuais-espaciais"
    - "Perguntas retóricas antes de responder"
    - "Antíteses ('Não é X, é Y')"
    - "Parênteses como pensamento paralelo (TDAH)"

  emotional_markers:
    - "Intensificadores ('MUDA tudo', 'É TRANSFORMADOR')"
    - "Validadores empáticos ('Te entendo...', 'Faz todo sentido...')"
    - "Provocadores intelectuais ('Mas e se...', 'Agora pensa comigo...')"

  structural_patterns:
    - "Espiral Expansiva (5 camadas)"
    - "Alternância curtas/longas"
    - "Confessionalidade estratégica (vulnerabilidade → aprendizado → universalização)"
```

### 2.2 Story Bank Extraction

```yaml
story_bank:
  origin_stories:
    - "Esquistossomose aos 7 anos (traduzir complexidade)"
    - "Criado pelos avós (superação, origem humilde)"
    - "7 cursos abandonados (padrão → força)"

  transformation_stories:
    - "Saída Rede Amazônica após 10 anos"
    - "Abandono League of Legends ao descobrir IA"
    - "De técnico mecatrônica para jornalista"

  vulnerability_stories:
    - "Reprovação 6ª série por falar muito"
    - "TDAH como 'defeito' → 'superpoder'"
    - "Dificuldade com rotinas"

  triumph_stories:
    - "10+ anos de TV ao vivo"
    - "Certificações Harvard/IBM/Anthropic"
    - "Criação de frameworks próprios (OMFA, Linchpin)"
```

---

## PHASE 3: APPLY TO COPY

### 3.1 Copy Rewrite Process

```yaml
rewrite_process:
  step_1_structure:
    action: "Aplicar Espiral Expansiva"
    layers:
      - "Gancho emocional"
      - "Metáfora visual"
      - "Fundamento conceitual"
      - "Aplicação prática"
      - "Expansão filosófica"

  step_2_voice:
    action: "Aplicar padrões linguísticos"
    elements:
      - "Signature phrases"
      - "Rhetorical patterns"
      - "Emotional markers"
      - "Sentence rhythm (alternância)"

  step_3_stories:
    action: "Inserir histórias pessoais quando apropriado"
    criteria:
      - "Relevância para o tema"
      - "Conexão emocional"
      - "Lição implícita"

  step_4_persona:
    action: "Selecionar persona situacional"
    options:
      - "Professor Socrático (aulas, didática)"
      - "Visionário Inquieto (peers, co-criação)"
      - "Conselheiro Empático (1-on-1, validação)"
      - "Estrategista Direto (negócios, ROI)"
```

### 3.2 Quality Checklist

```yaml
voice_quality_checklist:
  structure:
    - [ ] "Usou metáfora visual-espacial?"
    - [ ] "Alternância curtas/longas?"
    - [ ] "Parênteses (pensamento paralelo)?"

  tone:
    - [ ] "2ª pessoa ('você')?"
    - [ ] "Entusiasmo (não neutro)?"
    - [ ] "Urgência existencial calibrada?"

  rhetoric:
    - [ ] "Perguntou antes de responder (quando apropriado)?"
    - [ ] "Usou antítese 'Não é X, é Y' (se aplicável)?"

  authenticity:
    - [ ] "Confessaria vulnerabilidade se relevante?"
    - [ ] "Evitou jargão desnecessário?"
    - [ ] "Evitou tom corporativo/distante?"

  stories:
    - [ ] "História pessoal relevante incluída?"
    - [ ] "Lição implícita clara?"
    - [ ] "Conexão emocional estabelecida?"

  scoring: "4+ checks = ✅ Sounds like expert | <3 = Revise"
```

---

## PHASE 4: OUTPUT

### 4.1 Deliverables

```yaml
deliverables:
  voice_context:
    description: "Contexto de voz carregado na sessão"
    includes:
      - "Voice DNA summary"
      - "Story bank available"
      - "Frameworks loaded"

  rewritten_copy:
    description: "Copy reescrita com voz do expert"
    includes:
      - "Original vs Rewritten comparison"
      - "Voice elements applied"
      - "Stories integrated"
```

---

## APPENDIX: CLONE AVAILABILITY

### Available MMOS Clones (as of 2026-02)

```yaml
available_clones:
  experts:
    - jose_carlos_amorim  # Cohort-based courses, AI, Nexialismo
    - alan_nicolas        # AI development, automation

  copywriters:
    - gary_halbert
    - dan_kennedy
    - david_ogilvy
    - eugene_schwartz
    - joe_sugarman
    - ben_settle
    - andre_chaperon
    - stefan_georgi
    - john_carlton
    # ... (check outputs/minds/ for complete list)
```

---

*Task Version: 1.0*
*Integration: MMOS + Copy Squad*
*Created: 2026-02-02*
