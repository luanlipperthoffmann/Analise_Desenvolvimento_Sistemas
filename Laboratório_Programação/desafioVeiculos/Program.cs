Carro carro = new Carro();

Moto moto = new Moto();

List<Veiculo> Veiculo = new List<Veiculo>();
Veiculo.Add(carro);
Veiculo.Add(moto);

foreach (var veiculo in Veiculo)
{
    veiculo.Acelerar();
    System.Console.WriteLine($"A velocidade do meu {veiculo} é de: {veiculo.ExibirVelocidade()} km");
    veiculo.Frear();
    System.Console.WriteLine($"A velocidade do meu {veiculo} é de: {veiculo.ExibirVelocidade()} km");
}