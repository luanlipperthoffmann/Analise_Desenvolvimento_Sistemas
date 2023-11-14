    --Comentário de 1 linha

/*comentario 
    de
    mais
    de 
    uma
    linha
*/

/*
    Modelo lógico para exemplo

    Clientes(Id int Not Null pk, Nome char(100));
    Enderecos(Id int Not Null pk, Rua varchar(100), Numero int, Bairro varchar(50), Cidade varchar(50), Estado char(2), Id_Clientes int Not Null references Clientes(Id));
*/

CREATE TABLE Clientes
(
    Id int Not Null Primary Key,
    Nome char(100)
);

CREATE TABLE Enderecos
(
    Id int Not Null Primary Key,
    Rua varchar(100),
    Numero int,
    Bairro varchar(50),
    Cidade varchar(50),
    Estado char(2),
    Id_Cliente int Not Null,
        Constraint Clientes_tem_Enderecos
            FOREIGN Key (Id_Cliente) references Clientes(Id)
);

ALTER	TABLE Clientes
	add Telefone varchar(50)

ALTER  TABLE  Enderecos
    DROP COLUMN E-mail varchar (50) 


ALTER TABLE Enderecos
	DROP COLUMN Email

ALTER TABLE Enderecos
	CHANGE COLUMN UF Uf char (2)

ALTER TABLE Enderecos
DROP CONSTRAINT Clientes_tem_Enderecos

ALTER TABLE Enderecos
add CONSTRAINT Nova_fk FOREIGN KEY (id_cliente) REFERENCES Clientes(id)



========
--Inserção em tabela


CREATE TABLE Produtos
(
    Codigo int Not Null Primary Key,
    Descricao varchar (150),
    Data_Cadastro Date,
    Valor_Unitario float,
    Cod_Cat int Not Null,
    	Constraint Categoria_tem_Produtos
        	Foreign Key (Cod_Cat) references Categorias(Codigo)
);


CREATE TABLE Produtos
(
    Codigo int Not Null Primary Key,
    Descricao varchar (150),
    Data_Cadastro Date,
    Valor_Unitario float,
    Cod_Cat int Not Null,
    	Constraint Categoria_tem_Produtos
        	Foreign Key (Cod_Cat) references Categorias(Codigo)
);


CREATE TABLE Fornecedores
(
    Codigo int Not Null Primary Key,
    Nome varchar(100)
);


CREATE TABLE Pedidos
(
    Quantidade int Not Null Primary Key,
    Valor_Unitario float,
    Data Date,
    Cod_Fornec int Not Null,
    Prod_Cod int Not Null,
    Constraint Fornecedores_Pede_Produtos
        Foreign Key (Cod_Fornec) references Fornecedores(Codigo),
    Constraint Produtos_tem_Fornecedores
        Foreign Key (Prod_Cod)references Produtos(Codigo)
);