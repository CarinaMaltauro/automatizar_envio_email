<h1 align="center"> Envio de e-mails em massa considerando as características dos destinatários </h1>

<p align="center">
Carina Maltauro <br/>
</p>

## Projeto

Este projeto visa automatizar um grande número de envios de e-mails, baseando-se em uma comunicação eficiente e rápida com parceiros/clientes. Considerou-se durante a construção do projeto a possibilidade de personalizar destinatários e mensagens. Uma empresa pode ter a necessidade de enviar e-mails padronizados considerando características semelhantes entre os destinatários, exemplificando, enviar e-mails para parceiros de determinado grupo ou para clientes de determinada região. A empresa ainda pode ter a necessidade de personalizar a mensagem, como inserir o nome do cliente ou o número de um pedido. O projeto fornece códigos que acessam os dados dos destinatários tanto de uma simples planilha de Excel como de um banco de dados (MySQL, Oracle, etc).

## Instruções

- Realize as instalações e verifique as recomendações em requirements.txt.
- Para personalizar apenas características dos destinatários(dados em uma planilha de Excel), utilize main.py, chave_sendgrid.py e o arquivo de Excel.
- Para personalizar características dos destinatários (dados em uma planilha de Excel) e mensagens, utilize main_personalized.py, chave_sendgrid.py e o arquivo de Excel.
- Para personalizar características dos destinatários (dados em banco de dados MySQL) e mensagens, utilize main_personalized.py, chave_sendrig.py, senha_mysql.py, connection_mysql.py, arquivo sql.

 
