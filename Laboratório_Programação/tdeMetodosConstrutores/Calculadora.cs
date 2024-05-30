using System.Runtime.InteropServices;
using System.Security.Cryptography.X509Certificates;

public class Calculadora
{
    public int n1;
    public int n2;
    public int n3;
    public int n4;

    public int Soma( int n1, int n2, int n3, int n4)
    {
        this.n1 = n1;
        this.n2 = n2;
        this.n3 = n3;
        this.n4 = n4;
        return n1 + n2 + n3 + n4;
    }

        public void Soma()
    {
        int somar;

        System.Console.WriteLine("Dígite o primeiro valor: ");
        n1 = Convert.ToInt32(Console.ReadLine());

        System.Console.WriteLine("Dígite o segundo valor: ");
        n2 = Convert.ToInt32(Console.ReadLine());

        System.Console.WriteLine("Dígite o terceiro valor: ");
        n3 = Convert.ToInt32(Console.ReadLine());

        System.Console.WriteLine("Dígite o quarto valor: ");
        n4 = Convert.ToInt32(Console.ReadLine());

        somar = n1 + n2 + n3 + n4;

        System.Console.WriteLine(somar);
    }
}