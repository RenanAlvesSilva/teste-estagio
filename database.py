from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

class GetDataBase:
    def get_supabase_client(self):
        try:
            SUPABASE_URL = os.environ.get('SUPABASE_URL')
            SUPABASE_KEY = os.environ.get('SUPABASE_KEY')
            supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
            return supabase
        except Exception as e:
            print('Erro ao criar cliente Supabase:', e)
            return None
        
        
    def buscar_contatos(self):
        try:
            client = self.get_supabase_client()
            response = client.table(os.environ.get('TABLE_NAME')).select("*").execute()
            print('Dados retornados com sucesso')
            print(response.data)
            if not response.data:
                print('Nenhum contato encontrado.')
                return []
            return response.data
        except Exception as e:
            print('Erro ao buscar contatos:', e)
            return {"error": str(e)}
        

