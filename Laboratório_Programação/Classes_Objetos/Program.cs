//OBJETO é uma instancia de uma classe, criado pelo operador new, possui caracteristica proprias.
//CLASSE é um modelo, hm planejamento, tal como a maquete de uma casa.
int x =100;

Pessoa p1 = new Pessoa();
p1.nome = "Maria";
p1.idade = 23;
p1.sexo = "feminino";

System.Console.WriteLine($"{p1.nome} {p1.idade} {p1.sexo}");

Pessoa p2 =new Pessoa();
p2.nome = "João";
p2.idade = 30;
p2.sexo = "masculino";

System.Console.WriteLine($"{p2.nome} {p2.idade} {p2.sexo}");

class Pessoa  //estrutura de um objeto
{
    public string nome;
    public int idade;
    public string sexo;
}