public class Livro{
    string autor;
    string titulo;
    int ano;
    public Livro(){
        autor = "nenhum";
        titulo = "nenhum";
        ano = 0000;
    }
    public Livro(string autor, string titulo, int ano){
        this.autor = autor;
        this.titulo = titulo;
        this.ano = ano;
    }

    public void ExibirInfo(){
        System.Console.WriteLine($"titulo:{titulo}], autor:{autor}, ano:{ano}");
    }
}