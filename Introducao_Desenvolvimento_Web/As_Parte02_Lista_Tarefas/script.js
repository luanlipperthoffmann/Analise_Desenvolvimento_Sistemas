function adicionar(){
    const nomeTime = document.getElementById('time').value
    const li = document.createElement('li');
    li.innerText = nomeTime
    const listaTimes = document.getElementById('tabelaTimes')
    listaTimes.appendChild(li)
}