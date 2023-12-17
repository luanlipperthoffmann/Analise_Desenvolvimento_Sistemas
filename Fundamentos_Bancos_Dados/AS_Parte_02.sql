/*Criar as tabelas Produtos e Pedidos (Considerando que as demais tabelas já foram criadas*/
CREATE TABLE Produtos
(
    Codigo int not null Primary Key,
    Descricao varchar(50),
    Data_Cadastro date,
    Valor_Unit float
);

CREATE TABLE Fornecedores
(
    Id int not null Primary Key,
    Nome varchar(30)
);

CREATE TABLE Pedidos
(
    Cod_Ped int not null,
    Total float,
    Data_Ped date,
    Codigo_Produtos int not null,
    Id_Fornecedores int not null,
        Constraint Produtos_tem_Pedidos
            Foreign Key (Codigo_Produtos) REFERENCES Produtos(Codigo),
        Constraint Pedidos_tem_Produtos
            Foreign Key (Id_Fornecedores) REFERENCES Fornecedores (id)
);

/*Altere a coluna “nome‘ da tabela Categorias para “nome_categoria” */
CREATE TABLE Categorias
(
    Codigo int not null,
    Nome varchar(30)
);

ALTER TABLE Categorias
    CHANGE COLUMN Nome Nome_Categorias varchar(30)

/*Consultar os nome e valor unitário do produto que possui Código igual a 300*/
INSERT INTO Produtos (Codigo, Descricao, Data_Cadastro, Valor_Unit)
VALUES (300, 'vassoura', '2023/12/04', 1299)

SELECT Codigo, Descricao, Valor_Unit FROM Produtos

/*Alterar o pedido Cod_Pede = 75. Onde o novo valor para o campo quantidade seja 83.*/
INSERT INTO Pedidos (Cod_Ped, Total, Data_Ped)
VALUES (75, 2599, 2023/12/04)

UPDATE Pedidos
SET Total = 83
WHERE Cod_Ped = 75

/*Listar todos os pedidos realizados no mês de outubro*/
SELECT *FROM Pedidos WHERE Data_Cadastro BETWEEN '2023/10/01' AND '2013/10/31';

/*Ordenar os produtos pela descricao por ordem alfabética*/
SELECT *FROM Produtos ORDER BY Descricao ASC DESC;