/*
1 - Escreva um programa para receber 3 números inteiros e a seguir calcular e exibir qual deles é o maior
Encontre o maior dentre 3 números:
Primeiro Número : 65465
Segundo Número : 64658;
Terceiro Número : 65464
O primeiro número : 65465 é o maior


    int num1 = 65465;
    int num2 = 64658;
    int num3 = 65464;
    if (num1 > num2 & num1 > num3)
    {
        System.Console.WriteLine($"O número 1 é o maior: {num1}");
    } 
    if (num2 > num1 & num2 > num3)
    {
        System.Console.WriteLine($"O número 2 é o maior: {num2}");
    }
    if (num3 > num1 & num3 > num2)
    {
        System.Console.WriteLine($"O número 3 é o maior: {num3}");
    }
*/


/*
2- Escreva um programa para exibir os 10 primeiros números naturais e calcular a sua soma usando os loop 
while, do-while e for.
Os 10 primeiros números naturais são :
1 2 3 4 5 6 7 8 9 10
A soma dos números é : 55


    int i =1;
    int soma = 0;
    while (i>=1 && i<11)
    {
        System.Console.WriteLine(i);
        soma += i;
        i++;
    } 
    System.Console.WriteLine($"A soma dos números naturais é de: {soma}");
*/


/*
3- Escreva um programa para exibir a tabela de multiplicação de um número natural maior que zero 
recebido via teclado 
- Verifique se o número é maior que zero e emita uma mensagem
- Considere a tabela de multiplicação de 1 até 10
- Após exibir a tabela torne a solicitar outro número 
- Para sair do loop defina uma condição de saída 
Dica: Use os loop while e for e para sair a instrução break;
*/
char continue; //dando erro na conversao, verificar com o prof
System.Console.WriteLine("Deseja realizar uma multiplicação?");
continue = Convert.ToChar(Console.ReadLine().ToUpper());

while (continue=="S")
{
    System.Console.WriteLine("Informe o numero a ser multiplicado:");
    int multiplicador = Convert.ToInt32(Console.ReadLine());
    if (multiplicador>0)
    {
        
        for(int i=1; i<=10; i++)
        {   
            System.Console.WriteLine($"{multiplicador}x{i}= {multiplicador*i}"); 
        }
    } 
    else 
    {
        System.Console.WriteLine("Número invalido!");
    }
}



    

/*
4- Crie um programa para exbir no console os números pares de 10 a 20, ambos incluídos, exceto 16, de 3 
maneiras diferentes:
- Incrementando 2 em cada passo
- Incrementando 1 em cada passo 
- Com e loop infinito (use "break" e "continue")
*/

/*
5 - Escreva um programa para calcular o fatorial de um número inteiro. 
O fatorial de um número é representado por : n! => n * (n – 1) * (n – 2) ....2*1 
Exemplo : fatorial de 6 é representado por 6! = 6*5*4*3*2*1     
*/

/*
6 - Escreva um programa para exibir as tabelas de multiplicação do 2 ao 6 usando o loop do-while aninhado

Modelo de saída
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
*/

/*
7 - Crie um programa que recebe na entrada de dados um número inteiro de 0 a 10 que representa a nota de 
um aluno. Com base na tabela a seguir imprima no console qual o resultado da avaliação do aluno. (Use a 
instrução switch, break e default em um loop infinito e defina uma condição de saida.)
VER IMAGEM NA TDE
*/

/*
8 - Crie um programa para realizar as operações de adição, subtração, multiplicação e divisão de números 
inteiros. (considere que na divisão podemos ter números fracionários e que não existe divisão por zero e 
quando isso ocorrer exibir uma mensagem de alerta
VER IMAGEM NA TDE
*/


