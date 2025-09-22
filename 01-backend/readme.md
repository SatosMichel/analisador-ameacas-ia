# Projeto: Análise de Ameaças STRIDE com IA

## 🎯 Objetivo

Este projeto, desenvolvido como parte de um desafio da DIO, implementa uma aplicação web que utiliza Inteligência Artificial para realizar uma análise de ameaças em diagramas de arquitetura de software, baseada na metodologia **STRIDE**. O usuário pode fazer o upload de uma imagem da arquitetura, e a aplicação retorna uma lista de potenciais vulnerabilidades e sugestões de mitigação.

> **Status do Projeto:** Atualmente, a integração com a API da Azure OpenAI está pausada devido a limitações de cota na plataforma Azure. A aplicação está 100% funcional utilizando uma **API Mockada (Simulada)** que retorna uma análise de exemplo. Isso permite demonstrar toda a estrutura do frontend, backend e a interação entre eles. O código para a integração real está preservado e comentado no `main.py` para futura ativação.

## ✨ Funcionalidades Principais

-   **Upload de Imagem:** Interface simples para o usuário selecionar e enviar uma imagem de diagrama de arquitetura.
-   **API Backend:** Um serviço construído com **FastAPI** que recebe a imagem.
-   **Análise de Ameaças (Simulada):** A API processa a requisição e retorna uma análise detalhada, categorizada pelo mnemônico STRIDE:
    -   **S**poofing (Falsificação de Identidade)
    -   **T**ampering (Adulteração de Dados)
    -   **R**epudiation (Repúdio)
    -   **I**nformation Disclosure (Divulgação de Informações)
    -   **D**enial of Service (Negação de Serviço)
    -   **E**levation of Privilege (Elevação de Privilégio)
-   **Visualização de Resultados:** O frontend exibe a análise de forma clara e organizada em tabelas.

## 🛠️ Tecnologias Utilizadas

-   **Backend:** Python 3, FastAPI, Uvicorn
-   **Frontend:** HTML5, CSS3, JavaScript (puro)
-   **Bibliotecas Python:** `python-dotenv`, `python-multipart`

## 🚀 Como Executar o Projeto Localmente

Siga os passos abaixo para rodar a aplicação em seu ambiente.

### Pré-requisitos

-   Python 3.8 ou superior
-   Um ambiente virtual (recomendado)

### Passos

1.  **Clone ou baixe o repositório:**
    Primeiro, certifique-se de que o projeto está na sua máquina, no caminho:
    `C:\Users\Computador Sala\Documents\Projeto agente de detecção`

2.  **Abra o terminal na pasta raiz do projeto:**
    Você pode navegar até a pasta usando o comando `cd` no seu terminal (PowerShell, CMD, etc.).
    ```powershell
    cd "C:\Users\Computador Sala\Documents\Projeto agente de detecção"
    ```

3.  **Crie e ative um ambiente virtual:**
    Este comando cria uma pasta `venv` dentro do seu projeto para isolar as dependências.
    ```bash
    # Criar o ambiente virtual
    python -m venv venv
    
    # Ativar o ambiente (no Windows PowerShell)
    .\venv\Scripts\Activate.ps1
    # ou se estiver usando CMD: .\venv\Scripts\activate.bat
    ```
    Após a ativação, você verá `(venv)` no início do seu prompt.

4.  **Instale as dependências:**
    Este comando lê o arquivo `requirements.txt` e instala todas as bibliotecas necessárias.
    ```bash
    pip install -r 01-backend/requirements.txt
    ```

5.  **Execute a API com Uvicorn:**
    Com o terminal ainda na pasta raiz (`Projeto agente de detecção`) e o ambiente virtual ativo, execute o seguinte comando:
    ```bash
    uvicorn 01-backend.main:app --reload
    ```

6.  **Acesse a aplicação:**
    Após o servidor iniciar, abra seu navegador e acesse o endereço:
    [http://127.0.0.1:8000](http://127.0.0.1:8000)

A página inicial será carregada, e você poderá testar o fluxo de upload e receber a análise simulada.

## 🧠 Engenharia de Prompt (Planejada)

A inteligência da análise reside no prompt enviado ao modelo de IA. O prompt foi desenhado para instruir a IA a atuar como um especialista em segurança e a formatar a saída em um JSON estruturado, facilitando a exibição no frontend.

```text
Você é um especialista sênior em cibersegurança e threat modeling. Sua principal habilidade é analisar diagramas de arquitetura de software e identificar vulnerabilidades com base na metodologia STRIDE.

Analise a imagem da arquitetura fornecida e identifique ameaças potenciais para cada uma das categorias STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege).

Para cada ameaça identificada, forneça uma descrição clara e uma sugestão de mitigação.

A saída deve ser um objeto JSON válido, sem nenhum texto ou formatação adicional fora do JSON. A estrutura deve ser a seguinte:
{
  "spoofing": [{"threat": "Descrição da ameaça", "mitigation": "Sugestão de mitigação"}],
  "tampering": [{"threat": "Descrição da ameaça", "mitigation": "Sugestão de mitigação"}],
  "repudiation": [{"threat": "Descrição da ameaça", "mitigation": "Sugestão de mitigação"}],
  "information_disclosure": [{"threat": "Descrição da ameaça", "mitigation": "Sugestão de mitigação"}],
  "denial_of_service": [{"threat": "Descrição da ameaça", "mitigation": "Sugestão de mitigação"}],
  "elevation_of_privilege": [{"threat": "Descrição da ameaça", "mitigation": "Sugestão de mitigação"}]
}
Se nenhuma ameaça for encontrada para uma categoria, retorne um array vazio para ela.
```