-- Cria o banco de dados Locadora
CREATE DATABASE IF NOT EXISTS Locadora;

-- Cria a tabela filmes se ainda não existir
CREATE TABLE IF NOT EXISTS filmes (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    sinopse TEXT,
    data_lancamento DATE
);

-- Insere os filmes da saga Star Wars na tabela filmes
INSERT INTO filmes(titulo, diretor, ano, genero) 
VALUES 
    ('Star Wars: Episódio IV - Uma Nova Esperança', 'George Lucas', 1977, 'Aventura, Fantasia'),
    ('Star Wars: Episódio V - O Império Contra-Ataca', 'Irvin Kershner', 1980, 'Aventura, Fantasia'),
    ('Star Wars: Episódio VI - O Retorno de Jedi', 'Richard Marquand', 1983, 'Aventura, Fantasia'),
    ('Star Wars: Episódio I - A Ameaça Fantasma', 'George Lucas', 1999, 'Aventura, Fantasia'),
    ('Star Wars: Episódio II - Ataque dos Clones', 'George Lucas', 2002, 'Aventura, Fantasia'),
    ('Star Wars: Episódio III - A Vingança dos Sith', 'George Lucas', 2005, 'Aventura, Fantasia'),
    ('Star Wars: O Despertar da Força', 'J.J. Abrams', 2015, 'Aventura, Fantasia'),
    ('Star Wars: Os Últimos Jedi', 'Rian Johnson', 2017, 'Aventura, Fantasia'),
    ('Star Wars: A Ascensão Skywalker', 'J.J. Abrams', 2019, 'Aventura, Fantasia');
