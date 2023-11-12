function exercicio01(){
    let numeroUm, numeroDois, resultado
    numeroUm = prompt ("Dígite o primeiro numero: ")
    numeroDois = prompt ("Dígite o segundo numero: ")
    resultado = numeroUm/ numeroDois
    alert("O resultado da divisão de "+ numeroUm +" por " +numeroDois +" é de: " + resultado)
}

function exercicio02(){
    let numero
    numero = prompt ("Dígite um numero: ")
    if(numero>=0 && numero%2==0){
        alert("O número é positivo e par")
    } else if(numero>=0 && numero%2!=0){
            alert("O número é positivo e impar")
    }   else if(numero<0 && numero%2==0){
            alert("O número é negativo e par")
    }   else if(numero<0 && numero%2!=0){
        alert("O número é negativo e impar")
    }
}

function exercicio03(){
    let nome, idade
    nome = prompt ("Informe seu nome: ")
    idade = prompt (" Informe sua idade: ")
    if (idade>18){
        alert(nome +" tem " + idade + " anos. \nÉ maior de idade!")
    } else if (idade<18 && idade >=0){
        alert(nome +" tem " + idade + " anos. \nÉ menor de idade!")
    } else if (idade<0){
        alert("A ídade dígitada está incorreta!")
    }
}

function exercicio04(){
    let numero=0, i=1, resultado
    numero = prompt ("Informe o número da tabuada desejada: ")
    for (i=1; i<=10; i++){
        resultado = numero * i
        alert (numero + " x " + i + " = " + resultado)
    }
    alert (numero + " x " + i + " = " + resultado)
}

function exercicio05(){
    let notaUm, notaDois, notaTres, resultado
    notaUm = prompt ("Informe a primeira nota do aluno: ")
    notaDois = prompt ("Informe a segunda nota do aluno: ")
    notaTres = prompt ("Informe a terceira nota do aluno: ")
    resultado = (parseFloat(notaUm) + parseFloat(notaDois) + parseFloat(notaTres))/3
    if (resultado>=6){
        alert ("A média foi de: " + resultado + ". \nVoçê está APROVADO!")
    } else if (resultado<6 && resultado>=0){
        alert ("A média foi de: " + resultado + ". \nVoçê está REPROVADO!")
    } else if (resultado<0){
        alert ("A notas dígitadas estão incorretas!")
    }
}

function exercicio06(){
    let opcao
    opcao = prompt("Escolha a opção de 1 a 7: ")

    switch(opcao){
        case '1':
            alert("1 = Domingo")
            break
        case '2':
            alert("2 = Segunda-Feira")
            break
        case '3':
            alert("3 = Terça-Feira")
            break
        case '4':
            alert("4 = Quarta-Feira")
            break
        case '5':
            alert("5 = Quinta-Feira")
            break
        case '6':
            alert("6 = Sexta-Feira")
            break
        case '7':
            alert("7 = Sábado")
            break
        default:
            alert("Opção inválida!")
    }   
}

function exercicio07(){
    let soma=0
    for(let i=0; i<=100; i++){
        if(i%3==0){
            soma+=i
        }
    }
    alert(soma)
}

function exercicio08(){
    let numero = 0
    let soma = 0
    let contador = 0
    let media = 0
    while(numero>=0){
        numero = parseFloat ( prompt("Dígite um número: ") )
        if (numero>=0){
            soma+=numero
            contador++
        }
        media=soma/contador
    }
    alert("A média dos " + contador + " números digitados é de: " + media)
}