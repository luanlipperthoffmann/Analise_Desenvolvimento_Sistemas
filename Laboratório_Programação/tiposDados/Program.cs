//Declarando variaveis númericas inteiras
/*
    byte valor01 = 255;
    sbyte valor02 = -127;
    int valor03 = -2147483648;
    uint valor04 = 2147483648;

    Console.WriteLine(valor01);     //Inteiro de 8 bits sem sinal
    Console.WriteLine(valor02);     //Inteiro de 8 bits com sinal
    Console.WriteLine(valor03);     //Inteiro assinado de 32 bits
    Console.WriteLine(valor04);     //Inteiro de 32 bits sem sinal
*/
z
//Declarando variaveis de ponto flutuante
/*
    double n1 = 1.234;      //Double usado para calculos cientificos
    float n2 = 1.234f;
    decimal n3 = 1.234m;      //Decimal usado para calculos financeiros
    Console.WriteLine(n1); 
    Console.WriteLine(n2);
    Console.WriteLine(n3);

    float x = 1f/3f;
    double y = 1d/3d;
    decimal z = 1m/3m;
    Console.WriteLine(x); 
    Console.WriteLine(y);
    Console.WriteLine(z);
*/

//Declarando variaveis boobleano
/*
    bool ativo = true;
    bool inativo = false;
    Console.WriteLine(ativo);
    Console.WriteLine(inativo);
    Console.WriteLine(10 == 10);
    Console.WriteLine(10 == 15);
*/

//Declarando variaveis char
/*
char letra1 -'A';   //tipo caractere
char letra2 = '\u0041'; // tipo unicode
*/

//Definindo variaveis do tipo string, object, dynamic
/*
    string nome = "Análise e Desenvolvimento de Sistemas";
    string disciplina = "Laboratório de Programação";
    Console.WriteLine(nome);
    Console.WriteLine(disciplina);
*/

/*
    string valor = "Isto é uma string";
    valor = "Isto é uma string alterada";
    Console.WriteLine(valor);
*/

// Tipo Object => É a base para os outros tipos, em tempo de compilação
/*
    object nota = 10;   //inteiro

    object valor01 = 8.55m; //decimal

    object nome01 = "Maria";    //string

    object ativa = true;    //bool

    object letra = 'A'; //char

    Console.WriteLine(nota);
    Console.WriteLine(valor01);
    Console.WriteLine(nome01);
    Console.WriteLine(ativa);
    Console.WriteLine(letra);
*/

//Tipo dynamic  =>Em tempo de execução
/*
    dynamic nota = 10;   //inteiro

    dynamic valor01 = 8.55m; //decimal

    dynamic nome01 = "Maria";    //string

    dynamic ativa = true;    //bool

    dynamic letra = 'A'; //char

    Console.WriteLine(nota);
    Console.WriteLine(valor01);
    Console.WriteLine(nome01);
    Console.WriteLine(ativa);
    Console.WriteLine(letra);
*/

/*
    int? x = null;
    if (x.HasValue){
        Console.WriteLine(x);
    }else {
        Console.WriteLine("X não possui um valor!");
    }
*/

//Variaveis de tipos são do tipo camelCase  ex.:notaAluno
//Metodos e classes são do tipo PascalCase ex.:NotaAluno