
const numberElement = document.getElementById("sensor"); // Toma el ID "sensor" del html para trabajar con el
const circleElement = document.querySelector(".circulo");// Toma la clase "circulo" del html para trabajar con el
const uvBar = document.getElementById("rango"); //Toma el ID "rango" del html para trabajar con el

function updateNumberAndUvBar(newNumber) { //Funcion para el cambio de color segun el indice UV

    if (newNumber <= 2) {//Condiciones para cambiar de color del circulo 
        circleElement.style.backgroundColor = "#29e01f"; // Verde
        uvBar.innerText = "Bajo"; //Usado para cambiar el texto segun el indice 
    } else if (newNumber <= 5) {
        circleElement.style.backgroundColor = "#d6e01f"; // Amarillo
        uvBar.innerText = "Moderado";
    }else if (newNumber <= 7) {
        circleElement.style.backgroundColor = "#e36f09"; // naranja
        uvBar.innerText = "Alto";
    } else if (newNumber <= 10) {
        circleElement.style.backgroundColor = "#d12424"; // Rojo
        uvBar.innerText = "Muy alto";
    }else if (newNumber > 10) {
        circleElement.style.backgroundColor = "#b62dfa"; // morado
        uvBar.innerText = "Extremo";
    }

}

// Función para actualizar el número y llamar a la función combinada
function update() {
    const currentNumber = parseInt(numberElement.textContent);
    updateNumberAndUvBar(currentNumber);
}
setInterval(update, 100);
