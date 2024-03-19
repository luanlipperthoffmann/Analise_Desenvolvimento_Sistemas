/*
    int idade = 25;
    string nome = "Maria";
    System.Console.WriteLine(idade);
    System.Console.WriteLine(nome);

    //CONCATENAÇÃO DE STRINGS
    System.Console.WriteLine( nome + " tem " + idade + " anos.");

    //INTERPOLAÇÃO DE STRINGS
    System.Console.WriteLine($"({nome} tem {idades} anos");
*/

/*
    =>  SEQUÊNCIA DE SCAPES
    string local = "c:\\dados\\poesia.txt"; //duas barrase quivalem a uma barra pra linha de local
    string frase = "Ele falou: \"Não fui eu\"";
    System.Console.WriteLine(local);
    System.Console.WriteLine(frase);
*/

/*
    => CONVERSÃO DE TIPOS:

    =>Conversão implicita
        int varInt = 100;
        double varDouble = varInt
        System.Console.WriteLine(varDouble);
    int => 4 bytes
    double => 8 bytes

    => Conversão explicita, necessita que seja explicito entre parenteses para onde vai 
    double varDouble = 12.456;
    int varInt = (int) varDouble;
    System.Console.WriteLine(varInt);

    int num1 =18;
    int num2 = 4;
    float resultado = (float) num1/num2;
    System.Console.WriteLine(resultado);

    ======================
    
    int varInt = 123;
    double varDouble = 12.456;
    decimal = 12.45670m;

    string s1 = varInt.ToString();
    string s2 = varDouble.ToString();
    string s3 = varDecimal.ToString();

    System.Console.WriteLine(s1);
    System.Console.WriteLine(s2);
    System.Console.WriteLine(s3);

    ============================

    //CONVERSÃO USANDO A CLASSE CONVERT:
    int valorInt = 10;
    double valorDouble = 5.35;
    bool valorBool = true;
    System.Console.WriteLine(Convert.ToString(valorInt));
    System.Console.WriteLine(Convert.ToDouble(valorInt));
    System.Console.WriteLine(Convert.ToString(valorBool));
    System.Console.WriteLine(Convert.ToInt32(valorDouble));

    int varInt = 10000;
    System.Console.WriteLine(Convert.Tobyte(varInt));
*/

/*
    => ENTRADA DE DADOS:

    Console.ReadKey();  //aqui o console esperará a entrada de uma tecla

    System.Console.WriteLine("Dígite seu nome");
    string nome = Console.ReadLine();
    System.Console.WriteLine($"O seu nome é {nome}");
    System.Console.WriteLine("Informe a idade");
    int idade = Convert.ToInt32(Console.ReadLine());
    System.Console.WriteLine($"Sua idade é: {idade}");
    Console.ReadKey();
*/

/*
    => OPERADORES BINÁRIOS:
    + - / * 
    System.Console.WriteLine("Informe o valor de x");
    int x = Convert.ToInt32(Console.ReadLine());

    System.Console.WriteLine("Informe o valor de y");
    int y = Convert.ToInt32(Console.ReadLine());

    System.Console.WriteLine($"A soma de X + Y = {x+y}");

    System.Console.WriteLine($"A subtração de X - Y = {x-y}");

    double divisao = (couble) x/y;
    System.Console.WriteLine($"A divisão de X / Y = {x/y}");

    System.Console.WriteLine($"A multiplicação de X * Y = {x*y}");

    System.Console.WriteLine($"A raiz quadrada de X = {Math.Sqrt(x)}");

    System.Console.WriteLine($"Valor de x elevado a y {Math.Pow(x, y)}");
*/

/*
    //VARIAVÉIS DO TIPO VAR, É IMPLICITO E SEMPRE DEVE SER INICIALIZADO
    var z  = 10;

    var nome2 = "Luan";
*/

/*
    OPERADORES DE ATRIBUIÇÃO / RELACIONAIS / LOGICOS / TERNÁRIOS:
    =>  Verificar Tabela aula  03;

    &&  => AND/E
    ||  => OR/OU
    !   => NOT/NÃO

    => OPERADORES TERNÁRIOS
    System.Console.WriteLine("Informe a temperatura");
    var temp Convert.ToDouble(Console.ReadLine());

    var resultado = temp > 27 ? "Quente" : "Normal";
    System.Console.WriteLine($"O tempo está {resultado}");
*/