public class Pessoa
{
    //atributos
    public string nome;
    public int idade;
    public string sexo;

    //metodos
    public void Comer()
    {
        System.Console.WriteLine("Pessoa comendo");
    }

    public void Caminhar(int passos)
    {
        System.Console.WriteLine($"Dando {passos} passos.");
    }

    public void Trabalhar()
    {
        string trabalho = "Pessoa Trabalhando";
        return trabalho;
    }
}