CREATE DATABASE IF NOT EXISTS db_filmes;
USE db_filmes;

CREATE TABLE IF NOT EXISTS Filmes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150),
    diretor VARCHAR(100),
    genero VARCHAR(50),
    ano INT,
    duracao INT,
    nota DECIMAL(3,1)
);

INSERT INTO Filmes (titulo, diretor, genero, ano, duracao, nota) VALUES
('Cidade de Deus', 'Fernando Meirelles', 'Drama', 2002, 130, 8.6),
('Central do Brasil', 'Walter Salles', 'Drama', 1998, 113, 8.0),
('Tropa de Elite', 'Jose Padilha', 'Acao', 2007, 115, 8.0);
