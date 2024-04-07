/* if com string
System.Console.WriteLine("### Instrução IF #####");

System.Console.WriteLine("Cliente especial (S/N)");
var resposta = Console.ReadLine().ToUpper();

if (resposta == "S")
{
    System.Console.WriteLine("Desconto de 10%");
}
*/

/* if com booblean, precisa converter a string pra boolean
System.Console.WriteLine("### Instrução IF #####");

System.Console.WriteLine("Cliente especial (S/N)");
var resposta = Convert.ToBoolean(Console.ReadLine());

if (resposta)
{
    System.Console.WriteLine("Desconto de 10%");
}
*/

// // System.Console.WriteLine("Informe o valor de x:");
// // int x = Convert.ToInt32(Console.ReadLine());

// // System.Console.WriteLine("Informe o valor de y:");
// // int y = Convert.ToInt32(Console.ReadLine());

// // if (x>y)
// // {
// //     System.Console.WriteLine("x é maior que y");
// // }
// // if (x<y)
// // {
// //     System.Console.WriteLine("x é menor que y");
// // }
// // if (x==y)
// // {
// //     System.Console.WriteLine("x é igual a y");
// // }

// System.Console.WriteLine("### INSTRUÇÃO IF-ELSE");
// System.Console.WriteLine("Informe a nota do aluno");
// var nota = Convert.ToInt32(Console.ReadLine());
// if(nota >5)
// {
//     System.Console.WriteLine("O aluno foi aprovado");
// }
// else
// {
//     System.Console.WriteLine("O aluno foi reprovado");
// }

/*
System.Console.WriteLine("Informe o valor de x:");
int x = Convert.ToInt32(Console.ReadLine());
System.Console.WriteLine("Informe o valor de y:");
int y = Convert.ToInt32(Console.ReadLine());
if (x>y)
{
System.Console.WriteLine("x é maior que y");
}
else
{
    if (x<y)
    {
    System.Console.WriteLine("x é menor que y");
    }
    if (x==y)
    {
    System.Console.WriteLine("x é igual a y");
    }
}
*/

/*
System.Console.WriteLine("---ESTRUTURA SWICTH CASE------");
int compra = 600;
System.Console.WriteLine("Valor da compra = R$600,00");
System.Console.WriteLine("Informe o número de parcelas: 1 á 3");
var numParcelas= Convert.ToInt32(Console.ReadLine());
switch(numParcelas)
{
    case 1:
    System.Console.WriteLine($"Prestação R${compra/numParcelas}");
    break;

    case 2:
    System.Console.WriteLine($"Prestação R${compra/numParcelas}");
    break;

    case 3:
    System.Console.WriteLine($"Prestação R${compra/numParcelas}");
    break;

    default:
    System.Console.WriteLine("Valor inválido, informe 1,2,3");
    break;
}
*/

/*
System.Console.WriteLine("---- INSTRUÇÃO WHILE ------");
int i =10;
while(i<12)
{
    System.Console.WriteLine($"i = {i}");
    i++;
}
*/

/*
System.Console.WriteLine("---- INSTRUÇÃO WHILE ------");
int i =10;
do
{
    System.Console.WriteLine($"i = {i}");
    i++;
}while(i<12);
*/

//CALCULADORA USANDO FOR
/*
int numero, resultado;
System.Console.WriteLine("Informe um número inteiro:");
numero = Convert.ToInt32(Console.ReadLine());
for(int i =1; i<=10; i++)
{
    resultado = numero * i;
    System.Console.WriteLine(numero + " X " + i + " = " + resultado);
}
*/

