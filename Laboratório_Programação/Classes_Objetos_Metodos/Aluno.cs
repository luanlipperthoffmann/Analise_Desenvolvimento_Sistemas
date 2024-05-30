public class Aluno
{
    string nome;
    int idade;

    public Aluno (string nome, int idade)
    {
        this.nome = nome;
        this.idade = idade;
    }

    public Aluno()
    {
        this.nome = "Não informado!";
        this.idade = 0;
    }
}