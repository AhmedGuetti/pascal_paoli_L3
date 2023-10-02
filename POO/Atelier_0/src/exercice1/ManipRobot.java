package exercice1;

public class ManipRobot {
	public static void main(String[] args) {
		try {
			Robot Rb1 = new Robot("Alex");
			System.out.println(Rb1);
			Rb1.avance();
			System.out.println(Rb1);
			Rb1.changeOrientation(4);
			Rb1.avance();
			System.out.println(Rb1);
			Rb1.avance();
			System.out.println(Rb1);
			// Rb1.afficheToi_v2();
			
		} catch (Exception e) {
			e.printStackTrace();
		}
		
		try {
			Robot Rb2 = new Robot("Sarah", 10,20,Orientation.SUD);
			System.out.println(Rb2);
			Rb2.avance();
			System.out.println(Rb2);
			Rb2.changeOrientation(1);
			Rb2.avance();
			System.out.println(Rb2);
			Rb2.avance();
			System.out.println(Rb2);
			// Rb2.afficheToi_v2();
			
		} catch (Exception e) {
			e.printStackTrace();
		}
		
	}
}
