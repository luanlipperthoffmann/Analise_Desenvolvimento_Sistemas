#12. Peso Ideal: Solicite a altura do usuário. Calcule o peso ideal como PesoIdeal = altura * 22. Mostre o peso ideal calculado.

altura= float (input("Dígite sua altura em metros: "))
#peso em libras
peso_ideal = altura*22
#peso em kilos
peso_ideal = 52 + (0.75 *(altura - 152.4))
print(f"O seu pesso ideal é de: {peso_ideal}")