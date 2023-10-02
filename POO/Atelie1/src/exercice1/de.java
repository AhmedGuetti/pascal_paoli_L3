package exercice1;

import java.util.*;



public class de {
	private String name;
	private int nbFaces;
	private static int i = 0;
	private static Random r = new Random();
	
	public de() {
		this("De n°"+i, 6);
		++i;
	}
	public de(String name) {
		this(name, 6);
		++i;
	}
	public de(int nbFaces) {
		this("De n°"+i, nbFaces);
		++i;
	}
	public de(String name, int nbFaces){
		this.name = name;
		setNbFaces(nbFaces);
		++i;
	}
	
	int getNbFaces() {
		return this.nbFaces;
	}
	
	String getName() {
		return this.name;
	}
	
	void setNbFaces(int nbFaces) {
        if (nbFaces >= 3 && nbFaces <= 120) {
            this.nbFaces = nbFaces;
        } else {
            System.err.println("Erreur : Le nombre de faces doit être compris entre 3 et 120.");
        }
	}
	
	public int lancer() {
		int nbAleatoire= r.nextInt(this.nbFaces) ;
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
		return "nom: "+this.name+"/========/nbFaces: "+this.nbFaces;
	}
	
	// GeekforGeeks
	@Override
    public boolean equals(Object o) {
        if (o == this) {
            return true;
        }
        if (!(o instanceof de)) {
            return false;
        }
        de c = (de) o;
        // Compare the data members and return accordingly
        return c.name == this.name
                && c.nbFaces == this.nbFaces;
    }
	
}
