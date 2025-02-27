# Envio de mensagens personalizadas pelo Twilio Sendgrid (modelo dinâmico, templates)
# Personalizar mensagens de acordo com dados de arquivo Excel

import pandas as pd
from pandasql import sqldf

from sendgrid import SendGridAPIClient # faz conexão com a conta do sengrid
from sendgrid.helpers.mail import Mail # cria o e-mail

from chave_sendgrid import chave_api_sendgrid 

# acessar conta sendgrid
conta_sendgrid = SendGridAPIClient(chave_api_sendgrid)

# função para enviar emails especifícos com mensagens personalizadas para cada email
def enviar_emails(destinatarios):

    if not destinatarios:  # verifica se a lista de destinatários está vazia
        print('Não há destinatários para enviar e-mails.')
        return  # retorna da função sem fazer nada
    
    for destinatario in destinatarios: # para cada destinatario em destinatarios
        nome = destinatario['Cliente']
        email = destinatario['Email']
        
        message = Mail(
                    from_email='seu_email_verificado_no_sendgrid@gmail.com',
                    to_emails=destinatario['Email'],
                    subject='Assunto do E-mail',
                )
        message.template_id = "d-ed948bcd9ff347269d5e9288e62fad24"  # substitua pelo ID do modelo dinâmico criado no sendgrid
        message.dynamic_template_data = {'first_name': destinatario['Cliente'], }
        
        try:
            response = conta_sendgrid.send(message)
            print(f'E-mail enviado para {nome} <{email}> com status: {response.status_code}')
        except Exception as e:
            print(f'Erro ao enviar e-mail para {nome} <{email}>: {e}')

# base de dados
df = pd.read_excel('email_clientes.xlsx')


# função defini os clientes que receberão os e-mails
def query_table(query_text):
    result = sqldf(query_text, globals())
    return result


# emails dos clientes da região Sul 
df_cliente_email = query_table('''SELECT Email, Cliente FROM df WHERE Region = 'Sul' ''')

# lista de dicionários, chaves Email e Cliente
dados_destinatarios = df_cliente_email.to_dict(orient='records') # records indica transformação para lista de dicionários, cabeçalhos a chave



enviar_emails(dados_destinatarios)
