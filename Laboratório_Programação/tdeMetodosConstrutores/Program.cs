/*
Exercicio 01 e 02
    01 - Crie uma classe chamada Produto com as propriedades Nome e Preco. Implemente um construtor padrão que inicializa Nome como "Desconhecido" e Preco como 0.0, e um construtor parametrizado que aceita valores para Nome e Preco.

    02 - Na classe Produto do exercício anterior, crie um método ExibirInfo que exibe as informações do produto. Em seguida, sobrecarregue este método para que ele aceite um parâmetro booleano exibirPreco. Se exibirPreco for verdadeiro, o método deve exibir também o preço do produto.
*/
// Produto produto = new Produto();
// Produto produto2 = new Produto("bolacha", 1.99);

// System.Console.WriteLine(produto.Nome);
// System.Console.WriteLine(produto2.Nome);


/*
Exercicio 03
    Crie uma classe chamada Calculadora com métodos sobrecarregados para somar dois, três e quatro números inteiros.
*/
// Calculadora calculadora = new Calculadora();
// calculadora.Soma(1,2,3,4);
// calculadora.Soma();


/*
Exercicio 04
    Crie uma classe Aluno com propriedades Nome e Idade. Implemente um construtor padrão que inicializa Nome como "Não Informado" e Idade como 0. Crie também um construtor parametrizado que aceita Nome e Idade como argumentos.
*/
// Aluno aluno1 = new Aluno("luan", 33);
// System.Console.WriteLine(aluno1.nome);
// System.Console.WriteLine(aluno1.idade);


/*
Exercicio 05
    Crie uma classe Funcionario com as propriedades Nome, Cargo e Salario. Implemente um construtor padrão que inicializa Nome como "Desconhecido", Cargo como "Não Informado" e Salario como 0.0. Crie também um construtor parametrizado que aceita Nome, Cargo e Salario.
*/
// Funcionario funcionario1 = new Funcionario();
// Funcionario funcionario2 = new Funcionario("Luan", "vendedor", 3000);


/*
Exercicio 06
    Crie uma classe Retangulo com propriedades Altura e Largura. Implemente métodos sobrecarregados CalcularArea para calcular a área do retângulo. O método deve funcionar tanto com a altura e largura da instância quanto com valores passados como parâmetros.
*/
// Retangulo retangulo1 = new Retangulo(20.5, 40.5);
// var resp1 = retangulo1.CalcularArea();
// var resp2 = retangulo1.CalcularArea(10,30);
// System.Console.WriteLine(resp1);
// System.Console.WriteLine(resp2);


/*
Exercicio 07
    Crie uma classe Livro com propriedades Titulo, Autor e Ano. Implemente um construtor padrão e um construtor parametrizado que aceita Titulo, Autor e Ano. Crie um método ExibirInfo para exibir as informações do livro.
*/
// Livro livro1 = new Livro("Roberto", "As armas da persuasão", 1964);
// livro1.ExibirInfo();


/*
Exercicio 08
    Crie uma classe ContaBancaria com propriedades NumeroConta, Titular e Saldo. Implemente um construtor padrão que inicializa NumeroConta e Titular como "Desconhecido" e Saldo como 0.0. Crie também um construtor parametrizado que aceita NumeroConta, Titular e Saldo.
*/
// ContaBancaria contaBancaria1 = new ContaBancaria();
// ContaBancaria contaBancaria2 = new ContaBancaria("Desconhecido", "Desconhecido", 0.0);


/*
Exercicio 09
    Crie uma classe Veiculo com as propriedades Marca, Modelo e Ano. Implemente um construtor padrão que inicializa Marca, Modelo como "Desconhecido" e Ano como 0. Crie também um construtor parametrizado que aceita Marca, Modelo e Ano.
*/
// Veiculo veiculo1 = new Veiculo();
// Veiculo veiculo 2 = new Veiculo("Desconhecido", "Desconhecido", 0);


/*
Exercicio 10
    Crie uma classe Conversor com métodos sobrecarregados para converter diferentes tipos de dados. Implemente métodos para converter int para double, double para int, string para int, e string para double
*/
Conversor conv = new Conversor();
Console.WriteLine(conv.Converter(10));         
Console.WriteLine(conv.Converter(10.5));        
Console.WriteLine(conv.Converter("10"));        
Console.WriteLine(conv.Converte("10.5"));    