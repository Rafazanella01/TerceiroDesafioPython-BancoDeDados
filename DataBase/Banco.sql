-- Cria o banco de dados Locadora
CREATE DATABASE IF NOT EXISTS Locadora;

--Cria a tabela filmes se ainda não existir
CREATE TABLE IF NOT EXISTS filmes (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    sinopse TEXT,
    data_lancamento DATE,
    locado BOOLEAN DEFAULT FALSE
);