function validar(contraseña) {
    if (contraseña.value.length<=6) {
        alert("por favor digita más de 6 carácteres")
        bolean=0
        window.location.href = "http://127.0.0.1:5000/registro";
    }
}