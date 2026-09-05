# AgentFlix — versão 2

O símbolo A forma a primeira letra de AGENTFLIX. Não há ícone adicional nem A duplicado. O play é um path independente, com preenchimento próprio.

## Cores e contraste
- Dark: A e FLIX ciano #30B0C7, GENT branco quente #F0EEE6, play branco #FFFFFF, fundo carvão #14161A.
- Light: A e FLIX ciano, GENT e play carvão #14161A, fundo branco quente.
- Monocromáticas: todos os elementos pretos ou brancos.
- Avatar ciano: símbolo carvão e play branco.

## Arquivos
Todos os SVGs são vetores reais; não contêm bitmaps, texto dependente de fontes nem filtros. Tipografia DejaVu Sans Bold em curvas. Geometria regularizada a partir da imagem aprovada; raster de estudo não é usado como imagem embutida.

- horizontal-dark/light: 1600 × 320, com fundo.
- horizontal-transparente-dark/light: para sobrepor respectivamente em superfícies escuras ou claras.
- vertical: composição AGENT em cima e FLIX embaixo, 1000 × 700.
- simbolo-dark/light: 512 × 512, transparente; escolha conforme a superfície.
- avatar-quadrado: 1024 × 1024, para WhatsApp/GitHub com recorte circular automático.
- avatar-circular: círculo pronto e exterior transparente.
- favicon-dark/light: SVG, PNG de 64 px e ICO com 16/32/48/64 px. O SVG permanece nítido em qualquer escala.
- PNGs exportados de cada SVG; avatares quadrados também em JPG.

## Site
Use horizontal-transparente-dark.svg no tema escuro e horizontal-transparente-light.svg no tema claro. Não basta alterar o fundo: troque o arquivo para preservar o contraste do play.

Exemplo de favicon com superfície escura própria:
<link rel="icon" type="image/svg+xml" href="/favicon-dark.svg">
<link rel="icon" sizes="any" href="/favicon-dark.ico">

Use SVG em interfaces que o aceitam. Nos serviços de avatar que exigem bitmap, envie o PNG de 1024 px. Não distorça proporções. Prefira o símbolo quando o espaço for pequeno.
