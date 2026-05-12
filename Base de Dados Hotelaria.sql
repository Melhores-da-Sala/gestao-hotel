CREATE DATABASE hotelaria;
-- ----------------------------------------------------------------
USE hotelaria;
-- ----------------------------------------------------------------
CREATE TABLE hospedes (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR (100) NOT NULL,
    email VARCHAR (100) NULL,
    telefone VARCHAR (20) NULL,
    cpf VARCHAR (14) UNIQUE
);

CREATE TABLE quartos (
	id INT PRIMARY KEY AUTO_INCREMENT,
    numero VARCHAR (10) NOT NULL,
    tipo VARCHAR (50) NOT NULL,
    valor_diaria DECIMAL (10,2) NOT NULL,
    status VARCHAR (20) NOT NULL
);

CREATE TABLE reservas (
	id INT PRIMARY KEY AUTO_INCREMENT,
    hospede_id INT NOT NULL,
    quarto_id INT NOT NULL,
    data_entrada DATE NOT NULL,
    data_saida  DATE NOT NULL,
    FOREIGN KEY (hospede_id) REFERENCES hospedes(id),
    FOREIGN KEY (quarto_id) REFERENCES quartos(id)
);