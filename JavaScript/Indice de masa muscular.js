let peso = prompt("Ingrese su peso en kg: ");
let altura = prompt("Ingrese su altura en metros: ");
let imc = peso / (altura * altura);

if (imc < 18.5) {
    console.log("Bajo peso");
}else if (imc >= 18.5 && imc < 24.9) {
    console.log("Peso normal");
}else if (imc <= 24.9 && imc < 29.9) {
    console.log("Sobrepeso");
}else {
    console.log("obesidad");
}
