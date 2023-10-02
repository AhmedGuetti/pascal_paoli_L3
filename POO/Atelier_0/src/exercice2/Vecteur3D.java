package exercice2;

import java.lang.Math;

public class Vecteur3D {
	private double x;
	private double y;
	private double z;
	
	
	public Vecteur3D(double x, double y, double z) {
		this.x = x;
		this.y = y;
		this.z = z;
	}
	public Vecteur3D() {
		// this.x = this.y = this.z = 0;
		this(0,0,0);
	}

	
	@Override
	public String toString() {
		return "<"+x+", "+y+", "+z+">";
	}
	public double norme() {
		return  Math.sqrt(Math.pow(x, 2)+Math.pow(y, 2)+Math.pow(z, 2));
	}
	public double produitScalaire(Vecteur3D vect2) {
		return this.x*vect2.x + this.y*vect2.y + this.z*vect2.z;
	}
	public Vecteur3D some(Vecteur3D v) {
		return new Vecteur3D(this.x+v.x, this.y+v.y, this.z+v.z);
	}
	
	public static double produitScalaire(Vecteur3D v1, Vecteur3D v2) {
		return v1.x*v2.x + v1.y*v2.y + v1.z*v2.z;
	}
	
	public static Vecteur3D some(Vecteur3D v1, Vecteur3D v2) {
		return new Vecteur3D(v1.x+v2.x, v1.y+v2.y, v1.z+v2.z);
	}
	
	
	
	
}
