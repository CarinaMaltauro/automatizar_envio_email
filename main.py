# Enviar mensagens padronizadas de acordo com as característas específicas dos Clientes como Região entre outras

import pandas as pd
from pandasql import sqldf

from sendgrid import SendGridAPIClient 
from sendgrid.helpers.mail import Mail 

from chave_sendgrid import chave_api_sendgrid # chave da api 

# Definir os clientes que receberão os e-mails
def query_table(query_text):
    result = sqldf(query_text, globals())
    return result

# base de dados
df_email_clientes = pd.read_excel('email_clientes.xlsx')
# emails dos clientes da região Sul 
emails = query_table('''SELECT Email FROM df_email_clientes WHERE Region = 'Sul' ''')
lista_emails = emails['Email'].tolist()

# acessar conta no sendgrid
conta_sendgrid = SendGridAPIClient(chave_api_sendgrid)


# Não se coloca anexo em email em massa, geralmente coloca um link que dê acesso ao documento.
# from_email deve ser o email verificado no sendgrid e não necessariamente o email da conta


# compor email
email = Mail(from_email="seu_email_verificado_no_sendgrid@gmail.com", to_emails= lista_emails, 
             subject="Comunicado de Atraso", 
             html_content="<p>Comunicamos ao Senhor(a) um atraso de três dias na entrega</p><p>Agradecemos a compreenssão. Para mais informações entre em contato pelo tel (xx)99999-9999</p>")

# poderia colocar no lugar de html_content, plain_text_content = "Texto aqui"

resposta = conta_sendgrid.send(email)
print(resposta.status_code)


