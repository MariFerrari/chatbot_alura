# Professor crIAtivo - Seu Assistente Inteligente para Planejamento de Aulas Inovadoras

## Descrição

O Professor crIAtivo é uma aplicação web que auxilia professores no planejamento de aulas criativas e alinhadas à Base Nacional Comum Curricular (BNCC). 
Utilizando o poder de agentes inteligentes baseados em modelos de linguagem, a aplicação oferece funcionalidades como:

* **Geração de Ideias de Aula com Agentes:** Ao fornecer um tópico, três agentes distintos (Pesquisador Pedagógico, Coordenador Pedagógico e Professor crIAtivo) colaboram para gerar ideias de aula embasadas em pesquisa, avaliação pedagógica e um plano de aula inicial.
* **Geração de Sugestões de Atividades (Formulário Pedagógico):** Um formulário permite refinar a busca por atividades, especificando a série/ano da turma, disciplina, tema da aula e metodologia de ensino desejável. A aplicação gera sugestões de atividades criativas e relevantes, considerando a BNCC.
* **Opção de Salvar Sugestões:** As sugestões de atividades geradas podem ser salvas em um arquivo de texto para referência futura.

## Tecnologias Utilizadas:

* **Python:** Linguagem de programação principal para a lógica do backend e dos agentes inteligentes.
* **Google AI Gemini API e Agents Framework (ADK):** Utilizados para criar e executar os agentes inteligentes para geração de ideias e sugestões.
* **Flask:** Microframework web Python para construir a interface web e lidar com as requisições do usuário.


## Pré-requisitos

* **Python 3.x** instalado no seu sistema.
* **Gerenciador de pacotes Pip** (instalado com Python).
* **Uma chave de API do Google AI Gemini:** Você precisará obter uma chave de API do Google AI Studio e configurá-la como uma variável de ambiente.

## Configuração

1.  **Clone o repositório (se aplicável):**
    ```bash
    git clone [https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content)
    cd professor_criativo
    ```

2.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Linux/macOS
    venv\Scripts\activate  # No Windows
    ```

3.  **Instale as dependências:**
    ```bash
    pip install flask Flask-Markdown ipython google-generativeai google-adk
    ```

4.  **Configure a chave de API do Google AI:**
    * Obtenha uma chave de API do Google AI Studio ([https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)).
    * Defina a chave de API como uma variável de ambiente chamada `GOOGLE_API_KEY`. No Linux/macOS:
        ```bash
        export GOOGLE_API_KEY="SUA_CHAVE_DE_API"
        ```
        No Windows (Prompt de Comando):
        ```bash
        set GOOGLE_API_KEY="SUA_CHAVE_DE_API"
        ```
        No Windows (PowerShell):
        ```powershell
        $env:GOOGLE_API_KEY = "SUA_CHAVE_DE_API"
        ```
        Você pode adicionar essa configuração ao seu arquivo `.bashrc`, `.zshrc` ou similar para que seja carregada automaticamente.

