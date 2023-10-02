package exercice2;

import java.text.DecimalFormat;

public class Test {
	public static void main(String[] args) {
//		v1 = < 3.0, 2.0, 5.0 >
//		Norme de v1 = 6,16
//		v2 = < 1.0, 2.0, 3.0 >
//		Norme de v2 = 3,74
//		v1 + v2 = < 4.0, 4.0, 8.0 >
//		v1.v2 = 22.0
		DecimalFormat df=new DecimalFormat("#0.00");
	
		Vecteur3D v1 = new Vecteur3D(3.0, 2.0, 5.0);
		Vecteur3D v2 = new Vecteur3D(1.0, 2.0, 3.0);
		
		System.out.println(v1);
		System.out.println("Norme de v1 = "+df.format(v1.norme()) );
		System.out.println(v2);
		System.out.println("Norme de v1 = "+df.format(v2.norme()) );
		System.out.println("v1 . v2 = "+ df.format( Vecteur3D.produitScalaire(v1,v2)));
		
		
		
	}
}
