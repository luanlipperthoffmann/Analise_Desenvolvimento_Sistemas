# 26. Energia Cinética: Peça ao usuário a massa de um objeto em quilogramas e sua velocidade em metros por segundo. Calcule a energia cinética. Apresente o valor.

massa = float (input("Dígite a massa do objeto em kg: "))
velocidade = float (input("Dígite a velocidade em m/s: "))
energia_cinetica = (massa*(velocidade*velocidade))/2
print(f"a energia ciética é de: {energia_cinetica}j")