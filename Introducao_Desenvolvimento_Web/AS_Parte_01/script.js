//Exerício 01: Calculadora

const numero1 = document.getElementById('numeroUm')
const numero2 = document.getElementById('numeroDois')
const resultado = document.getElementById('resultado')

function limpar(){
    numero1.value=""
    numero2.value=""
    numero1.focus()
    resultado.innerText= "Resultado: "
}

function somar(){
    let soma = Number(numero1.value)+ Number(numero2.value)
    resultado.innerText = "Resultado: " + soma
}

function subtrair(){
    let menos = Number(numero1.value)- Number(numero2.value)
    resultado.innerText = "Resultado: " + menos
}

function multiplicar(){
    let multiplica = Number(numero1.value)* Number(numero2.value)
    resultado.innerText = "Resultado: " + multiplica
}

function dividir(){
    let dividi = Number(numero1.value)/ Number(numero2.value)
    if(numero2.value<=0){
        alert('Numero 2 não divisivel')
    }
    resultado.innerText = "Resultado: " + dividi
}


//Execicio 02: Notas do Aluno

const apUm = document.getElementById('ap1')
const apDois = document.getElementById('ap2')
const avalSem = document.getElementById('as')
const nf = document.getElementById('notaFinal')

function zerar(){
    apUm.value=""
    apDois.value=""
    avalSem.value=""
    apUm.focus()
    nf.innerText = nf.style.color = 'white'
    nf.innerText= "Nota Final: "
}

function ap1Valida(){
    if (apUm.value<0 || apUm.value>1.5){
        alert('Nota AP1 Incorreta!')
    }
}

function ap2Valida(){
    if (apDois.value<0 || apDois.value>2.5){
        alert('Nota AP2 Incorreta!')
    }
}

function asValida(){
    if (avalSem.value<0 || avalSem.value>6){
        alert('Nota AS Incorreta!')
    }
}

function calcular(){
    let media = Number(apUm.value)+ Number(apDois.value)+ Number(avalSem.value)
    if (media>=6){
        nf.innerText = nf.style.color = '#83E509'
        nf.innerText= "Nota Final: " + media +"! \nAprovado. Parabéns."
    } else if((media<6)){
        nf.innerText = nf.style.color = 'red'
        nf.innerText= "Nota Final: " + media +"! \nReprovado. Reforce seus estudos para realização da AF."
    }
}