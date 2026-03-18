# Estudos de Python

Este repositório contém exercícios e materiais de estudo da linguagem Python.

## 📚 Referências e Material de Estudo - Python

Lista de materiais de apoio e guias de referência utilizados para o estudo e desenvolvimento prático na linguagem Python.

### Guias e Documentação

- **[Python Developer Roadmap](https://roadmap.sh/python):** Trilha visual interativa com os conceitos fundamentais e avançados do ecossistema Python.
- **[W3Schools - Python Tutorial](https://www.w3schools.com/python/):** Guia prático ideal para consulta rápida de sintaxe, métodos integrados e estruturas de dados.

### Cursos em Vídeo - Curso em Vídeo

- **[Mundo 1: Fundamentos](https://youtube.com/playlist?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&si=nbZ0NM2BbrGpkW6_)**: Sintaxe básica, tipos primitivos, operadores lógicos/aritméticos e importação de módulos.
- **[Mundo 2: Estruturas de Controle](https://youtube.com/playlist?list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&si=tqbZDfsHAWq6CPWY)**: Condicionais aninhadas (`if`, `elif`, `else`) e laços de repetição (`for`, `while`).
- **[Mundo 3: Estruturas Compostas](https://youtube.com/playlist?list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&si=ft9qRjTtrOxroNIo)**: Estruturas de dados nativas (Tuplas, Listas, Dicionários), funções e tratamento de erros.
- **[Python POO: Programação Orientada a Objetos](https://youtube.com/playlist?list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3&si=_-jSz6wiEIHJ1Eta)**: Conceitos de Classes, Objetos, Herança, Polimorfismo e Encapsulamento.

## 🛠️ Configuração do Ambiente (venv)

Para evitar conflitos entre bibliotecas e manter o ambiente limpo, recomenda-se o uso de ambientes virtuais (`venv`).

### 1. Criar o ambiente virtual

No terminal, na raiz do projeto, execute:

```bash
python -m venv .venv
```

### 2. Ativar o ambiente virtual

- **Linux/macOS:**
  ```bash
  source .venv/bin/activate
  ```
- **Windows (PowerShell):**
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
- **Windows (CMD):**
  ```cmd
  .\.venv\Scripts\activate.bat
  ```

### 3. Instalar dependências

Com o ambiente ativo, você pode instalar as bibliotecas necessárias:

```bash
pip install nome_da_biblioteca
```

### 4. Desativar o ambiente

Quando terminar, basta executar:

```bash
deactivate
```

### ⚠️ Versionamento e Boas Práticas

**Nunca envie a pasta `.venv` para o Git.** Ela contém arquivos específicos do seu sistema operacional e caminho local. Em vez disso, versione as dependências:

1. **Gerar lista de dependências:**
   ```bash
   pip freeze > requirements.txt
   ```
2. **Instalar dependências de um projeto existente:**
   ```bash
   pip install -r requirements.txt
   ```

Certifique-se de que o seu arquivo `.gitignore` contenha a entrada `.venv/`.

---
