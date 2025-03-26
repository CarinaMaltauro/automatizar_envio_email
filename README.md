<h1 align="center"> Envio de e-mails em massa considerando as características dos destinatários  <img src="https://cdn-icons-png.freepik.com/256/16257/16257037.png?ga=GA1.1.763163565.1742925562&semt=ais_hybrid" width="25" heigth="25"></h1>

<p align="center">Carina R. P. M Dias</p>

## Projeto

O projeto tem como objetivo automatizar o envio de um grande número de e-mails, tendo por base uma comunicação eficiente e rápida com parceiros e clientes. Durante a sua construção, foi considerada a possibilidade de personalizar destinatários e mensagens. Uma empresa pode precisar enviar e-mails padronizados com base em características semelhantes entre os destinatários. Por exemplo, enviar e-mails para parceiros de um grupo ou para clientes de uma região. Além disso, a empresa ainda pode ter a necessidade de personalizar o conteúdo da mensagem, como inserir o nome do cliente ou o número de um pedido. O projeto inclui códigos que permitem acessar os dados dos destinatários, tanto a partir de uma simples planilha de Excel quanto de um banco de dados (MySQL, Oracle, etc).

## Instruções

- Leia requirements.txt.
- Crie uma conta no Twilio SendGrid, faça a verificação de e-mail e configure em 'API de e-mail' uma chave_sendgrid.
- Para personalizar apenas características dos destinatários (dados em uma planilha de Excel), utilize main.py, chave_sendgrid.py e o arquivo de Excel.
- Para personalizar características dos destinatários (dados em uma planilha de Excel) e mensagens, utilize main_personalized.py, chave_sendgrid.py e o arquivo de Excel.
- Para personalizar características dos destinatários (dados em banco de dados MySQL) e mensagens, utilize main_personalized_mysql.py, chave_sendrig.py, senha_mysql.py, connection_mysql.py, arquivo sql.

 
