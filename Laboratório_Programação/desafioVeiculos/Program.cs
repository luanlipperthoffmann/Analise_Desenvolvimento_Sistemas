List<Veiculo> Veiculos = new List<Veiculo>();

Carro carro = new Carro();
Moto moto = new Moto();

Veiculos.Add(carro);
Veiculos.Add(moto);

foreach (var veiculo in Veiculos)
{
    veiculo.Acelerar();
    System.Console.WriteLine($"A velocidade do meu {veiculo} é de: {veiculo.ExibirVelocidade()} km");
    veiculo.Frear();
    System.Console.WriteLine($"A velocidade do meu {veiculo} é de: {veiculo.ExibirVelocidade()} km");
}