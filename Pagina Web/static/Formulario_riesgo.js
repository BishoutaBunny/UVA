// Obtiene el elemento del DOM con el ID "sensor" y lo almacena en la variable `indiceText`.
const indiceText = document.getElementById("sensor");

// Obtiene el elemento del DOM con el ID "factores_riesgo" (un formulario) y lo almacena en la variable `r_formulario`.
const r_formulario = document.getElementById("factores_riesgo");

// Obtiene todos los elementos del DOM con la clase "exclamacion" y los almacena en la variable `signo` como una NodeList.
const signo = document.querySelectorAll(".exclamacion");

// Agrega un event listener al formulario para escuchar el evento "submit".
r_formulario.addEventListener("submit", function (event) {
    // Previene el comportamiento por defecto del formulario (recargar la página).
    event.preventDefault();

    // Obtiene el valor del elemento con ID "tipo_piel", lo convierte a un número entero y lo almacena en `v_pregunta1`.
    let v_pregunta1 = parseInt(document.getElementById("tipo_piel").value);

    // Obtiene el valor del elemento con ID "ante_propio", lo convierte a un número entero y lo almacena en `v_pregunta2`.
    let v_pregunta2 = parseInt(document.getElementById("ante_propio").value);

    // Obtiene el valor del elemento con ID "ante_familiar", lo convierte a un número entero y lo almacena en `v_pregunta3`.
    let v_pregunta3 = parseInt(document.getElementById("ante_familiar").value);

    // Si el valor de `v_pregunta2` es 8, establece `v_pregunta3` en 0.
    if (v_pregunta2 === 8) { v_pregunta3 = 0; }

    // Obtiene el valor del elemento con ID "quemadura", lo convierte a un número entero y lo almacena en `v_pregunta4`.
    let v_pregunta4 = parseInt(document.getElementById("quemadura").value);

    // Obtiene el valor del elemento con ID "edad", lo convierte a un número entero y lo almacena en `v_pregunta5`.
    let v_pregunta5 = parseInt(document.getElementById("edad").value);

    // Obtiene el valor del elemento con ID "bloqueador", lo convierte a un número entero y lo almacena en `v_pregunta6`.
    let v_pregunta6 = parseInt(document.getElementById("bloqueador").value);

    // Obtiene el elemento del DOM con el ID "rango_riesgo" y lo almacena en la variable `resultado_rango`.
    const resultado_rango = document.getElementById("rango_riesgo");

    // Obtiene el texto contenido en el elemento `indiceText`, lo convierte a un número entero y lo almacena en `indice`.
    const indice = parseInt(indiceText.innerText);

    // Suma los valores de todas las preguntas y almacena el resultado en `total_form`.
    let total_form = v_pregunta1 + v_pregunta2 + v_pregunta3 + v_pregunta4 + v_pregunta5 + v_pregunta6;

    // Declara una variable `color` para almacenar el color que se asignará más adelante.
    let color = "";

    // Declara una variable `fontSize` para almacenar el tamaño de la fuente que se asignará más adelante.
    let fontSize = "85px";

    // Calcula el valor de riesgo (`v_riesgo`) basado en la fórmula proporcionada.
    v_riesgo = (total_form / 12) * (indice / 10) * 10;

    // Evalúa el valor de `v_riesgo` y asigna un texto y un color según el rango en el que caiga.
    if (v_riesgo <= 2) {
        resultado_rango.innerText = "Riesgo Bajo";
        color = "#13ba0074";  // Color verde claro.
    }
    else if (v_riesgo <= 4) {
        resultado_rango.innerText = "Riesgo Moderado";
        color = "#fff836f6";  // Color amarillo.
    }
    else if (v_riesgo <= 6) {
        resultado_rango.innerText = "Riesgo Alto";
        color = "#fb9a4b74";  // Color naranja claro.
    }
    else if (v_riesgo <= 8) {
        resultado_rango.innerText = "Riesgo Muy alto";
        color = "#ff626274";  // Color rojo claro.
    }
    else if (v_riesgo > 8) {
        resultado_rango.innerText = "Riesgo Extremo";
        color = "#a94bfb74";  // Color morado claro.
    }

    // Itera sobre cada elemento en la NodeList `signo`.
    signo.forEach(signo => {
        // Cambia el color de cada elemento `signo` al valor almacenado en `color`.
        signo.style.color = color;

        // Cambia el tamaño de la fuente de cada elemento `signo` al valor almacenado en `fontSize`.
        signo.style.fontSize = fontSize;
    });
});
