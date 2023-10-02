package exercice1;


enum Orientation{
	NORD, 
	SUD, 
	EST, 
	OUEST
};


class Robot {
	private String ref;
	private String name;
	private int x;
	private int y;
	private Orientation ori;
	private static int count;
	
	
	public Robot(String name, int x, int y, Orientation ori) throws Exception{
		if (x < 0 || y < 0) {
			 throw new Exception("[ERROR]: coordone invalid (x,y) doit etre les deux positif");
		}
		this.name = name;
		this.x = x;
		this.y = y;
		this.ori = ori;
		this.ref = "ROB"+count;
		count++;
	}
	
	
	
	public Robot(String name) throws Exception{
		this(name,0,0,Orientation.NORD);
//		this.name = name;
//		this.x = 0;
//		this.y = 0;
//		this.ori = Orientation.NORD;
//		this.ref = "ROB"+count;
//		count++;
	}



	
	public void changeOrientation(int newOrientaion) {
		switch (newOrientaion) {
			case 1:
				this.ori = Orientation.NORD;
				break;
			case 2:
				this.ori = Orientation.EST;
				break;
			case 3:
				this.ori = Orientation.SUD;
				break;
			case 4:
				this.ori = Orientation.OUEST;
				break;
		}
	}
	
	public void avance() {
		if (this.ori == Orientation.EST || this.ori == Orientation.OUEST) {
			++x;
		} 
		else{
			++y;
		} 	
	}
	
	
	public void deplacer() {
		switch (this.ori) {
		case NORD:
			++y;
			break;
		case EST:
			++x;
			break;
		case SUD:
			if (y > 0) {
				--y;
			}
			break;
		case OUEST:
			if (x>0) {
				--x;
			}
			break;
		}
	}
	
	public void afficheToi() {
		System.out.println("[Ref]: "+this.ref+"\nname: "+this.name+"\nx: "+this.x+"	y: "+this.y+"\norientaion: "+this.ori.name());
	}
	
	public void afficheToi_v2() {
		System.out.println(this);
	}
	
	
	@Override
	public String toString(){
		return "================= "+this.ref+"____"+this.name+" ================= "
				+ "\nx: "+ x
				+ "\ny: "+ y 
				+ "\nOrientation: "+this.ori.name();
//				+"\n================================================= ";
	}
	
}
