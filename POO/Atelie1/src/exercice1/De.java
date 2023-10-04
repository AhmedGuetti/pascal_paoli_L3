package exercice1;

import java.util.*;



public class De {
	private final String name;
	private int nbFaces;
	private static int i = 0;
	private static Random r = new Random();
	

	public De(String name, int nbFaces){
		this.name = name;
		setNbFaces(nbFaces);
		++i;
	}
	
	public De() {
		this("De n°"+i, 6);
	}
	public De(String name) {
		this(name, 6);
	}
	public De(int nbFaces) {
		this("De n°"+i, nbFaces);
	}
	
	public int getNbFaces() {
		return this.nbFaces;
	}
	
	public String getName() {
		return this.name;
	}
	
	public void setNbFaces(int nbFaces) {
        if (nbFaces >= 3 && nbFaces <= 120) {
            this.nbFaces = nbFaces;
        } else {
            System.err.println("Erreur : Le nombre de faces doit être compris entre 3 et 120.");
        }
	}
	
	public int lancer() {
		int nbAleatoire= r.nextInt(this.nbFaces) +1;
		return nbAleatoire;	
	}
	
	public int lancer(int nb) {
		int res=this.lancer(), temp;
		for(int i=0; i < nb-1 ; ++i) {
			temp = this.lancer();
			if(res < temp) {
				res = temp;
			}
		}
		return res;
	}
	
	public int getNbDe() {
		return i;
	}
	
	@Override
	public String toString() {
		return "nom: "+this.name+"\nnbFaces: "+this.nbFaces+"\n";
	}
	
	// GeekforGeeks
	@Override
    public boolean equals(Object o) {
        if (!(o instanceof De) || o == null) { // o,getClass() != this,getClass()
            return false;
        }
        if (o == this) {
            return true;
        }
        De c = (De) o;
        return ((c.name.equals(this.name))
                && (c.nbFaces == this.nbFaces));
    }
	
}
