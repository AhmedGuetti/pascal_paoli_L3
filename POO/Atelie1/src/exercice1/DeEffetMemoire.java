package exercice1;
import java.util.Random;

public class DeEffetMemoire extends de {
    private static int lastValue = -1;
    private final Random random = new Random();

    public DeEffetMemoire(String name, int nbFaces) {
        super(name, nbFaces);
    }

    @Override
    public int lancer() {
        int result;
        do {
            result = random.nextInt(getNbFaces()) + 1; // Generate a random value between 1 and nbFaces
        } while (result == lastValue);
        lastValue = result;
        return result;
    }
}