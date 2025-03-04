// Agrega un event listener que se ejecuta cuando el contenido del DOM ha sido completamente cargado y parseado.
document.addEventListener("DOMContentLoaded", function () {

    // Obtiene el elemento del DOM con el ID "ante_propio" y lo almacena en la variable `pregunta2`.
    const pregunta2 = document.getElementById("ante_propio");

    // Obtiene el elemento del DOM con el ID "pregunta3" y lo almacena en la variable `pregunta3`.
    const pregunta3 = document.getElementById("pregunta3");

    // Agrega un event listener al elemento `pregunta2` para escuchar el evento "change" (cambio de valor).
    pregunta2.addEventListener("change", function () {

        // Verifica si el valor seleccionado en `pregunta2` es "0".
        if (pregunta2.value === "0") {
            // Si el valor es "0", remueve la clase "ocultar_P3" del elemento `pregunta3`.
            pregunta3.classList.remove("ocultar_P3");
        } else {
            // Si el valor no es "0", añade la clase "ocultar_P3" al elemento `pregunta3`.
            pregunta3.classList.add("ocultar_P3");
        }
    });
});
