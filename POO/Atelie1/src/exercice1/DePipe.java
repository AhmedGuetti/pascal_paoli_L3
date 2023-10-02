package exercice1;

public class DePipe extends de {
    private final int minValue;

    public DePipe(String name, int nbFaces, int minValue) {
        super(name, nbFaces);
        if (minValue < 1 || minValue > nbFaces) {
            System.err.println("Erreur : La valeur minimale doit être comprise entre 1 et le nombre de faces.");
            minValue = 1;
        }
        this.minValue = minValue;
    }

    @Override
    public int lancer() {
        int result;
        do {
            result = super.lancer();
        } while (result <= minValue);
        return result;
    }
}