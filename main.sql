CREATE DATABASE locadora;
use locadora;

CREATE TABLE IF NOT EXISTS 	filme(
	id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    genero VARCHAR(255) NOT NULL,
    ano INT NOT NULL,
    preco FLOAT NOT NULL
);

CREATE TABLE IF NOT EXISTS cliente(
	id INT AUTO_INCREMENT PRIMARY KEY,
	nome VARCHAR(255) NOT NULL,
	idade INT NOT NULL,
	cep varchar(9)
);

CREATE TABLE aluguel(
	id INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT not null,
    id_filme INT not null,
    
    FOREIGN KEY (id_cliente) REFERENCES cliente(id),
    FOREIGN KEY (id_filme) REFERENCES filme(id)

);
