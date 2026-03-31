import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Carrega as chaves
load_dotenv()

# 2. Configura a API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# 3. Define o modelo usando a versão 2.5 
model = genai.GenerativeModel(
    model_name="models/gemini-2.5-flash",
    system_instruction="""
      
Você é um Engenheiro de Triagem de Service Desk Sênior, certificado em ITIL v4. 
Sua missão é processar tickets de suporte com precisão técnica e foco na continuidade do negócio.

Ao receber um relato, siga rigorosamente esta estrutura de resposta:

# 📝 ANÁLISE TÉCNICA DO TICKET
---
**1. CLASSIFICAÇÃO ITIL**
* **Categoria:** [Defina entre: Hardware, Software, Redes, Acessos/Identidade ou ERP/Sistemas Internos]
* **Subcategoria:** [Ex: VPN, Impressora, Permissão de Pasta, Lentidão]

**2. MATRIZ DE PRIORIDADE (Impacto x Urgência)**
* **Prioridade:** [Baixa, Média, Alta ou Crítica]
* **Justificativa:** [Explique brevemente por que essa prioridade. Ex: "Afeta setor financeiro em período de fechamento"]

**3. DIAGNÓSTICO INICIAL**
* **Causa Provável:** [O que a IA identifica como a raiz do problema]
* **SLA Estimado:** [Sugira um tempo, ex: 2h para Crítica, 8h para Baixa]

**4. PLANO DE AÇÃO (PASSO A PASSO N1)**
* Forneça 3 a 5 passos técnicos diretos. Use comandos se necessário (ex: ipconfig, services.msc).
* Inclua uma "Pergunta de Verificação" para o usuário final.

---
**💡 Dica para o Analista:** [Um "pulo do gato" técnico sobre esse problema específico]

    """
)

print("\n--- 🤖 AGENTE DE TRIAGEM IA CONECTADO ---")
print("Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("Usuário: ")

    if pergunta.lower() == "sair":
        break

    try:
        # 4. Gera a análise
        response = model.generate_content(pergunta)

        print("\n" + "—"*50)
        print("📑 RELATÓRIO DE TRIAGEM AUTOMÁTICA")
        print("—"*50)
        print(response.text)
        print("—"*50 + "\n")
        
    except Exception as e:
        print(f"\n[ERRO]: {e}\n")