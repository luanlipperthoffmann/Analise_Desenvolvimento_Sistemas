/*
    Declare as variáveis nome, idade e nota atribuindo os valores “Paulo”, 17 e 7.5 e exiba a saída no formato : Aluno tem anos e nota usando a concatenação e a interpolação de strings.
*/
string nome = "Paulo";
int idade = 17;
double nota = 7.5;
//Concatenação de string:
System.Console.WriteLine( nome + " tem " + idade + " anos e nota " + nota);
//Interpolação de string:
System.Console.WriteLine($"{nome} tem {idade} anos e nota {nota}");


/*
    Para o exercício anterior exiba o nome a idade e a nota em linhas separadas usando as sequências de escapes.
*/
System.Console.WriteLine($"{nome} tem \n{idade} anos e \nnota {nota}");   


/*
    Para qual tipo de dados você pode converter um float implicitamente ?
    (x) int
    ( ) double
    ( ) long
    ( ) decimal
*/


/*
    Em qual conversão numérica você precisaria realizar o casting (convesão forçada) ?
    (x) int para long
    ( ) double para long
    ( ) double para float
    ( ) decimal para float
    ( ) long para int
    ( ) double para decimal
*/


/*
    Escreva um programa que recebe 3 letras via teclado e as exiba na ordem reversa usando
    a concatenação e também a interpolação de strings
*/
System.Console.WriteLine("Dígite a primeira letra:");
string letraUm = Console.ReadLine();
System.Console.WriteLine("Dígite a segunda letra:");
string letraDois = Console.ReadLine();
System.Console.WriteLine("Dígite a terceira letra:");
string letraTres = Console.ReadLine();
System.Console.WriteLine(letraTres + letraDois + letraUm);
System.Console.WriteLine($"{letraTres} {letraDois} {letraUm}");


/*
    Marque verdadeiro(V) ou falso(F) para os códigos abaixo:
    (F) long resultado = 1.32;
    (V) var nome = “Maria”;
    (F) string resultado = 100.ToString();
    (V) A sequência de escape \n inclui uma nova linha
    (F) float f = 5.45;
    (F) decimal valor = (decimal) 10.99f;
    (V) var status = null;
    (V) object o = 12.45m;
    (V) string titulo = true.ToString();
    (F) A sequencia \t inclui uma tabulação vertical
*/

/*
    Escreva um programa para receber dois valores via teclado do tipo double e a seguir
    realize as operações de soma, subtração, multiplicação, exponenciação, divisão e módulo
    exibindo o resultado:
*/ 

/*
    Escreva um programa que receba um nome e uma senha via teclado. Nome é uma string e
    Senha é um inteiro. Se o nome for igual a ‘admin’ ou ‘maria’ e a senha for igual a ‘123’
    então exiba a mensagem ‘Login feito com sucesso’ caso contrário exiba a mensagem ‘Login
    inválido’: (use o operador condicional ternário)
*/

/*
    Escreva um programa que recebe via teclado dois números inteiros x e y e imprima no
    console se x é par ou não e se y é par ou não. Use o operador condicional ternário (? :)
*/