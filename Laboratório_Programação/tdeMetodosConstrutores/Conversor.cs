public class Conversor
{
    public double Converter(int valor)
    {
        return Convert.ToDouble(valor);
    }

    public int Converter(double valor)
    {
        return Convert.ToInt32(valor);
    }

    public int Converter(string valor)
    {
        return int.Parse(valor);
    }

    public double Converte(string valor)
    {
        return double.Parse(valor);
    }
}