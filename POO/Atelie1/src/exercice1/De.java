package exercice1;

import java.util.*;



public class De {
	protected static int i = 0;
	protected final static int DEFAULT_VALUE_FACES = 6;
	protected final static int MIN_VALUE_FACES = 3;
	protected final static int MAX_VALUE_FACES = 120;

	private final String name;
	private int nbFaces;
	private static Random r = new Random();
	
	
	// Constructures
	public De(String name, int nbFaces){
		this.name = name;
		setNbFaces(nbFaces);
		++i;
		
	}
	public De() {this("De n°"+i, DEFAULT_VALUE_FACES);}
	public De(String name) {this(name, DEFAULT_VALUE_FACES);}
	public De(int nbFaces) {this("De n°"+i, nbFaces);}
	
	// Getter
	public int getNbFaces() {return this.nbFaces;}
	public String getName() {return this.name;}
	public int getNbDe() {return i;}
	
	
	// Setter
	public void setNbFaces(int nbFaces) {
        if (nbFaces >= MIN_VALUE_FACES && nbFaces <= MAX_VALUE_FACES) 
            this.nbFaces = nbFaces;
        else 
            System.err.println("Erreur : Le nombre de faces doit être compris entre 3 et 120.");
        
	}
	
	
	// Methodes
	public int lancer() {
		int nbAleatoire= r.nextInt(this.nbFaces) +1;
		return nbAleatoire;	
	}
	
	public int lancer(int nb) {
		int res=this.lancer(), temp;
		for(int i=0; i < nb-1 ; ++i) {
			temp = this.lancer();
			if(res < temp) 
				res = temp;
		}
		return res;
	}
	

	@Override
	public String toString() {
		return "nom: "+this.name+"\nnbFaces: "+this.nbFaces+"\n";
	}
	 
	// GeekforGeeks
	@Override
    public boolean equals(Object o) {
        if (!(o instanceof De) || o == null) // o.getClass() != this,getClass()
            return false;
        if (o == this) 
            return true;
        De c = (De) o;
        return ((c.name.equals(this.name))
                && (c.nbFaces == this.nbFaces));
    }
	
}
