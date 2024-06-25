public abstract class Veiculo
{
    protected int Velocidade = 100;

    public abstract void Acelerar();
    public abstract void Frear();
    public int ExibirVelocidade(){
        return Velocidade;
    }
}