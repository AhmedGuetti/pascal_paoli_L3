package exercice2;

import java.util.Random;

public class EntierFou extends Entier {
    private int niveauDeFolie;
    private Random random = new Random();

    public EntierFou(int borneMin, int borneMax, int niveauDeFolie) {
        super(borneMin, borneMax);
        this.niveauDeFolie = niveauDeFolie;
    }

    public EntierFou(int borneMin, int borneMax, int valeurInitiale, int niveauDeFolie) {
        super(borneMin, borneMax, valeurInitiale);
        this.niveauDeFolie = niveauDeFolie;
    }

    public void incrementer() {
        int increment = random.nextInt(niveauDeFolie + 1);
        int nouvelleValeur = getValeur() + increment;
        if (nouvelleValeur >= getBorneMin() && nouvelleValeur <= getBorneMax()) {
            setValeur(nouvelleValeur);
        } else {
            System.err.println("Erreur : L'incrémentation dépasse les bornes.");
        }
    }



	@Override
    public String toString() {
        return "Valeur: " + getValeur() + ", Niveau de Folie: " + niveauDeFolie;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (!(obj instanceof Entier)) {
            return false;
        }
        EntierFou entierFou = (EntierFou) obj;
        return getValeur() == entierFou.getValeur()
                && getBorneMin() == entierFou.getBorneMin()
                && getBorneMax() == entierFou.getBorneMax()
                && niveauDeFolie == entierFou.niveauDeFolie;
    }
}