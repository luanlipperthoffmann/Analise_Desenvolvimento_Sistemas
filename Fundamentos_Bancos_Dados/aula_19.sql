/*
    =================== DDL ============
    DDL => Define a estrutura das tabelas
        CREATE TABLE => Criação da estrutura do B.D. (tabelas);
        ALTER TABEL => Altera uma estruta das tabelas;
            - ADD COLUNA => adiciona coluna á tabela;
            - REMOVE COLUNA => remove coluna da tablea;
            - ALTER COLUNA => altera coluna da tabela e chaves primaria e estrangeuiras, altera a estrutura da tabela;
            - DROP COLUNA / CHAVE => pode remover colunas e chaves primaria e estrangeuiras;
        DROP TABLE => remove coluna da tabela; 
    * É a carcaça das tabela sem os dados inseridos

    =================== DML ============
    DDL => Defina os dados na tabela
        INSERT => Inserção de dados na tabela, não cria tupla, apenas insere;
        SELECT => 
        UPDATE => Alera os dados da tabela, modifica um dado existente, insere um dado em um campo que está NULL, desde que esse não seja NOT NULL;
    * Manipulação, inserção dos dados na tabela

    =>BETWEEN verifica os itens que estão entre os termos citados
    => LIKE pega somente o itens da palavra restrito
    => % colocado antes ou depois de uma palavra afin de pesquizar tudo que contem a palavra antes ou deppois
    => DISTINC junto com o select para retornar as redundanias de uma palavra buscada
*/