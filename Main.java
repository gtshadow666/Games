import java.util.Random;
import java.util.Scanner;

// Clase principal del juego
class JuegoAdivinar {
    private int numeroSecreto;
    private int intentos;
    private boolean adivinado;

    // Constructor
    public JuegoAdivinar(int maxNumero) {
        Random random = new Random();
        this.numeroSecreto = random.nextInt(maxNumero) + 1; // Número entre 1 y maxNumero
        this.intentos = 0;
        this.adivinado = false;
    }

    // Método para jugar
    public void jugar() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("¡Bienvenido al juego de adivinar el número!");
        System.out.println("Estoy pensando en un número entre 1 y 100. ¡Intenta adivinarlo!");

        while (!adivinado) {
            System.out.print("Introduce tu intento: ");
            int intentoUsuario = scanner.nextInt();
            intentos++;

            if (intentoUsuario == numeroSecreto) {
                System.out.println("¡Felicidades! Has adivinado el número en " + intentos + " intentos.");
                adivinado = true;
            } else if (intentoUsuario < numeroSecreto) {
                System.out.println("El número es mayor. Intenta de nuevo.");
            } else {
                System.out.println("El número es menor. Intenta de nuevo.");
            }
        }

        scanner.close();
    }
}

// Clase Main para ejecutar el juego
public class Main {
    public static void main(String[] args) {
        JuegoAdivinar juego = new JuegoAdivinar(100); // Número máximo 100
        juego.jugar();
    }
}
