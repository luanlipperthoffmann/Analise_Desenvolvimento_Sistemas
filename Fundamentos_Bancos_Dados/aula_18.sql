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