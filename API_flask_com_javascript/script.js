'use strict'

// Incluir cidades na lista de selection:

var estados = ['AC',
    'AL',
    'AM',
    'AP',
    'BA',
    'CE',
    'DF',
    'ES',
    'GO',
    'MA',
    'MG',
    'MS',
    'MT',
    'PA',
    'PB',
    'PE',
    'PI',
    'PR',
    'RJ',
    'RN',
    'RO',
    'RR',
    'RS',
    'SC',
    'SE',
    'SP',
    'TO'];
for (var i = 0; i < estados.length; i++) {
    var opcao = $(`<option value="${estados[i]}">${estados[i]}</option>`)
    $('#estados').append(opcao);
}

// funções de catch dos dados

async function fetchData_todas_capitais() {
    try {
        const response = await fetch(`http://127.0.0.1:5000/cidade`, {
            headers: { 'Content-Type': 'application/json' },
            method: "GET"
        });

        if (!response.ok) {
            throw new error("Could not fetch resource!");
        }
        const data = await response.json();
        incluir_dados_tabela(data)
    }
    catch (error) {
        console.log(error);
    }
}

async function fetchData_busca_cidade() {
    try {
        var nome_cidade = document.getElementById('input_cidade').value;
        var apiUrl = `http://127.0.0.1:5000/cidade/${nome_cidade}`;
        console.log(apiUrl);

        const response = await fetch(apiUrl, {
            headers: { 'Content-Type': 'application/json' },
            method: "GET"
        });
        if (!response.ok) {
            throw new error("Could not fetch resource!");
        }
        const data = await response.json();
        incluir_dados_tabela(data)
    }
    catch (error) {
        console.log(error);
    }
}

async function fetchData_cidade_estado() {
    try {
        var e = document.getElementById("estados");
        var value = e.value;
        var text = e.options[e.selectedIndex].text;
        console.log(text)

        var apiUrl = `http://127.0.0.1:5000/estado/${text}`;
        console.log(apiUrl);

        const response = await fetch(apiUrl, {
            headers: { 'Content-Type': 'application/json' },
            method: "GET"
        });

        if (!response.ok) {
            throw new error("Could not fetch resource!");
        }
        const data = await response.json();
        incluir_dados_tabela(data)
    }
    catch (error) {
        console.log(error);
    }
}

// função de limpar tabela e incluir as linhas na tabela dinâmica

function incluir_dados_tabela(data) {
    $('.linha_dinamica').remove();
    for (let i = 0; i < data.length; i++) {
        var new_row = $(`<tr class='linha_dinamica'>
            <td class='linha_dinamica'>${i}</td>
            <td class='linha_dinamica'>${data[i]['municipio']}</td>
            <td class='linha_dinamica'>${data[i]['uf']}</td>
            <td class='linha_dinamica'>${data[i]['uf_code']}</td>
            <td class='linha_dinamica'>${data[i]['name']}</td>
            <td class='linha_dinamica'>${data[i]['mesoregion']}</td>
            <td class='linha_dinamica'>${data[i]['microregion']}</td>
            <td class='linha_dinamica'>${data[i]['rgint']}</td>
            <td class='linha_dinamica'>${data[i]['rgi']}</td>
            <td class='linha_dinamica'>${data[i]['osm_relation_id']}</td>
            <td class='linha_dinamica'>${data[i]['wikidata_id']}</td>
            <td class='linha_dinamica'>${data[i]['is_capital']}</td>
            <td class='linha_dinamica'>${data[i]['wikipedia_pt']}</td>
            <td class='linha_dinamica'>${data[i]['lon']}</td>
            <td class='linha_dinamica'>${data[i]['lat']}</td>
            <td class='linha_dinamica'>${data[i]['no_accents']}</td>
            <td class='linha_dinamica'>${data[i]['slug_name']}</td>
            <td class='linha_dinamica'>${data[i]['alternative_names']}</td>
            <td class='linha_dinamica'>${data[i]['pop_21']}</td>
            </tr class='linha_dinamica'>`)
        $('#tabela').append(new_row);
    }
}