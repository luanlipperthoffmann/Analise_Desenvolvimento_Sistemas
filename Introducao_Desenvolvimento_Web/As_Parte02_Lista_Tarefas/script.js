function adicionar(){
    const nomeTarefa = document.getElementById('tarefa').value
    const li = document.createElement('li');
    li.innerText = ' '

    const btnRemover = document.createElement('button');
    btnRemover.type = 'button';
    btnRemover.innerText = 'Remover';
    btnRemover.addEventListener('click', function() {li.remove()})

    const checkbox = document.createElement('input')
    checkbox.type = 'checkbox';
    checkbox.addEventListener('click', function(){
        //ADICIONAR NO CONCLUIDOS.
        const tarefasConcluidas = document.getElementById('tarefasConcluidas')
        tarefasConcluidas.appendChild(li)
        const date = new Date()
        span.innerText +=  `    ${date.getHours()}:${date.getMinutes()}`
        span = marcar(li)
    })

    const span = document.createElement('span' )
    span.innerText = nomeTarefa

    const div = document.createElement('div')

    div.appendChild(checkbox)
    div.appendChild(span)

    li.appendChild(div)
    li.appendChild(btnRemover)
    
    const tarefasPendentes = document.getElementById('tarefasPendentes')
    tarefasPendentes.appendChild(li)
}

function mudaDark(){
    const body = document.querySelector('body')
    body.classList.add('darkTheme')
}
function mudaLight(){
    const body = document.querySelector('body')
    body.classList.remove('darkTheme')
}
function marcar(){
    const li = document.querySelector('li')
    li.classList.toggle('selected')
}