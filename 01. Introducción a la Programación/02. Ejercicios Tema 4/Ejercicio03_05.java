public class Ejercicio03_05 {
    public static void main(String[] args) {
        var estacion = "OTOÑO";


        switch (estacion){
            case "PRIMAVERA":
                System.out.println("Estacion: Primavera");
                break;
            case "VERANO":
                System.out.println("Estacion: Verano");
                break;
            case "OTOÑO":
                System.out.println("Estacion: Otoño");
                break;
            case "INVIERNO":
                System.out.println("Estacion: Invierno");
                break;
            default:
                System.out.println("Estacion: NOT FOUND 404");
        }

    }
}
