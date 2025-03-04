document.querySelectorAll("option").forEach(select => {
    select.addEventListener("mouseover", function () {
        this.style.backgroundColor = "#8237c3";
        this.style.color = "white";
    });

    select.addEventListener("mouseout", function () {
        this.style.backgroundColor = ""; // Restaura el color original
        this.style.color = ""; // Restaura el color original
    });
});
