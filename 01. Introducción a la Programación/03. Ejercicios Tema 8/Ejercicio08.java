public class Ejercicio08 {

    public static void main(String[] args) {
        Persona persona1 = new Persona();

        persona1.setEdad(24);
        System.out.println(" Edad: " + persona1.getEdad());

        persona1.setNombre("Aurora");
        System.out.println("Nombre: " + persona1.getNombre());

        persona1.setNumeroTelefono(666666666);
        System.out.println("Numero telefono: " + persona1.getNumeroTelefono());
    }
}

class Persona {
    private int edad;
    private String nombre;
    private int numeroTelefono;


    public void setEdad (int edad) {
        this.edad = edad;
    }
    public int getEdad(){
        return this.edad;
    }


    public void setNombre (String nombre){
        this.nombre = nombre;
    }
    public String getNombre(){
        return this.nombre;
    }

    public void setNumeroTelefono (int telefono){
        this.numeroTelefono = telefono;
    }
    public int getNumeroTelefono () {
        return this.numeroTelefono;
    }
}