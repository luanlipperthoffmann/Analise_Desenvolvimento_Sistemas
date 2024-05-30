public class Produto
{
    public string Nome;
    public double Preco;

    public Produto()      //isso é um Construtor
    {
        Nome = "Não Informado";
        Preco = 0.0;
    }

    public Produto(string nome, double preco) //sobrecarga de metodos
    {
        Nome = nome;
        Preco = preco;
    }
}