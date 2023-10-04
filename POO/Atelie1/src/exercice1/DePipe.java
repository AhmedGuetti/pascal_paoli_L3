package exercice1;

public class DePipe extends De {
    private final int minValue;
    
    // Constructures
    public DePipe(String name, int nbFaces, int minValue) {
        super(name, nbFaces);
        if (minValue < 1 || minValue > nbFaces) {
            System.err.println("[ERROR] : La valeur minimale doit être comprise entre 1 et le nombre de faces.");
            minValue = 1;
        }
        this.minValue = minValue;
    }
    public DePipe(String name, int minValue) {this(name, 6,minValue);}
    public DePipe(int nbFaces, int minValue) {this("De n°"+i, nbFaces,minValue);}
    public DePipe(int minValue) {this("De n°"+i, 6,minValue);}
    
    
    
    @Override
    public int lancer() {
        int result;
        do {
            result = super.lancer();
        } while (result <= minValue);
        return result;
    }
}