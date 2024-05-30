public class ContaBancaria
{
    string NumeroConta;
    string Titular;
    double Saldo;

    public ContaBancaria()
    {
        NumeroConta = "Desconhecido";
        Titular = "Desconhecido";
        Saldo = 0.0;
    }

    public ContaBancaria(string NumeroConta, string Titular, double Saldo)
    {
        this.NumeroConta=NumeroConta;
        this.Titular=Titular;
        this.Saldo=Saldo;
    }
}