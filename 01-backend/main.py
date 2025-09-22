import os
import base64
import tempfile
from openai import AzureOpenAI
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware

env_path = Path(__file__).resolve(strict=True).parent / ".env"
load_dotenv(dotenv_path=env_path)

# Carregar as variáveis de ambiente do arquivo .env
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens (ajuste conforme necessário)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_mock_analysis():
    """
    Esta função retorna um JSON fixo que simula a resposta da IA.
    É uma análise STRIDE de exemplo para uma aplicação web genérica.
    """
    mock_data = {
      "spoofing": [
        {"threat": "Um atacante pode se passar por um usuário legítimo se as senhas forem fracas ou roubadas.", "mitigation": "Implementar autenticação de múltiplos fatores (MFA) e políticas de senha forte."},
        {"threat": "A API pode ser vulnerável a ataques de 'replay' se não houver tokens de uso único.", "mitigation": "Utilizar nonces ou tokens de requisição com tempo de expiração."}
      ],
      "tampering": [
        {"threat": "Dados em trânsito entre o cliente e o servidor podem ser alterados se a comunicação não for criptografada.", "mitigation": "Forçar o uso de HTTPS (TLS) em todas as comunicações."},
        {"threat": "Um atacante com acesso ao banco de dados poderia alterar registros sem ser detectado.", "mitigation": "Implementar logs de auditoria detalhados no banco de dados e controle de acesso restrito."}
      ],
      "repudiation": [
        {"threat": "Um usuário pode negar ter realizado uma transação crítica (ex: uma compra) se não houver logs suficientes.", "mitigation": "Registrar todas as ações críticas em logs de auditoria imutáveis, incluindo IP, timestamp e ID do usuário."}
      ],
      "information_disclosure": [
        {"threat": "Mensagens de erro detalhadas podem vazar informações sobre a tecnologia do backend (ex: versões de software).", "mitigation": "Configurar mensagens de erro genéricas para o usuário final e registrar os detalhes completos apenas nos logs do servidor."},
        {"threat": "Dados sensíveis podem estar expostos em backups não criptografados.", "mitigation": "Criptografar todos os backups de banco de dados."}
      ],
      "denial_of_service": [
        {"threat": "A API pode ser sobrecarregada com um grande número de requisições, tornando o serviço indisponível.", "mitigation": "Implementar Rate Limiting (limitação de taxa) e um Web Application Firewall (WAF)."},
        {"threat": "O processo de upload de arquivos grandes pode consumir todos os recursos do servidor.", "mitigation": "Limitar o tamanho máximo dos arquivos de upload e processá-los de forma assíncrona."}
      ],
      "elevation_of_privilege": [
        {"threat": "Um usuário comum pode conseguir acesso a rotas de administrador se o controle de acesso não for aplicado em cada endpoint.", "mitigation": "Centralizar e aplicar a verificação de permissões em cada requisição na API, não confiando apenas no frontend."}
      ]
    }
    return mock_data

app = FastAPI(title="Analisador de Ameaças STRIDE (Versão Mockada)")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Serve a página principal do frontend."""
    # O caminho do arquivo HTML agora é relativo à localização do main.py
    frontend_path = Path(__file__).resolve().parent.parent / "02-frontend" / "index.html"
    with open(frontend_path) as f:
        return HTMLResponse(content=f.read(), status_code=200)

@app.post("/analyze")
async def analyze_architecture(file: UploadFile = File(...)):
    """
    Endpoint que recebe a imagem e retorna a análise STRIDE MOCKADA.
    """
    print(f"Recebido arquivo: {file.filename}")
    
    # Simula o tempo de processamento da IA
    await asyncio.sleep(2)

    # Retorna a análise simulada
    analysis_json = get_mock_analysis()

    return JSONResponse(content=analysis_json)
