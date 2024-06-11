using System.Security.Cryptography.X509Certificates;

public class Autor
{
    public string Nome;
    public string Nacionalidade;
    public Autor()
    {
        Nome = "Desconhecido";
        Nacionalidade = "Indeterminado";
    }

    public void MostrarInfo()
    {
        System.Console.WriteLine($"\nAUTOR: \nNome: {Nome}, Nacionalidade: {Nacionalidade}");
    }
}

public class Livro
{
    public string? Titulo;
    public string? Autor;
    public double Preco;

    public Livro(string Titulo, string Autor)
    {
        this.Titulo = Titulo;
        this.Autor = Autor;
    }

    public Livro(string Titulo, string Autor, double Preco){
        this.Titulo = Titulo;
        this.Autor = Autor;
        this.Preco = Preco;
    }

    public void MostrarInfo()
    {
        System.Console.WriteLine($"\nLIVRO: \nTitulo: {Titulo}, Autor: {Autor}, Preço: {Preco}");
    }

    
    public void AplicarDesconto(double Desconto) {
        System.Console.WriteLine($"O Valor do livro {Titulo} com  o desconto de {Desconto}% é de: {Preco -(Preco*Desconto/100)}");
    }

    public void AplicarDesconto(int Desconto){
        System.Console.WriteLine($"O valor do livro {Titulo} com o desconto de {Desconto} Reais é de: {Preco-Desconto}");
    }
}