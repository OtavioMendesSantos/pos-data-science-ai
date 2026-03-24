# Estudos de R - Matemática Computacional

Este repositório contém exercícios e materiais de estudo da linguagem R, focados em Matemática Computacional e Ciência de Dados.

## 📚 Referências e Material de Estudo - R

Lista de materiais de apoio e guias de referência utilizados para o estudo e desenvolvimento prático na linguagem R.

### Guias e Documentação

- **[R Project Official Website](https://www.r-project.org/):** Documentação oficial e download da linguagem R.
- **[W3Schools - R Tutorial](https://www.w3schools.com/r/r_intro.asp):** Guia prático ideal para consulta rápida de sintaxe, tipos de dados e funções básicas.
- **[R for Data Science (2e)](https://r4ds.hadley.nz/):** Referência fundamental para manipulação, visualização e análise de dados em R (Tidyverse).
- **[Posit Cheatsheets](https://posit.co/resources/cheatsheets/):** Folhas de consulta rápida para pacotes como `ggplot2`, `dplyr`, `tidyr` e a própria linguagem R.

### Cursos e Comunidade

- **[Curso-R](https://curso-r.com/):** Excelente material em português sobre R e ciência de dados.
- **[R-Bloggers](https://www.r-bloggers.com/):** Agregador de blogs sobre R para acompanhar novidades e tutoriais da comunidade.

## 🚀 Como Executar os Projetos

Os documentos deste repositório utilizam o formato **Quarto (`.qmd`)**, que combina código R, texto (Markdown) e resultados dinâmicos. Escolha uma das três opções abaixo para executar os arquivos:

### Opção 1: Posit Cloud (Sem instalação)

Ambiente em nuvem nativo, ideal para execução imediata sem necessidade de configurar infraestrutura local.

1. Acesse [posit.cloud](https://posit.cloud) e faça login.
2. Crie um novo projeto clicando em **New Project > New RStudio Project** (ou selecione _New Project from Git Repository_ para clonar este repositório diretamente).
3. Caso não tenha clonado via Git, faça o upload dos arquivos `.qmd` utilizando o painel inferior direito (**Files > Upload**).
4. Abra o arquivo `.qmd` desejado e clique no botão **Render** na barra superior do editor para compilar o documento.

### Opção 2: Ambiente Local (VS Code)

Para execução local utilizando o Visual Studio Code.

#### Requisitos

- **Quarto CLI:** [Instalador do Quarto](https://quarto.org/docs/get-started/).
- **R Base:** Instalação da linguagem R no seu sistema operacional.
- **Pacotes R:** Instale os motores de renderização rodando `install.packages(c("rmarkdown", "knitr"))` no console do R.
- **Extensões do VS Code:** - [Quarto](https://marketplace.visualstudio.com/items?itemName=quarto.quarto)
  - [R Extension](https://marketplace.visualstudio.com/items?itemName=REditorSupport.r)

#### Execução

1. Abra o arquivo `.qmd` (ex: `src/aula-4/Aula4.qmd`) no VS Code.
2. **Renderização Completa:** Clique no botão **Render** (ícone de play no canto superior direito) ou use o atalho `Ctrl+Shift+K` (Windows/Linux) / `Cmd+Shift+K` (macOS).
3. **Execução Parcial:** Execute blocos de código (`chunks`) individualmente clicando em **Run Cell** logo acima do bloco ou usando `Ctrl+Shift+Enter`.

### Opção 3: Contêiner Docker (Isolamento Total)

Para rodar localmente sem instalar o R e suas dependências diretamente no sistema operacional, utilizando a imagem oficial `rocker/verse` que já inclui RStudio, Quarto e pacotes de Data Science.

#### Execução

No terminal, na raiz deste repositório, execute o seguinte comando:

```bash
docker run --rm -d -p 8787:8787 -e PASSWORD=senha_temporaria -v "$(pwd)":/home/rstudio/projeto rocker/verse
```

O Gemini disse
Aqui está o README atualizado com a terceira opção detalhando o uso do Docker e seus parâmetros.

Markdown
# Estudos de R - Matemática Computacional

Este repositório contém exercícios e materiais de estudo da linguagem R, focados em Matemática Computacional e Ciência de Dados.

## 📚 Referências e Material de Estudo - R

Lista de materiais de apoio e guias de referência utilizados para o estudo e desenvolvimento prático na linguagem R.

### Guias e Documentação

- **[R Project Official Website](https://www.r-project.org/):** Documentação oficial e download da linguagem R.
- **[W3Schools - R Tutorial](https://www.w3schools.com/r/r_intro.asp):** Guia prático ideal para consulta rápida de sintaxe, tipos de dados e funções básicas.
- **[R for Data Science (2e)](https://r4ds.hadley.nz/):** Referência fundamental para manipulação, visualização e análise de dados em R (Tidyverse).
- **[Posit Cheatsheets](https://posit.co/resources/cheatsheets/):** Folhas de consulta rápida para pacotes como `ggplot2`, `dplyr`, `tidyr` e a própria linguagem R.

### Cursos e Comunidade

- **[Curso-R](https://curso-r.com/):** Excelente material em português sobre R e ciência de dados.
- **[R-Bloggers](https://www.r-bloggers.com/):** Agregador de blogs sobre R para acompanhar novidades e tutoriais da comunidade.

## 🚀 Como Executar os Projetos

Os documentos deste repositório utilizam o formato **Quarto (`.qmd`)**, que combina código R, texto (Markdown) e resultados dinâmicos. Escolha uma das três opções abaixo para executar os arquivos:

### Opção 1: Posit Cloud (Sem instalação)

Ambiente em nuvem nativo, ideal para execução imediata sem necessidade de configurar infraestrutura local.

1. Acesse [posit.cloud](https://posit.cloud) e faça login.
2. Crie um novo projeto clicando em **New Project > New RStudio Project** (ou selecione *New Project from Git Repository* para clonar este repositório diretamente).
3. Caso não tenha clonado via Git, faça o upload dos arquivos `.qmd` utilizando o painel inferior direito (**Files > Upload**).
4. Abra o arquivo `.qmd` desejado e clique no botão **Render** na barra superior do editor para compilar o documento.

### Opção 2: Ambiente Local (VS Code)

Para execução local utilizando o Visual Studio Code.

#### Requisitos
- **Quarto CLI:** [Instalador do Quarto](https://quarto.org/docs/get-started/).
- **R Base:** Instalação da linguagem R no seu sistema operacional.
- **Pacotes R:** Instale os motores de renderização rodando `install.packages(c("rmarkdown", "knitr"))` no console do R.
- **Extensões do VS Code:** - [Quarto](https://marketplace.visualstudio.com/items?itemName=quarto.quarto)
  - [R Extension](https://marketplace.visualstudio.com/items?itemName=REditorSupport.r)

#### Execução
1. Abra o arquivo `.qmd` (ex: `src/aula-4/Aula4.qmd`) no VS Code.
2. **Renderização Completa:** Clique no botão **Render** (ícone de play no canto superior direito) ou use o atalho `Ctrl+Shift+K` (Windows/Linux) / `Cmd+Shift+K` (macOS).
3. **Execução Parcial:** Execute blocos de código (`chunks`) individualmente clicando em **Run Cell** logo acima do bloco ou usando `Ctrl+Shift+Enter`.

### Opção 3: Contêiner Docker (Isolamento Total)

Para rodar localmente sem instalar o R e suas dependências diretamente no sistema operacional, utilizando a imagem oficial `rocker/verse` que já inclui RStudio, Quarto e pacotes de Data Science.

#### Execução
No terminal, na raiz deste repositório, execute o seguinte comando:

```bash
docker run --rm -d -p 8787:8787 -e PASSWORD=senha_temporaria -v "$(pwd)":/home/rstudio/projeto rocker/verse
```

(Nota: Se estiver utilizando o Prompt de Comando padrão do Windows, substitua "$(pwd)" por "%cd%").

Explicação dos Parâmetros:

`--rm`: Exclui o contêiner automaticamente quando ele for parado, evitando acúmulo de lixo no sistema.

`-d`: (Detached) Roda o contêiner em segundo plano, liberando o terminal para outros comandos.

`-p 8787:8787`: Expõe a porta interna do RStudio (8787) para a porta 8787 do seu localhost.

`-e PASSWORD=senha_temporaria`: Define uma variável de ambiente criando a senha obrigatória de acesso.

`-v "$(pwd)"`:/home/rstudio/projeto: Cria um volume que espelha a pasta atual da sua máquina para dentro do contêiner. Isso garante que as alterações nos arquivos .qmd sejam salvas no seu disco local de forma permanente.

Acesso
Abra o navegador web e acesse: http://localhost:8787

Usuário: rstudio

Senha: senha_temporaria

Acesse a pasta projeto na interface do RStudio para visualizar e editar os arquivos.


