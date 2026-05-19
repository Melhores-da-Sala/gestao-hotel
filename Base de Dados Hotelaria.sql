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
-- --------------------------------------------------------------------------
-- ──────────────────────────────────────────
-- INSERINDO HÓSPEDES
-- ──────────────────────────────────────────
INSERT INTO hospedes (nome, email, telefone, cpf) VALUES
('Carlos Silva', 'carlos.silva@email.com', '(11) 99999-1111', '111.111.111-11'),
('Ana Oliveira', 'ana.oliveira@email.com', '(11) 98888-2222', '222.222.222-22'),
('Marcos Santos', 'marcos.santos@email.com', '(21) 97777-3333', '333.333.333-33'),
('Beatriz Costa', 'beatriz.costa@email.com', '(31) 96666-4444', '444.444.444-44'),
('João Pedro Almeida', 'joao.almeida@email.com', '(41) 95555-5555', '555.555.555-55');

-- ──────────────────────────────────────────
-- INSERINDO QUARTOS
-- ──────────────────────────────────────────
INSERT INTO quartos (numero, tipo, valor_diaria, status) VALUES
('101', 'Standard', 150.00, 'Ocupado'),
('102', 'Standard', 150.00, 'Disponível'),
('201', 'Luxo', 280.00, 'Ocupado'),
('202', 'Luxo', 280.00, 'Manutenção'),
('301', 'Presidencial', 850.00, 'Disponível');

-- ──────────────────────────────────────────
-- INSERINDO RESERVAS
-- ──────────────────────────────────────────
-- Nota: As datas estão configuradas para o momento atual para que apareçam na sua query de "reservas ativas"
INSERT INTO reservas (hospede_id, quarto_id, data_entrada, data_saida) VALUES
-- Reserva ativa (Hóspede 1 no Quarto 101)
(1, 1, DATE_SUB(CURDATE(), INTERVAL 2 DAY), DATE_ADD(CURDATE(), INTERVAL 3 DAY)),

-- Reserva ativa (Hóspede 2 no Quarto 201)
(2, 3, CURDATE(), DATE_ADD(CURDATE(), INTERVAL 5 DAY)),

-- Reserva futura (Hóspede 4 no Quarto 301)
(4, 5, DATE_ADD(CURDATE(), INTERVAL 15 DAY), DATE_ADD(CURDATE(), INTERVAL 20 DAY)),

-- Reserva passada (Hóspede 3 no Quarto 102 - NÃO aparecerá na tela de ativas)
(3, 2, DATE_SUB(CURDATE(), INTERVAL 10 DAY), DATE_SUB(CURDATE(), INTERVAL 5 DAY));

SELECT * FROM hospedes;
SELECT * FROM quartos;
SELECT * FROM reservas;