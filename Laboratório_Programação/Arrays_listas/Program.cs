//Definição: Um array é uma coleção de elementos de um mesmo tipo, armazenados em posições contíguas de memória.

//ARRAYS:
    //usado em grandes volumes de tarefas;

int [] notas = new int[5];
notas[0] = 90;
notas[1] = 85;
notas[2] = 88;
notas[3] = 92;
notas[4] = 95;

for (int i =0; i < notas.Length; i++)
{
    System.Console.WriteLine($"O aluno: {i+1} tem nota: {notas[i]}");
}

//LIST:
//Definição: Uma List é uma coleção dinâmica de elementos de um mesmo tipo. Ao contrário dos arrays, Lists podem crescer e diminuir de tamanho conforme necessário.
//lista vazia de strings
List<string> tarefas = new List<string>();

//adicionar tarefas
tarefas.Add("Estudar c#");
tarefas.Add("Ler um livro de programação");
tarefas.Add("Escrever um artigo");

//remover tarefas
tarefas.Remove("Escrever um artigo");
tarefas.RemoveAt(0);  //remove a tarefa numa posição especifica da lista;

foreach(var tarefa in tarefas)
{
    System.Console.WriteLine(tarefa);
}