# Criar banco de dados
CREATE DATABASE IF NOT EXISTS bank_test;

# Indicar banco de dados
USE banco_teste;

# Criar tabelas
CREATE TABLE users (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    email VARCHAR(50) UNIQUE,
    regiao VARCHAR(20),
    ativo BOOLEAN DEFAULT TRUE
);

CREATE TABLE pedidos (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_user INT,
    num_pedido VARCHAR(30),
    cod_rastreio VARCHAR(30),
    valor DECIMAL(10,2),
    vencimento DATETIME,
    FOREIGN KEY (id_user) REFERENCES users(id_user)
);

# Inserir dados
INSERT INTO users (nome, email, regiao)
VALUES ('Maltauro Carin', 'primeiro_email_teste@gmail.com', 'Norte'),
('Catarina Dias', 'segundo_email_teste@gmail.com', 'Sul' );

INSERT INTO pedidos (id_user, num_pedido, cod_rastreio, valor, vencimento)
VALUES (1, '268469#j', '248870fo', 1234.89, '2025-02-27'),
(2, '896541#u', '666677uj', 3456.00, '2025-02-28');

SELECT * FROM users;
SELECT * FROM pedidos;