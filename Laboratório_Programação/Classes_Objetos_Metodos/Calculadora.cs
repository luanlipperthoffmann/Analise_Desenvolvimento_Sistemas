public class Calculadora
{
    public Calculadora(double x, double y)
   {
        num1 = x;
        num2 = y;
    }


    double num1;
    double num2;


    public void Somar(int x, int y)
    {
        var resultado = x +y;
        Console.WriteLine(resultado);
    }

    public void Somar(int x, int y, int z)
    {
        var resultado = x + y + z;
        Console.WriteLine(resultado);
    }

    public void Somar(int a, int b, int c)
    {
        var resultado = (a + b + c);
        Console.WriteLine(resultado);
    }

    public double Divisao(double a, double b)
    {
        var resultado = a / b;
        return resultado;
    }

    public double Divisao()
    {
        return n1 / n2;
    }
}