package exercice2;

public class Entier {
    private final int inf;
    private final int sup;
    private int valeur;
    

    public Entier(int inf, int sup, int valeurInitiale) {
        this.inf = inf;
        this.sup = sup;
        setValeur(valeurInitiale);
    }

    public Entier(int inf, int sup) {
        this(inf, sup, 0);
    }

    // Getter
    public int getValeur() {return valeur;}
    public int getBorneMax() {return this.sup;}
	public int getBorneMin() {return this.inf;}
	
	// Setter
    public void setValeur(int nouvelleValeur) {
        if (nouvelleValeur >= inf && nouvelleValeur <= sup) {
            valeur = nouvelleValeur;
        } else {
            System.err.println("[ERROR]: La valeur est hors des bornes.");
        }
    }

    // Methodes 
    public void incrementer(int pas) {
        int nvaleur = valeur + pas;
        if (nvaleur >= inf && nvaleur <= sup) {
            valeur = nvaleur;
        } else {
            System.err.println("Erreur : L'incrémentation dépasse les bornes.");
        }
    }
    
    public void incrementer() {
        incrementer(1); 
    }
    
    @Override
    public String toString() {
        return Integer.toString(valeur);
    }

    // GeekforGeeks
    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof Entier) || obj == null)
            return false;
        if (this == obj) 
            return true;
        Entier entier = (Entier) obj;
        return valeur == entier.valeur && 
        		inf == entier.inf && 
        		sup == entier.sup;
    }
    
    
}