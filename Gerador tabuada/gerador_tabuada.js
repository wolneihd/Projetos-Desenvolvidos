var contador = 0;
let div_tabuada = document.getElementById('container_tabuada');

function criar_tabuada() {
	let valor = document.getElementById('valor').value;
	var teste_preenchido = document.getElementById(0);
	
	if (teste_preenchido) {
		for (i=0;i<=10;i++) {
			var excluir = document.getElementById(i);
			excluir.remove();
		}		
	}	
	if (valor != '') {
		for (i=0;i<=10;i++){
			let novoItem = `<p id='${i}' class='valores_tabuada'>${i} x ${valor} = ${i*valor} </p>`;
			div_tabuada.innerHTML += novoItem;
			contador++;
			if (i%2 != 0){
				var linha = document.getElementById(i);
				linha.style.backgroundColor = '#f2f2f2';
			}
		}
	}
	else {
		alert('O valor deve ser obrigatoriamente preenchido!');
	}	
}

function limpar() {
	document.getElementById('valor').value = '';
	var teste_preenchido = document.getElementById(0);
	if (teste_preenchido) {
		for (i=0;i<=10;i++) {
			var excluir = document.getElementById(i);
			excluir.remove();
		}		
	}
}
