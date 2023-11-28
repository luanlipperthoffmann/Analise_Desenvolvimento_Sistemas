//Pega elementos pelo od
const titulo = document.getElementById('titulo')

titulo.innerHTML = 'Novo Titulo'

titulo.style.color = 'greem'
titulo.style.textAlign = 'center'
titulo.style.fontSize = '80px'

//Pega elementos pela tag
const paragrafos = document.getElementsByTagName('p')
paragrafos[0].innerHTML = 'Novo texto 1'
paragrafos[1].style.color = 'green'
paragrafos[2].style.fontWeight = 'bold'

for (let i = 0; i < paragrafos.length; i++){
    paragrafos[i].style.color = 'red'
    paragrafos[i].style.fontSize = '30px'
}

//Pega elementos pela Classe
const quadrados = document.getElementsByClassName('quadrado')

quadrados[0].style.width = '200px'
quadrados[0].style.height = '200px'
quadrados[1].style.backgroundColor = 'green'
quadrados[2].style.backgroundColor = 'blue'

//Pegando elementos pelo seletor
const titulo2 = document.querySelector('#titulo')
titulo2.innerText = 'Titulo pelo Seletor'

const quadrado1 = document.querySelector('.quadrado')
quadrado1.style.backgroundColor = 'pink'

const todosQuadrados = document.querySelectorAll('.quadrado')
todosQuadrados[1].style.backgroundColor = 'purple'

// Alterar atributos
function trocarFoto(){
    const foto = document.querySelector('img')
    foto.style.marginLeft = '400px'
    foto.src = './imagens/js2.jpg'
}

function voltarFoto(){
    foto.src = './imagens/js1.jpeg'
}

const siteGoogle = document.querySelector('a')

siteGoogle.href = 'http://www.google.com'

//Criando elementos
const meuElemento = document.createElement('h2')
meuElemento.innerText = 'Meu Elemento'

const elementoPai = document.getElementById('pai')
elementoPai.appendChild(meuElemento)

