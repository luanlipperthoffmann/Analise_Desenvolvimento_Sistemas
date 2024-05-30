public class Retangulo
{
    double altura;
    double largura;

    public Retangulo(double altura, double largura){
        this.altura= altura;
        this.largura = largura;
    }
    public double CalcularArea(){
        return altura * largura;
    }

    public double CalcularArea( double altura, double largura){
        return altura*largura;
    }
}