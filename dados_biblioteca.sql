drop database biblioteca;

create database biblioteca;
use biblioteca;

create table livros (
	id int primary key auto_increment,
	nome varchar (100)
);

ALTER TABLE livros ADD COLUMN quantidade_paginas int;

ALTER TABLE livros ADD COLUMN autor varchar(100);
ALTER TABLE livros ADD COLUMN preco double;
ALTER TABLE livros ADD COLUMN isbn varchar(30);
ALTER TABLE livros ADD COLUMN descricao text;



select * from livros;