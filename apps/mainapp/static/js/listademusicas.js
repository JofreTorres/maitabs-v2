var botaoAdicionar = document.querySelector("#adicionar-musica");
botaoAdicionar.addEventListener("click", function(event) {
    event.preventDefault();

    var form = document.querySelector("#form-adiciona");

    var nome = form.nome.value;
    var banda = form.banda.value;
    var genero = form.genero.value;
    var album = form.album.value;

    var musicaTr = document.createElement("tr");

    var nomeTd = document.createElement("td");
    var bandaTd = document.createElement("td");
    var generoTd = document.createElement("td");
    var albumTd = document.createElement("td");

    nomeTd.textContent = nome;
    bandaTd.textContent = banda;
    generoTd.textContent = genero;
    albumTd.textContent = album;

    musicaTr.appendChild(nomeTd);
    musicaTr.appendChild(bandaTd);
    musicaTr.appendChild(generoTd);
    musicaTr.appendChild(albumTd);

    var tabela = document.querySelector("#tabela-musicas");

    tabela.appendChild(musicaTr);
});