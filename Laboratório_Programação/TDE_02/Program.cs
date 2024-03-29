/*
    Declare as variáveis nome, idade e nota atribuindo os valores “Paulo”, 17 e 7.5 e exiba a saída no formato : Aluno tem anos e nota usando a concatenação e a interpolação de strings.



    string nome = "Paulo";
    int idade = 17;
    double nota = 7.5;
    //Concatenação de string:
    System.Console.WriteLine( nome + " tem " + idade + " anos e nota " + nota);
    //Interpolação de string:
    System.Console.WriteLine($"{nome} tem {idade} anos e nota {nota}");
*/



/*
    Para o exercício anterior exiba o nome a idade e a nota em linhas separadas usando as sequências de escapes.


    System.Console.WriteLine($"{nome} tem \n{idade} anos e \nnota {nota}");   
*/


/*
    Para qual tipo de dados você pode converter um float implicitamente ?
    ( ) int
    (x) double
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


    char letra1, letra2, letra3;
    System.Console.WriteLine("Dígite a primeira letra: ");
    letra1 = Convert.ToChar(Console.ReadLine());
    System.Console.WriteLine("Dígite a segunda letra: ");
    letra2 = Convert.ToChar(Console.ReadLine());
    System.Console.WriteLine("Dígite a terceira letra: ");
    letra3 = Convert.ToChar(Console.ReadLine());
    System.Console.WriteLine(letra3 ""+ ""letra2 ""+ ""letra1);
    System.Console.WriteLine($"{letra3} {letra2} {letra1}");
*/


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


    System.Console.WriteLine("Dígite o primeiro valor: ");
    double valorUm = Convert.ToDouble(Console.ReadLine());
    System.Console.WriteLine("Dígite o segundo valor: ");
    double valorDois = Convert.ToDouble(Console.ReadLine());
    System.Console.WriteLine($"Soma do Valor Um: {valorUm} + Valor Dois {valorDois} é de: {valorUm+valorDois} ");
    System.Console.WriteLine($"Subtração do Valor Um: {valorUm} + Valor Dois {valorDois} é de: {valorUm-valorDois} ");
    System.Console.WriteLine($"Multiplicao do Valor Um: {valorUm} + Valor Dois {valorDois} é de: {valorUm*valorDois} ");
    System.Console.WriteLine($"Exponenciação do Valor Um: {valorUm} + Valor Dois {valorDois} é de: {Math.Pow(valorUm, valorDois)} ");
    System.Console.WriteLine($"Divisão do Valor Um: {valorUm} + Valor Dois {valorDois} é de: {valorUm/valorDois} ");
    System.Console.WriteLine($"O modulo do Valor Um: {valorUm} + Valor Dois {valorDois} é de: {valorUm%valorDois} ");
    Console.ReadKey();
*/ 



/*
    Escreva um programa que receba um nome e uma senha via teclado. Nome é uma string e
    Senha é um inteiro. Se o nome for igual a ‘admin’ ou ‘maria’ e a senha for igual a ‘123’
    então exiba a mensagem ‘Login feito com sucesso’ caso contrário exiba a mensagem ‘Login
    inválido’: (use o operador condicional ternário)


    System.Console.WriteLine("Dígite o nome de usúario: ");
    string nome = Convert.ToString(Console.ReadLine());
    System.Console.WriteLine("Dígite a senha: ");
    int senha = Convert.ToInt32(Console.ReadLine());
    System.Console.WriteLine( nome == "admin" || nome == "maria" && senha == 123 ?  "Login feito com sucesso" : "Login Inválido");
    Console.ReadKey();
*/


/*
    Escreva um programa que recebe via teclado dois números inteiros x e y e imprima no
    console se x é par ou não e se y é par ou não. Use o operador condicional ternário (? :)


    System.Console.WriteLine("Dígite um número x: ");
    int x = Convert.ToInt32(Console.ReadLine());
    System.Console.WriteLine("Dígite um número y: ");
    int y = Convert.ToInt32(Console.ReadLine());
    System.Console.WriteLine(x%2==0 ? "X é Par" : "X é Impar");
    System.Console.WriteLine(y%2==0 ? "Y é Par" : "Y é Impar");
    Console.ReadKey();
*/
 System.Console.WriteLine("Dígite um número x: ");
    int x = Convert.ToInt32(Console.ReadLine());
    System.Console.WriteLine("Dígite um número y: ");
    int y = Convert.ToInt32(Console.ReadLine());
    System.Console.WriteLine(x%2==0 ? "X é Par" : "X é Impar");
    System.Console.WriteLine(y%2==0 ? "Y é Par" : "Y é Impar");
    Console.ReadKey();