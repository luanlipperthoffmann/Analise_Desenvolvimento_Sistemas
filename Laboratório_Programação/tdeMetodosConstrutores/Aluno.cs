public class Aluno
{
    public string nome;
    public int idade;

    public Aluno() //contrutor padrão
    {
        nome = "Não Informado";
        idade = 0;
    }

    public Aluno(string nome, int idade)  //Contrutor parametrizado, recebe os  parametros dentro chave
    {
        this.nome = nome;
        this.idade = idade;
    }

}