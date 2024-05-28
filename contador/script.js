var contador = 0;

function aumentar() {
	let valor = document.getElementById('valor');
	contador++;
	valor.innerHTML = contador;
	if (contador > 0) {
		document.getElementById("valor").style.color = "blue";
		document.getElementById("valor").style.backgroundColor = "#ccccff";
	}
	console.log('aumentar', contador)
}

function zerar() {
	let valor = document.getElementById('valor');
	contador = 0;
	valor.innerHTML = contador;
	document.getElementById("valor").style.color = "black";
	document.getElementById("valor").style.backgroundColor = "#f2f2f2";
	console.log('zerar', contador)
}

function diminuir() {
	let valor = document.getElementById('valor');
	contador--;
	if (contador < 0) {
		document.getElementById("valor").style.color = "red";
		document.getElementById("valor").style.backgroundColor = "#ffcccc";
	}
	valor.innerHTML = contador;
	console.log('diminuir', contador)
}