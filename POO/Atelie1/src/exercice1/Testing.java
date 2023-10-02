package exercice1;

public class Testing {
    public static void main(String[] args) {
        de de1 = new de();
        de de2 = new de("My Custom Die");
        de de3 = new de(12);
        de de4 = new de("Another Die", 20);
        de de5 = new de("Another Die", 20);

        // Get and print the number of faces of each die
        System.out.println(de1);
        System.out.println(de2);
        System.out.println(de3);
        System.out.println(de4);

        // Roll the dice and print the results
        System.out.println("Rolling " + de1.getName() + ": " + de1.lancer());
        System.out.println("Rolling " + de2.getName() + ": " + de2.lancer());
        System.out.println("Rolling " + de3.getName() + ": " + de3.lancer());
        System.out.println("Rolling " + de4.getName() + ": " + de4.lancer());

        // Roll multiple times and print the maximum result
        int numRolls = 5;
        System.out.println("Rolling " + de1.getName() + " " + numRolls + " times, maximum result: " + de1.lancer(numRolls));
        System.out.println("Rolling " + de2.getName() + " " + numRolls + " times, maximum result: " + de2.lancer(numRolls));
        System.out.println("Rolling " + de3.getName() + " " + numRolls + " times, maximum result: " + de3.lancer(numRolls));
        System.out.println("Rolling " + de4.getName() + " " + numRolls + " times, maximum result: " + de4.lancer(numRolls));

        // Print the total number of dice created
        System.out.println("Total number of dice created: " + de1.getNbDe());
        
        
        
     
        boolean t1 = de1.equals(de2);
        System.out.println("de1 ?= de2: " + t1);

        boolean t2 = de1.equals(de3);
        System.out.println("de1 ?= de3: " + t2);
        
        boolean t3 = de4.equals(de5);
        System.out.println("de4 ?= de5: " + t3);
        
        
        
        
        
        DePipe dePipedValid = new DePipe("Dé pipé valide", 6, 3);

        // Test with an invalid minValue
        DePipe dePipedInvalid = new DePipe("Dé pipé invalide", 6, 10);

        // Test the lancer method of a valid DePipe
        System.out.println("Testing DePipe with valid minValue:");
        for (int i = 0; i < 10; i++) {
            int result = dePipedValid.lancer();
            System.out.println("Lancer " + (i + 1) + ": " + result);
        }

        // Test the lancer method of an invalid DePipe
        System.out.println("\nTesting DePipe with invalid minValue:");
        for (int i = 0; i < 10; i++) {
            int result = dePipedInvalid.lancer();
            System.out.println("Lancer " + (i + 1) + ": " + result);
        }
        
        


        DeEffetMemoire deMemoire = new DeEffetMemoire("Dé à effet mémoire", 6);

        System.out.println("Rolling the memory-effect die:");
        for (int i = 0; i < 10; i++) {
            int result = deMemoire.lancer();
            System.out.println("Roll " + (i + 1) + ": " + result);
        }

    
    
    
    }
}
