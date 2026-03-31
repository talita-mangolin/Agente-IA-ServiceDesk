import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Configurações iniciais
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.5-flash")

# TÍTULO DA INTERFACE (Aqui você pode usar HTML/CSS)
st.set_page_config(page_title="IA Triagem N1", page_icon="🤖")

st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    .stButton>button { width: 100%; background-color: #4CAF50; color: White; }
    .stButton>button:hover {
    background-color: #0055aa; 
    cursor: pointer; /* Transforma a seta do mouse na "mãozinha" */
}
    .stMarkdown {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        border-left: 8px solid #ff4b4b; /* Vermelho para destaque de criticidade */
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 Agente de Triagem - Service Desk")
st.subheader("Análise inteligente de tickets via Agente IA")

# Campo de entrada
pergunta = st.text_area("Descreva o problema técnico aqui:", placeholder="Ex: VPN não conecta...")

if st.button("Analisar Ticket"):
    if pergunta:
        with st.spinner('Analisando impacto e categoria...'):
            # O prompt que você já criou
            prompt_instrucao = f"Analise como Especialista de Service Desk: {pergunta}"
            response = model.generate_content(prompt_instrucao)
            
            # Exibição do resultado
            st.success("Análise Concluída!")
            st.markdown(response.text)
    else:
        st.warning("Por favor, digite o problema antes de analisar.")