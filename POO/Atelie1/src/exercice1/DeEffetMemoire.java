package exercice1;
import java.util.Random;

public class DeEffetMemoire extends De {
    private static int lastValue = -1;
    private Random random = new Random();

    
    // Constructure
    public DeEffetMemoire(String name, int nbFaces) {super(name, nbFaces);}
    public DeEffetMemoire(String name) {super(name);}
    public DeEffetMemoire(int nbFaces) {super(nbFaces);}
    public DeEffetMemoire() {super();}
    

    @Override
    public int lancer() {
        int result;
        do {
            result = random.nextInt(getNbFaces()) + 1;
        } while (result == lastValue);
        lastValue = result;
        return result;
    }
}