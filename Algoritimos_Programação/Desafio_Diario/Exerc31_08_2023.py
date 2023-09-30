'''E aí, galera codefit? Estamos trazendo um desafio daqueles que vão trabalhar a mente e a saúde ao mesmo tempo! Sabe aquele algoritmo que é quase como um "match" entre você e a balança? Isso mesmo, estamos falando do famoso IMC - Índice de Massa Corporal!
Mas antes de encararmos essa matemática gostosa (ou não), precisamos te contar uma coisa. Lembram que nós programadores adoramos uma abstração? Pois é, o IMC é um jeito de abstrair a nossa relação com o peso e altura, mostrando se estamos naquela zona tranquila ou se o alerta da "tilinha" apareceu!
A fórmula é simples, só precisa dividir seu peso (em kg) pela sua altura ao quadrado (em metros). Ficou assustado? Nada de pânico! Nós temos um desafio incrível pra você: criar um algoritmo em Python que calcule automaticamente o seu IMC. Sim, nós sabemos que você adora desafios de lógica, mas desta vez, vai ter um toque de dieta nele! 😉
Fórmula do IMC: IMC = peso / altura². Agora, o que queremos de você é: solte a criatividade e crie um algoritmo que, ao inserir seu peso e altura, te apresente o resultado do seu IMC. Vamos lá, pessoal, mostrem que vocês são "pesados" de talento em programação e que também sabem como cuidar do seu corpo virtual e real! 💻🥦💪'''

peso = float (input("Dígite seu peso em kg: \n"))
altura = float (input("Digite sua altura em metros: \n"))
imc = peso/(altura*altura)
if imc < 18.5:
    print(f"Seu IMC é de {imc:.2f}. Voçê está magro, capriche na pizza!")
elif imc >=18.5 and imc <=24.9:
    print(f"Seu IMC é de {imc:.2f}. Voçê está otimo, continue assim!")
elif imc >=25 and imc <=29.9:
    print(f"Seu IMC é de {imc:.2f}. Voçê está acima do peso, cuidado com a pizza!")
elif imc >=30:
    print(f"Seu IMC é de {imc:.2f}. Voçê está obeso, procure um nutricionista urgente!")