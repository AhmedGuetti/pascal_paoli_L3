package exercice1;
import java.util.Random;

public class DeDiffNames<T> extends De {
    private static Random r = new Random();
    private T[] namesFaces;

   
	public DeDiffNames(String name, int nbFaces) {
        super(name, nbFaces);
    }

    public DeDiffNames(int nbFaces) {
        super(nbFaces);
    }

    public DeDiffNames(String name) {
        super(name);
    }

    public void setNamesFaces(T[] names) {
        if (names.length != super.getNbFaces()) {
        	System.err.println("[ERROR]: le nombre des noms doit etre eguale le nombre des faces ");
        }
        this.namesFaces = names;
    }

    public T lancerDiff() {
        int nbAleatoire = r.nextInt(super.getNbFaces());
        return namesFaces[nbAleatoire];
    }

    public T lancerDiff(int nb) {
        int res = super.lancer();
        int temp;
        for (int i = 0; i < nb - 1; ++i) {
            temp = super.lancer();
            if (res < temp) {
                res = temp;
            }
        }
        return namesFaces[res];
    }
}
