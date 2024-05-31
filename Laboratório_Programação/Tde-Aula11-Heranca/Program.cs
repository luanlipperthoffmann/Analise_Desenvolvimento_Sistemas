/*
Exercício 1: Classe Base e Classe Derivada
Crie uma classe base Veiculo com as propriedades Marca e Ano. Crie uma classe derivada Carro que adicione a propriedade Modelo e um método ExibirDetalhes que exibe todas as informações do carro.
*/
System.Console.WriteLine("\nEXERCÍCIO 01:"); //este CW serve só pra diferenciar os  prints por ordem de exercício

Carro carro = new Carro("Citroen", 2011, "C4");
carro.ExibirDetalhes();


/*
Exercício 2: Sobrescrita de Método
Crie uma classe base Animal com um método virtual EmitirSom. Crie uma classe derivada Gato que sobrescreva o método EmitirSom para exibir "O gato mia".
*/
System.Console.WriteLine("\nEXERCÍCIO 02");

Animal animal = new Animal();
animal.EmitirSom();

Gato gato = new Gato();
gato.EmitirSom();


/*
Exercício 3: Modificadores de Acesso
Crie uma classe Pessoa com um campo privado nome e uma propriedade pública Nome. Adicione um método ExibirNome que exibe o nome da pessoa. Crie uma classe derivada Funcionario que adicione um campo protegido salario e um método para definir o salário.
*/
System.Console.WriteLine("\nEXERCÍCIO 03");

var funcionario = new Funcionario();
funcionario.ExibirNome();
funcionario.InformaSalario();

/*
Exercício 4: Construtores em Classes Derivadas
Crie uma classe base Produto com um construtor que aceita nome e preco. Crie uma classe derivada Eletronico que adicione a propriedade Garantia e um construtor que aceite nome, preco e garantia.
*/
System.Console.WriteLine("\nEXERCÍCIO 04");

Produto produto = new Produto();
Eletronico eletronico = new Eletronico();


/*
Exercício 5: Polimorfismo com Herança
Crie uma classe base Forma com um método virtual CalcularArea. Crie classes derivadas Quadrado e Circulo que sobrescrevam o método CalcularArea para calcular a área específica de cada forma.
*/
System.Console.WriteLine("\nEXERCÍCIO 05");

Quadrado quadrado = new Quadrado(5.2);
System.Console.WriteLine(quadrado.CalcularArea());

var circulo = new Circulo(8.4);
System.Console.WriteLine(circulo.CalcularArea());


/*
Exercício 6: Encapsulamento com Propriedades
Crie uma classe ContaBancaria com propriedades NumeroConta, Titular e Saldo. Use modificadores de acesso para garantir que Saldo só possa ser modificado dentro da classe.
*/
System.Console.WriteLine("\nEXERCÍCIO 06");

ContaBancaria contaBancaria = new ContaBancaria("12345-70", "Luan", 10100);
System.Console.WriteLine($"Conta Bancaria: {contaBancaria.NumeroConta}");
System.Console.WriteLine($"Titular: {contaBancaria.Titular}");


/*
Exercício 7: Herança e Sobrescrita
Crie uma classe Funcionario com uma propriedade Nome e um método virtual CalcularBonus. Crie uma classe derivada Gerente que sobrescreva CalcularBonus para retornar um valor maior de bônus.
*/
System.Console.WriteLine("\nEXERCÍCIO 07");

Funcionario07 funcionario07 = new Funcionario07();
System.Console.WriteLine($"O valor do bonus original é de: {funcionario07.Bonus}");
Gerente gerente = new Gerente(10);
System.Console.WriteLine($"O novo valor do Bonus é de: {gerente.MaiorBonus}");


/*
Exercício 8: Usando Protected
Crie uma classe Banco com uma propriedade protegida Nome. Crie uma classe derivada Agencia que tenha um método para definir o nome do banco.
*/
System.Console.WriteLine("\nEXERCÍCIO 08");

Banco banco =new Banco();
Agencia agencia = new Agencia("Bradesco");
agencia.ExibiNome();


/*
Exercício 9: Herança Múltipla com Interfaces
Crie uma interface IImprimivel com um método Imprimir. Crie uma classe Documento que implemente essa interface e uma classe Relatorio que herde de Documento e sobrescreva o método Imprimir.
*/
System.Console.WriteLine("\nEXERCÍCIO 09");

Documento documento = new Documento();
documento.Imprimir();

Relatorio relatorio = new Relatorio();
relatorio.Imprimir();


/*
Exercício 10: Combinando Herança e Polimorfismo
Crie uma classe base Funcionario com um método virtual Trabalhar. Crie classes derivadas Desenvolvedor e Designer que sobrescrevam o método Trabalhar para descrever suas atividades específicas.
*/
System.Console.WriteLine("\nEXERCÍCIO 10");

Desenvolvedor desenvolvedor = new Desenvolvedor();
desenvolvedor.Trabalhar();

Designer designer = new Designer();
designer.Trabalhar();