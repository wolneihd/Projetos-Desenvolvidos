var numero_postagem = 0;

function salvar_texto() {
    numero_postagem++;
    var texto = $('#entradaTexto').val();
    var dt = new Date();
    var time = dt.getDay() + "/" + dt.getMonth() + ' ' + dt.getHours() + ":" + dt.getMinutes();
    var novoParagrafo = $(`
        <div class='novaPostagem'>
            <p>${texto}</p>
            <p class='dados_postagem'>Postagem número: ${numero_postagem} | Data da postagem: ${time} | Postado por Wolnei Hellmann Dircksen.</p>  
        </div>  
    `)
    $('#postagens').append(novoParagrafo);
}