import streamlit as st
from twilio.rest import Client

# Credenciais Twilio
account_sid = 'SEU_ACCOUNT_SID'
auth_token = 'SEU_AUTH_TOKEN'
client = Client(account_sid, auth_token)

def enviar_mensagem(numero, mensagem):
    from_whatsapp_number = 'whatsapp:+SEU_NUMERO'
    to_whatsapp_number = f'whatsapp:+{numero}'
    message = client.messages.create(
        body=mensagem,
        from_=from_whatsapp_number,
        to=to_whatsapp_number
    )
    return message.sid

st.title("Envio Massivo no WhatsApp")
mensagem = st.text_area("Mensagem:")
numeros = st.text_area("Números (um por linha):")

if st.button("Enviar"):
    if mensagem and numeros:
        numeros_list = numeros.split("\n")
        for numero in numeros_list:
            try:
                sid = enviar_mensagem(numero.strip(), mensagem)
                st.success(f"Enviado para {numero}")
            except Exception as e:
                st.error(f"Erro no número {numero}: {str(e)}")
    else:
        st.warning("Preencha todos os campos.")
