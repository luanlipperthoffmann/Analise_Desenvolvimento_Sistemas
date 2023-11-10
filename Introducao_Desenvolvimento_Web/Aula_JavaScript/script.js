/*
    alert("Hello World!");
    let nome 
    nome = prompt("Digite seu nome: ")
    console.log(nome)          
*/

//Testanto idade & Teste de condição AND
/*
    let idade

    idade = prompt("Dígite sua idade: ")

    if (idade>= 0 && idade <=120){
        if (idade>= 18){
            alert("Voçê é maior;")
        }
        else{
            alert("Voçê é de menor!")
        }
    }
    else{
        alert("Idade Inválida!")
    }
*/

//Teste de condição OR
/*
    let idade, passeLivre

    idade = prompt("Qaul sua idade: ")
    passeLivre - prompt("VoçÊ possui passe livre? s-sim n-não")

    if(idade>= 18 || passeLivre =="s"){
        alert("Acesso liberado!")
    }
    else{
        alert("Voçê não está autorizado a entrar na festa.")
    }
*/

//switch
/*
    let opcao
    opcao = prompt("Escolha a opção de 1 a 4: ")

    switch(opcao){
        case '1':
            alert("Voçê escolheu a opção 1.")
            break
        case '2':
            alert("Voçê escolheu a opção 2.")
            break
        case '3':
            alert("Voçê escolheu a opção 3.")
            break
        case '4':
            alert("Voçê escolheu a opção 4.")
            break
        default:
            alert("Opção inválida!")
    }
*/

//Operadores Aritimetéticos
/*
    soma +
    subtracao -
    multiplicação *
    divisão /
    resto %
*/

//Operadores Lógicos
/*
    And (E) &&
    OR (OU) ||
    Negação (NOT) !
*/

//contador for
/*
    for(let i=1; i<=10; i++){
    alert(i)
}
*/

//concatenar strings
/*
    let nome, sobrenome
    nome = prompt("Dígite seu nome: ")
    sobrenome = prompt("Dígite seu sobrenome: ")
    alert(nome + " " + sobrenome)
*/

//concatenar strings com interpolação
/*
    let nome, sobrenome
    nome = prompt("Digite seu nome:")
    sobrenome = prompt("Digite seu sobrenome:")
    alert(`Seu nome é ${nome} ${sobrenome}`)
*/

//Acumulador
/*
    let soma=0
    for(let i=1; i<=10; i++){
        soma = soma + i
        soma += i
    }
    alert(soma)
*/

//repetição com contador
/*
    let numero = 0
    let i = 1
    while(numero!=1){
        numero = pronpt("Dígite um número")
        i++
    }
    alert("Voçê Digitou ${i} números. ")
*/