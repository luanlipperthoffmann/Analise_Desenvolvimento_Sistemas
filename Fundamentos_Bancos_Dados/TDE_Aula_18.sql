/*
    Modelo Lógico:

    Professores (Id int Not Null pk, Nome varchar(100), Especializacao varchar(50), Idade (int));
    Disciplinas (Id_Disc int Not Null pk, Disciplina varchar(50), Carga_Horaria (int));
    Software (Id int Not Null pk, Nome varchar(100), Tipo varchar(50));
    Leciona (Id_Leciona int Not Null pk, Id_Professores int Not Null fk, Id_Disc int Not Null fk references Professores(Id), Disciplinas(Id_Disc));
    Utiliza (Id_Utiliza int not Null pk, Id_Disc int Not Null fk, Id_Softwares int Not Null fk references Disciplinas(Id_Disc), Software (Id));
*/

CREATE TABLE Professores
(
    Id int NOT NULL PRIMARY KEY,
    Nome varchar(100),
    Especializacao varchar(50),
    Idade int
);

CREATE TABLE Disciplinas
(
    Id_Disc int NOT NULL PRIMARY KEY,
    Disciplina varchar(50),
    Carga_Horaria int,
);

CREATE TABLE Leciona
(
    Id NOT NULL PRIMARY kEY,

);
