# Envio de mensagens personalizadas pelo Twilio Sendgrid
# Personalizar mensagens de acordo com dados do banco MySQL

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from chave_sendgrid import chave_api_sendgrid 
from connection_mysql import df



sg = SendGridAPIClient(chave_api_sendgrid)

def enviar_emails(destinatarios):
    if not destinatarios:  # verifica se a lista de destinatários está vazia
        print('Não há destinatários para enviar e-mails.')
        return  # retorna da função sem fazer nada
     
    for destinatario in destinatarios:
        nome = destinatario['nome']
        email = destinatario['email']
        
        mensagem = Mail(
            from_email='seu_email_verificado_no_sendgrid@gmail.com',
            to_emails=email,
            subject='Olá, {}'.format(nome),
            html_content='<strong>Comunicamos ao Sr(a){},</strong><br>que o seu pedido foi enviado com sucesso.'.format(nome)
        )
        
        try:
            response = sg.send(mensagem)
            print(f'E-mail enviado para {nome} <{email}> com status: {response.status_code}')
        except Exception as e:
            print(f'Erro ao enviar e-mail para {nome} <{email}>: {e}')



# lista de dicionários
destinatarios = df.to_dict(orient='records')

enviar_emails(destinatarios)
