import requests
import os 
from dotenv import load_dotenv

load_dotenv()

class SendMessagerWhatsapp():
    
    def send_message(self, telefone, message):
        INSTANCE_ID = os.environ.get("INSTANCE_ZAP_ID")
        INSTANCE_TOKEN = os.environ.get("TOKEN_ZAP")
        SECURE_TOKEN = os.environ.get("SECURE_TOKEN_ZAP")
        
        API = f"https://api.z-api.io/instances/{INSTANCE_ID}/token/{INSTANCE_TOKEN}/send-text"
        payload = {
        "phone": telefone,
        "message": message,
        "delayMessage": 15,
        }
        headers = {
            "Client-token": SECURE_TOKEN,
            "Content-Type": "application/json"
        }
        try:
            response = requests.post(
                API, json=payload, headers=headers
            )
            print("Status Code:", response.status_code)
            resp_json = response.json()
            print("Response JSON:", resp_json)
            if response.status_code != 200:
                print('Erro na resposta da API:', resp_json)
            else:
                print('Mensagem enviada com sucesso!')
            return resp_json
        except Exception as e:
            print('Erro ao enviar mensagem:', e)
            return {"error": str(e)}