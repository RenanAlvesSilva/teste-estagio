from database import GetDataBase
from messages import SendMessagerWhatsapp


def main():
    db = GetDataBase()
    buscar = db.buscar_contatos()
    send_messages = SendMessagerWhatsapp()
    for contatos in buscar:
        nome = contatos['nome_contato']
        telefone = contatos['telefone_contato']
        if not telefone or not nome:
            print(f"Contato inválido: {contatos} ...")
            return 
        if telefone and nome:
            messages = f"Olá {nome}, tudo bem com você ?"
            send_messages.send_message(telefone, messages)
            print(f'Mensagem enviada para {nome} no telefone {telefone}')
        
        
if __name__ == "__main__":
    main()
    

