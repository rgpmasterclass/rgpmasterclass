import streamlit as st
from twilio.rest import Client

# Credenciais Twilio
account_sid = 'ACd06323047f5c26c22e466372b9e52e82'
auth_token = '2a00ca945416ca7bb324fbf72d4e14f8'
client = Client(account_sid, auth_token)

def enviar_mensagem(numero, mensagem):
    from_whatsapp_number = 'whatsapp:+17602922639'
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
