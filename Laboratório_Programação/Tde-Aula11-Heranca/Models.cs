//Exercício 1: Classe Base e Classe Derivada
using System.Security.Cryptography.X509Certificates;

public class Veiculo
{
    public string? Marca;
    public int Ano;
}

public class Carro : Veiculo
{
    public string? Modelo;

    public void ExibirDetalhes(string Marca, int Ano, string Modelo)
    {
        System.Console.WriteLine($"Marca: { Marca}, Ano: {Ano}, Modelo: {Modelo}");
    }
}


//Exercício 2: Sobrescrita de Método
public class Animal
{
    public virtual void EmitirSom()
    {
        System.Console.WriteLine("O animal emite som");
    }
}

public class Gato : Animal
{
    public override void EmitirSom()
    {
        System.Console.WriteLine("O gato mia!");
    }
}


//Exercício 3: Modificadores de Acesso
public class Pessoa
{
    private string? nome;
    public string? Nome;

    public void ExibirNome()
    {
        Nome = "Luan";
        System.Console.WriteLine($"Nome: {Nome}");
    }
}

public class Funcionario : Pessoa
{
    protected double Salario;

    public void InformaSalario()
    {   
        System.Console.WriteLine("Informe o salario: ");
        Salario = Convert.ToDouble(Console.ReadLine());
    }
}


//Exercício 4: Construtores em Classes Derivadas
public class Produto
{
    public string Nome;
    public decimal Preco;

    public Produto()
    {
        Nome = "Notbook";
        Preco = 3000;
    }
}

public class Eletronico : Produto
{
    public string Garantia;

    public Eletronico()
    {
        Garantia = "1 Ano";
        System.Console.WriteLine($"Nome: {Nome}, Preço: {Preco}, Garantia: {Garantia}");
    }
}


//Exercício 5: Polimorfismo com Herança
public class Forma
{
    public virtual double CalcularArea()
    {
        return 0;
    }
}

public class Quadrado : Forma
{   
    public double lado;

    public Quadrado(double lado)
    {
        this.lado = lado;
    }
    public override double CalcularArea()
    {
        return lado*lado;
    }
}

public class Circulo : Forma
{   
    public double raio;

    public Circulo(double raio)
    {
        this.raio = raio;
    }
    public override double CalcularArea()
    {
        return raio*3.14;
    }
}


//Exercício 6: Encapsulamento com Propriedades
public class ContaBancaria
{
    public string NumeroConta;
    public string Titular;
    private double Saldo;

    public ContaBancaria(string NumeroConta, string Titular, double Saldo)
    {
        this.NumeroConta = NumeroConta;
        this.Titular = Titular;
        this.Saldo = Saldo;
    }
}


//Exercício 7: Herança e Sobrescrita
public class Funcionario07
{
    public string? Nome;
    public int Bonus;

    public virtual int CalcularBonus()
    {
        return 0;
    }
}

public class Gerente : Funcionario07
{
    public int MaiorBonus;

    public Gerente(int MaiorBonus)
    {
        this.MaiorBonus = MaiorBonus;
    }
}


//Exercício 8: Usando Protected
public class Banco
{
    protected string? Nome;
}

public class Agencia : Banco
{
    public Agencia(string Nome)
    {
        this.Nome = Nome;
    }
    public void ExibiNome()
    {
        System.Console.WriteLine($"Nome do Banco: {Nome}");
    }
}


//Exercício 9: Herança Múltipla com Interfaces
public interface Imprimivel
{
    void Imprimir();
}

public class Documento : Imprimivel
{
    public virtual void Imprimir()
    {
        System.Console.WriteLine("Documento sendo impresso");
    }
}

public class Relatorio : Documento
{
    public override void Imprimir()
    {
        System.Console.WriteLine("Relatorio sendo impresso");
    }
}


//Exercício 10: Combinando Herança e Polimorfismo
public class Funcionario10
{
    public virtual void Trabalhar()
    {
        return;
    }
}

public class Desenvolvedor : Funcionario10
{
    public override void Trabalhar()
    {
        System.Console.WriteLine("Desenvolvedor toma café e passa raiva!");
    }
}

public class Designer : Funcionario10
{
    public override void Trabalhar()
    {
        System.Console.WriteLine("Designer toma toddy e muda cor de botão!");
    }
}