var botaoAdicionar = document.querySelect("#adicionar-musica")
botaoAdicionar.addEventListener("click", function(event){
    event.preventDefault();

    var form = document.querySelector("#form-adiciona")

    var nome = form.nome.value;
    var banda = form.banda.value;
    var genero = form.genero.value;
    var album = form.album.value;

    var musicaTr = document.createElement("tr");

    var nomeTd = document.createElement("td");
    var bandaTd = document.createElement("td");
    var generoTd = document.createElement("td");
    var albumTd = document.createElement("td");

    nomeTd.textContext = nome;
    bandaTd.textContext = banda;
    generoTd.textContext = genero;
    albumTd.textContext = album;

    musicaTr.appendChild(nomeTd, bandaTd, generoTd, albumTd);

    var tabela = document.querySelector("#tabela-musicas")

    tabela.appendChild(musicaTr);
});