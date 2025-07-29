import streamlit as st
import datetime
import pandas as pd
from google.oauth2 import service_account
import gspread

st.set_page_config(page_title="Coleta Rápida", layout="centered")

st.title("📋 Coleta Rápida - Fichas ACS")

st.markdown("Preencha os campos da ficha:")

# Formulário
with st.form("ficha_form"):
    familia = st.text_input("Família (ex: FAM001)")
    nome = st.text_input("Nome completo")
    data_nasc = st.date_input("Data de nascimento", min_value=datetime.date(1900, 1, 1))
    sexo = st.selectbox("Sexo", ["[não informado]", "Masculino", "Feminino", "Outro"])
    mae = st.text_input("Nome da mãe")
    pai = st.text_input("Nome do pai")
    nasc_mun = st.text_input("Município de nascimento")
    resid_mun = st.text_input("Município de residência")
    cpf = st.text_input("CPF")
    cns = st.text_input("CNS")
    telefones = st.text_input("Telefones")
    observacoes = st.text_area("Observações adicionais")
    imagem = st.text_input("Fonte da Imagem (ex: FAM001.jpg)")

    submitted = st.form_submit_button("Salvar dados")

# Cálculo da idade
def calcular_idade(nascimento):
    hoje = datetime.date.today()
    return hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))

# Salvamento
if submitted:
    idade = calcular_idade(data_nasc)
    hoje_str = datetime.date.today().strftime("%d/%m/%Y")

    nova_linha = [familia, nome, data_nasc.strftime("%d/%m/%Y"), idade, sexo, mae, pai,
                  nasc_mun, resid_mun, cpf, cns, telefones, observacoes, imagem, hoje_str]

    # Autenticação com o Google Sheets
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )

    client = gspread.authorize(credentials)
    sheet = client.open("Fichas_Coletadas_Modelo").sheet1
    sheet.append_row(nova_linha)

    st.success("✅ Dados salvos com sucesso!")