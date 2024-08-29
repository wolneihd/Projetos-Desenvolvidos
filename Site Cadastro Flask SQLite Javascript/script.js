function getData() {
    let nome = document.getElementById('nome').value;
    let idade = document.getElementById('idade').value;
    if (nome.length == 0 || idade.length == 0) {
        alert('Campo vazio, tentar novamente.')
    } else {
        let usuario = {
            'nome': nome,
            'idade': idade
        }
        return usuario
    }
}

function cleanField() {
    document.getElementById('nome').value = '';
    document.getElementById('idade').value = '';
    console.log('Campos de input zerados!')
}

// insert user in DB
async function insertDataDB() {
    var usuario = getData()
    console.log('insertDataDB', usuario);
    document.getElementById('nome').value = '';
    document.getElementById('idade').value = '';
    try {
        var apiUrl = `http://localhost:5000/get/${usuario.nome}/${usuario.idade}`;

        const response = await fetch(apiUrl, {
            headers: { 'Content-Type': 'application/json' },
            method: "GET"
        });

        if (!response.ok) {
            throw new error("Could not fetch resource!");
        }
        const data = await response.json();
        getAllUsers()
    }
    catch (error) {
        console.log(error);
    }
}

//  START application and update status
getAllUsers()
function changeStatusAPI(status) {
    var paragrafo = document.getElementById('status');
    if (status == false) {        
        paragrafo.innerHTML = 'NOT RUNNING';
        paragrafo.style.color = 'red';
        paragrafo.style.fontWeight = 'bold';
    } else {
        paragrafo.innerHTML = 'RUNNING';
        paragrafo.style.color = 'green';
        paragrafo.style.fontWeight = 'bold';
    }

}

// Get object with all users:
async function getAllUsers() {
    try {
        var apiUrl = `http://localhost:5000/`;

        const response = await fetch(apiUrl, {
            headers: { 'Content-Type': 'application/json' },
            method: "GET"
        });

        if (!response.ok) {
            throw new error("Could not fetch resource!");
        }
        const data = await response.json();
        changeStatusAPI(true)
        showData(data)
    }
    catch (error) {
        console.log(error);
        changeStatusAPI(false)
    }
}

// Show in HTML all users
function showData(listUsers) {
    // clean table for new data to be showed:
    document.getElementById('new-row').innerHTML = ''
    document.getElementById('new-row').innerHTML = `<tr><th>id</th><th>nome</th><th>idade</th><th>Editar</th><th>Excluir</th></tr>`
    // insert new rows into the table
    var newRow = document.getElementById('new-row')
    for (i = 0; i < listUsers.length; i++) {
        newRow.innerHTML += `
        <td>${i + 1}</td>
        <td>${listUsers[i].nome}</td>
        <td>${listUsers[i].idade}</td>
        <td><button onclick="getOneUser(${listUsers[i].id_database})">Editar</button></td>
        <td><button onclick="deleteUser(${listUsers[i].id_database})">Excluir</button></td>
        `;
    }
}

// Função para excluir linha
async function deleteUser(index) {
    console.log('excluindo id n°: ', index)

    try {
        var apiUrl = `http://localhost:5000/delete/${index}`;

        const response = await fetch(apiUrl, {
            headers: { 'Content-Type': 'application/json' },
            method: "GET"
        });

        if (!response.ok) {
            throw new error("Could not fetch resource!");
        }
        const data = await response.json();
        console.log(data)
        getAllUsers()
    }
    catch (error) {
        console.log(error);
    }
}

// Função para editar linha
async function getOneUser(index) {
    try {
        var apiUrl = `http://localhost:5000/get-one-user/${index}`;

        const response = await fetch(apiUrl, {
            headers: { 'Content-Type': 'application/json' },
            method: "GET"
        });

        if (!response.ok) {
            throw new error("Could not fetch resource!");
        }
        const data = await response.json();
        document.getElementById('nome').value = data.nome;
        document.getElementById('idade').value = data.idade;
        createButtons(index)
    }
    catch {
        console.log('error');
    }
}

function createButtons(index) {
    var botoes = document.getElementById('all-buttons')
    botoes.innerHTML = '';
    botoes.innerHTML = `
    <button onclick='saveChanges(${index})'>Atualizar</button>
    <button onclick='returnButtons()'>Cancelar</button>
    `;
}

async function saveChanges(index) {
    var usuario = getData()

    try {
        var apiUrl = `http://localhost:5000/update/${index}/${usuario.nome}/${usuario.idade}`;

        const response = await fetch(apiUrl, {
            headers: { 'Content-Type': 'application/json' },
            method: "GET"
        });

        if (!response.ok) {
            throw new error("Could not fetch resource!");
        }
        const data = await response.json();
        returnButtons()
        getAllUsers()
    }
    catch (error) {
        console.log(error);
    }
}

function returnButtons() {
    var botoes = document.getElementById('all-buttons')
    document.getElementById('nome').value = '';
    document.getElementById('idade').value = '';
    botoes.innerHTML = '';
    botoes.innerHTML = `
        <button onclick="insertDataDB()">Salvar</button>
        <button onclick="cleanField()">Limpar</button>
        <!-- <button onclick="getAllUsers()">Ver todos</button> -->
    `;
}