<h1 align="center"> Envio de e-mails em massa considerando as características dos destinatários  </h1>

<p align="center">Carina R. P. M Dias</p>


Este projeto tem como objetivo **automatizar o envio em massa de e-mails personalizados**, facilitando uma comunicação eficiente e segmentada com **clientes e parceiros**. Ele permite que empresas enviem e-mails padronizados com variações de conteúdo, com base em características compartilhadas entre os destinatários — como grupo, região, tipo de relacionamento entre outros.

Durante o desenvolvimento, foram incluídas funcionalidades para:

* Personalizar o **conteúdo das mensagens** (ex: nome do cliente, número do pedido)
* Segmentar o envio por **grupo, localidade ou categoria**
* Utilizar **dados armazenados em planilhas Excel ou bancos de dados** (MySQL, Oracle, etc.)

---

## ⚙️ Instruções de Uso

### 1. Configuração inicial

1. Crie uma conta gratuita no [SendGrid (Twilio)](https://sendgrid.com/)
2. Gere uma chave de API em: **Email API > Integration Guide > API Key**
3. Salve essa chave em um arquivo chamado `chave_sendgrid.py`, no seguinte formato:

```python
SENDGRID_API_KEY = "sua_chave_aqui"
```

---

### 2. Modos de uso

#### A) Personalização com dados de Excel (somente destinatários)

Use os arquivos:

* `main.py`
* `chave_sendgrid.py`
* Planilha `.xlsx` com os dados dos destinatários

#### B) Personalização com dados de Excel e mensagens

Use os arquivos:

* `main_personalized.py`
* `chave_sendgrid.py`
* Planilha `.xlsx` com dados e conteúdo dinâmico das mensagens

#### C) Personalização com banco de dados (MySQL) e mensagens

Use os arquivos:

* `main_personalized_mysql.py`
* `chave_sendgrid.py`
* `senha_mysql.py`
* `connection_mysql.py`
* Script `.sql` contendo a estrutura/tabela com os dados dos destinatários e mensagens

---

## 🛠️ Tecnologias utilizadas

* Python 3.x
* [SendGrid API](https://sendgrid.com/docs/api-reference/)
* `pandas` (leitura e manipulação de Excel)
* `mysql-connector-python` (conexão com MySQL)
* Modularização segura com arquivos separados para credenciais

---

## 💡 Aplicações Práticas

* Envio de e-mails promocionais personalizados
* Notificações segmentadas por localidade
* Comunicação com grupos de parceiros
* Follow-ups automatizados com informações individualizadas

---

## 🚀 Execução rápida

1. Instale as dependências:

```bash
pip install pandas sendgrid mysql-connector-python openpyxl
```

2. Execute o script desejado, por exemplo:

```bash
python main_personalized.py
```


 
