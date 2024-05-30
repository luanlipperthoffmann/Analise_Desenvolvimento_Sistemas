/*Objeto é uma instancia de uma classe, criado pelo operador new. Os objetos possuem caracteristicas próprias, agrupadas, enquanto uma classe descreve todos os objetos d euma tipo particular

    int x = 100;

    int y = 200;

    Pessoa p1 = new Pessoa();
    p1.nome = "Lucas";
    p1.idade = 31;
    p1.sexo = "Masculino";

    System.Console.WriteLine($"Nome: {p1.nome}, Idade: {p1.idade}, Sexo: {p1.sexo}");

    Pessoa p2 = new Pessoa();
    p2.nome = "Luan"; //Objeto do tipo pessoa
    p2.idade = 15;   // atributo idade
    p2.sexo = "Masculino";

    System.Console.WriteLine($"Nome: {p2.nome}, Idade: {p2.idade}, Sexo: {p2.sexo}");
*/

/*
internal class Program
{
    private static void Main(string[] args)
    {
        Pessoa p1 = new Pessoa();
        int passos = 500;
        p1.nome = "Lucas";
        p1.Comer();
        p1.Caminhar(passos);
        string x = p1.Trabalhar();
        System.Console.WriteLine(x);;
    }
}
*/

/*
Calculadora calculo = new Calculadora(1.5, 2.5);
calculo.Somar(1,2);
calculo.Somar(1,2,3);
calculo.Divisao(1.5, 2.5);
var resultado = calculo.Divisao()
Console.WriteLine(resultado);
var resultado2 = calculo.Divisao();
Console.WriteLine(resultado2);
*/

aluno azul = new Aluno("luan", 33);
aluno dois = new Aluno();