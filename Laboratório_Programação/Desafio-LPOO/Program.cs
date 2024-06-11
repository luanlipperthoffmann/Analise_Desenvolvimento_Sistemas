/*
Descrição do Exercício:
Crie uma aplicação simples para gerenciar um único livro e autor. A aplicação deve permitir a criação de objetos representando livros e autores, e deve demonstrar o uso de classes, atributos, métodos, construtores, sobrecarga de métodos, abstração e polimorfismo.
Requisitos:

Classe Autor:
Atributos: Nome (string), Nacionalidade (string).
Construtor para inicializar Nome e Nacionalidade.
Método MostrarInfo para exibir as informações do autor.

Classe Livro:
Atributos: Titulo (string), Autor (Autor), Preco (double).
Construtores:
Um construtor que inicializa Titulo e Autor.
Outro construtor que inicializa Titulo, Autor e Preco.
Método MostrarInfo para exibir as informações do livro.

Método sobrecarregado AplicarDesconto:
    Um método que aceita um double representando a porcentagem de desconto e aplica ao preço do livro.
    Outro método que aceita um int representando um valor fixo de desconto e aplica ao preço do livro.

Polimorfismo:
Demonstrar o polimorfismo utilizando o método AplicarDesconto na classe Livro.

Abstração:
Utilize a abstração ao criar classes Livro e Autor, escondendo os detalhes internos e expondo apenas as funcionalidades essenciais.
*/
Autor autor = new Autor();
autor.MostrarInfo();

Livro livro = new Livro("Senhor dos Anéis", "J.R.R. Tolkien", 150);
livro.MostrarInfo();
livro.AplicarDesconto(15.2);
livro.AplicarDesconto(10);
