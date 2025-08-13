# Teste Estágio - Envio de Mensagens via API WhatsApp Pegando informações do SupaBase

Projeto desenvolvido para Teste de Estágio, Objetivo : Buscar informações do SupaBase e enviar mensagem através da API Z-API, Enviando nome na mensagem e enviando para o número salvo no SupaBase.

## 🔧 Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Supabase**: Banco de dados utilizado para armazenar contatos.
- **Z-API**: API para envio de mensagens via WhatsApp.
- **dotenv**: Gerenciamento de variáveis de ambiente.
- **requests**: Envio de requisições HTTP.

## 🛠️ Estrutura do Projeto

- `database.py`: Contém a classe `GetDataBase` responsável pela interação com o banco de dados Supabase.
- `messages.py`: Funções para formatação e envio de mensagens via Z-API.
- `main.py`: Script principal que orquestra o processo de busca de contatos e envio de mensagens.
- `.env`: Arquivo de configuração contendo variáveis de ambiente sensíveis.
- `.gitignore`: Arquivo para ignorar arquivos e pastas que não devem ser versionados.

- # 🛠️ Estrutura do SupaBase
- `Nome da Tabela`: whatsapp_contact
- `ID`: Criação de ID de forma automática a partir da inserção de um novo registro.
- `Create_at`: Data e hora da inserção de um novo registro.
- `nome_contato`: Nome do contato que será salvo no banco de dados.
- `telefone_contato`: Telefone do contato que será salvo no banco de dados.

- # 🛠️ Estrtura .env
- `SUPABASE_URL`: Passando API URL do SupaBase
- `SUPABASE_KEY`: Passando a Key do SupaBase API
- `INSTANCE_ZAP_ID`: Passando a Instance ID da API do Z-API
- `TOKEN_ZAP`: Passando Token da API do Z-API
- `SECURE_TOKEN`: Passando o Secure Token do Z-API
- `TABLE_NAME`: Passando o nome da tabela do SupaBase

## ⚙️ Como Executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/RenanAlvesSilva/teste-estagio.git
   cd teste-estagio

2. Crie um ambiente virtual:
   ```bash
   virtualenv venv
   venv\Scripts\activate (versão windowns)
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
4. Execute o programa:
   ```bash
   python main.py

Observação: .venv já está no projeto, não será necessário ser criado.
