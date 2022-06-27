public class Ejercicios09 {

    public static void main (String[] args) {
        Cliente cliente1 = new Cliente();
        
        System.out.println("Edad: " + cliente1.edad);
        System.out.println("Nombre: " + cliente1.nombre);
        System.out.println("Telefono: " + cliente1.telefono);
    }
}

class Persona{
    int edad = 29;
    String nombre = "Filomena";
    int telefono = 666666666;
    }

class Cliente extends Persona {
    int credito;
    }

class Trabajador extends Cliente {
    float salario;
    }