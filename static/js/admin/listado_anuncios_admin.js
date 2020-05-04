function mostrarAnuncio(){
    comercial = document.getElementById("select_comercials").value
    valid = document.getElementById("anuncios_validados")
    not_valid = document.getElementById("anuncios_no_validados")

    if (comercial == "validado" ){
        valid.style.display = "block";
        not_valid.style.display = "none";
    }
    else if (comercial == "no_validado" ){
        valid.style.display = "none";
        not_valid.style.display = "block";
    }
    else {
        valid.style.display = "none";
        not_valid.style.display = "none";
    }
}
window.onload = function(){mostrarAnuncio()};

