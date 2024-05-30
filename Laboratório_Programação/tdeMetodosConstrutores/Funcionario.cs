public class Funcionario
{
    string nome;
    string cargo;
    double salario;

    public Funcionario()
    {
        nome = "Desconhecido";
        cargo = "Não Informado";
        salario = 0.0; 
    }

    public Funcionario(string nome, string cargo, double salario)
    {
        this.nome = nome;
        this.cargo = cargo;
        this.salario = salario;
    }
}