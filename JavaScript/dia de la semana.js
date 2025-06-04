let dia = 3;
let nombredia;

switch (dia) {
    case 1:
        nombredia = "Lunes";
        break;
    case 2:
        nombredia = "Martes";
        break;
    case 3:
        nombredia = "Miércoles";
        break;
    case 4:
        nombredia = "Jueves";
        break;
    case 5:
        nombredia = "Viernes";
        break;
    case 6:
        nombredia = "Sábado";
        break;
    case 7:
        nombredia = "Domingo";
        break;
    default:
        nombredia = "Día inválido";
}
console.log("El día de la semana es: " + nombredia);
// Output: El día de la semana es: Miércoles