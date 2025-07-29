import streamlit as st
from datetime import datetime
from PIL import Image

st.set_page_config(page_title="Coleta Rápida", layout="centered")

st.title("📸 Coleta Rápida - Upload de Fichas")

# Upload da imagem
imagem = st.file_uploader("Envie a imagem da ficha preenchida (foto ou escaneado)", type=["jpg", "jpeg", "png", "pdf"])

if imagem:
    st.success("Imagem recebida com sucesso!")
    st.image(imagem, caption="Pré-visualização", use_column_width=True)
    st.info("🔍 A extração de dados será feita automaticamente após o envio final.")

# Campo extra para observações
obs = st.text_area("Observações adicionais (opcional)")

# Botão de envio
if st.button("Enviar"):
    if imagem:
        st.success("✅ Ficha enviada com sucesso!")
        st.write("📅 Data de envio:", datetime.today().strftime("%d/%m/%Y"))
        if obs:
            st.write("📝 Observações:", obs)
    else:
        st.warning("⚠️ Por favor, envie uma imagem antes de confirmar.")
