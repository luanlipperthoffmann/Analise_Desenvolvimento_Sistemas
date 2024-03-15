//1.Crie uma variável chamada idade e atribua a ela o valor 35 e exiba o seu valor.
byte idade = 33;
Console.WriteLine(idade);

//2.Crie uma variável chamada nome e atribua o valor "Maria" e exiba o seu valor.
string nome = "Maria";
Console.WriteLine(nome);

//3.Crie uma variável chamada altura e atribua a ela o valor 3.45.
double altura = 3.45;
Console.WriteLine(altura + " Mts");

//4.Crie uma constante chamada ano e atribua a ela o valor 12 e exiba o seu valor
uint ano = 12;
Console.WriteLine(ano);

//5.Declare uma variável nota do tipo double como sendo do tipo Nullable type e atribua o valor 7.80 e exiba o seu valor
double? nota = null;
nota = 7.80;
if (nota.HasValue){
    Console.WriteLine(nota);
}else{
    Console.WriteLine("Nota não possui um valor!");
}

//6.Quais as diferenças entre os tipos por valor e os tipos por referência ?
/*
    TIPOS POR VALOR:
    Nos tipos por valor as variáveis cada variável tem a própria copia dos dados e as operções de uma variável não pode afetar a outra.

    TIPOS POR REFERENCIA:
    Já nos tipos de refÊncia, duas variáveis podem fazer referência ao mesmo objeto, o useja, a operação realizada numa varável pode afetar o objeto referenciado em outra variável
*/

//7.O que é um nullable type e qual a sua utilidade ?
/*
    É um tipo que indica um atributo de tipo inteiro que aceita valor nulo, ele é util quando temos um valor do tipo inteiro que poderia ser considerado invalido, logo um campo extra é usado para marcar quando é nulo
*/

//8.O que é Camel Case ? Dê um exemplo de sua aplicação.
/*
    Came case é um estilo de nomenclatura usado na programação para podemos conbinar mais de um nome numa variavel, parâmetro. Neste tipo de nomenclatura usamos a primeira letra do nome em minúscula e as seguintes palavras concatenadas terão a primeira letra em maiuscula. e geramente é usado para nomear variavéis e propriedades,  ex.: idadeDaPessoa, numeroUm, areaRetangulo.
*/

//9.O que é Pascal Case ? Dê um exemplo de sua aplicação
/*
    O pascal case é um outro tipo de nomenclatura muito utilizados também como fomra de organização de um codigo garantido assim a legibilidade do mesmo. O Pascal Case é geralmente utilizado para nomear classes, interfaces, enums e métodos públicos, neste tipo de nomencaltura utilizamos como forma de escrita a primeira detra de cada nome em letra maiuscula e as demais em letra minuscula. por ex.: CarroSedan, HomensCarecas, CarroBranco
*/

//10.Declare duas variáveis x e y como sendo do tipo int e atribua a ela os valores 77 e 66 e a seguir imprima o valor da soma de x com y. (Use o operador aritmético + para realizar a operação de soma). 
int x = 77;
int y = 66;
Console.WriteLine(x+y);

//11.Quais os valores padrões dos tipos de dados bool, char, int, double, float, decimal e string.
/*
    bool => false
    char => \0 ou U+0000
    int => todo tipo integral o valor padrão é 0
    double => 0, tem uso em calculos ciêntificos
    float => 0, tem uso em calculos aritimeticos
    decimal => 0, tem uso em aplicativos financeiros, como moeda e tipos de juros
    string => null
*/
