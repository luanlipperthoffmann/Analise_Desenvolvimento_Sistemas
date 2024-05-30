public class Veiculo
{
    string Marca;
    string Modelo;
    int Ano;

    public Veiculo()
    {
        Marca = "Desconhecido";
        Modelo = "Desconhecido";
        Ano = 0;
    }

    public Veiculo( string Marca, string Modelo, int Ano)
    {
        this.Marca = Marca;
        this.Modelo = Modelo;
        this.Ano = Ano;
    }
}