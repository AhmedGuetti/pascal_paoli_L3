package exercice2;

import exercice1.de;

public class Entier {
    private final int inf;
    private final int sup;
    private int valeur;

    public Entier(int inf, int sup) {
        this.inf = inf;
        this.sup = sup;
        this.valeur = 0; 
    }

    public Entier(int inf, int sup, int valeurInitiale) {
        this.inf = inf;
        this.sup = sup;
        setValeur(valeurInitiale);
    }

    
    	// SETTER
    public int getValeur() {return valeur;}
    public int getBorneMax() {return this.sup;}
	public int getBorneMin() {return this.inf;}
    public void setValeur(int nouvelleValeur) {
        if (nouvelleValeur >= inf && nouvelleValeur <= sup) {
            valeur = nouvelleValeur;
        } else {
            System.err.println("[ERROR]: La valeur est hors des bornes.");
        }
    }

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
        if (this == obj) {
            return true;
        }

        if (!(obj instanceof Entier)) {
            return false;
        }
        Entier entier = (Entier) obj;
        return valeur == entier.valeur && 
        		inf == entier.inf && 
        		sup == entier.sup;
    }
    
    
}