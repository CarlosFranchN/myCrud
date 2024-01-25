use locadora;

INSERT into filme(titulo,genero,ano,preco)
values
	("Senhor dos Aneis: A Sociedade do Anel","Fantasia/Aventura",2002, 60),
	("Assassino da Lua das Flores", "Crime/Faroeste", 2023, 55),
    ("Em Ritimo de Fuga","Ação/Thriller", 2017,35);

INSERT into filme(titulo,genero,ano,preco)
values
	("Guardiões da Galaxia Vol.3","Ação/Ficção Cientifica",2023,45),
	("Barbie", "Comédia/Fantasia", 2023,58);

INSERT INTO filme(titulo, genero, ano, preco)
VALUES
	("Saltburn","Thiller/Comédia",2023,56.69),
    ("Midsommar","Terror/Misterio",2019,42.50),
    ("Duna","Ficção cientifica/Aventura",2021,58.60),
    ("Hereditário","Terror/Mistério",2018,46.66),
    ("Super Mario Bros. O filme","Comdia/Aventura",2023,42.55)
    ;


INSERT INTO cliente(nome,idade, cep)
VALUES
	("Carlos", 26, "60125-151"),
    ("Aloy", 20,"60842-220"),
    ("Aragorn",87,"60340-360"),
    ("Baby", 24,"60050-110");
INSERT INTO cliente(nome,idade, cep)
VALUES
	("Lulu", 50,"60422-050");


INSERT INTO aluguel(id_cliente,id_filme)
VALUES
	(1,3),
    (1,5),
    (2,1),
    (2,2),
    (2,8),
    (5,7),
    (5,9),
    (5,10);


UPDATE filme
set titulo = "Nárnia", genero = "Fantasia", ano = 2003
where id = 4;

DELETE FROM filme 
WHERE id=6;

select * from filme;
select titulo,ano,preco 
FROM filme
WHERE ano >= 2015;

select titulo,ano,preco 
from filme
WHERE preco <=55;

SELECT cliente.nome as "cliente", filme.titulo as "Filme" 
FROM ((aluguel
	INNER JOIN cliente ON cliente.id = aluguel.id_cliente)
	INNER JOIN filme on filme.id = aluguel.id_filme);
    
select * from filme;
