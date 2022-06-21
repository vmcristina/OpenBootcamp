public class Ejercicio02 {

    public static void main(String[] args) {
        Coche miCoche = new Coche();
        miCoche.sumarpuertas();
        System.out.println(miCoche.puertas);
    }

}

class Coche {
    public int puertas = 1;

    public void sumarpuertas() {
        this.puertas++;
    }
}