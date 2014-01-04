/*
 * This program demonstrates the solution
 * to the Tossing Coins For A Dollar challenge
 * pg 405 #13.
 * 
 * Student Name: Michael Palmer
 * Date: 11/17/2013
 */
// the point of this exercise is to use the class we created in the 
// previous exercise to make objects of that class. We can then get
// information about these objects (their heads or tails state) using
// the built-in methods we created.

public class CoinMoney {
    
    // main method
    public static void main(String[] args) {
        
        // declare a double to hold the running balance
        // each time the game is played
        
        double balance = 0;
        
        // create three new objects of the CoinTossSim class.
        // These will be flipped to play the game.
        
        CoinTossSim nickel = new CoinTossSim();
        CoinTossSim dime = new CoinTossSim();
        CoinTossSim quarter = new CoinTossSim();
        
        // this while loop is the game. Each loop will flip all three coins
        // and add their balance if the side up is Heads, otherwise it will
        // do nothing. It ends when the balance is or exceeds 1.00.
        
        while(balance <= 1.00) {
            nickel.Toss();
            dime.Toss();
            quarter.Toss();
            if(nickel.getSideUp().equals("Heads")) {
                balance += 0.05;
            }
            if(dime.getSideUp().equals("Heads")) {
                balance += 0.10;
            }
            if(quarter.getSideUp().equals("Heads")) {
                balance += 0.25;
            }
            
            // after each loop, print out the running total.
            
            System.out.printf("Running total: %.2f\n", balance);
        }
        
        // once the game ends, get the balance and print out win
        // or lose statements.
        
        if(balance == 1.0) {
            System.out.println("You Win The Game!");
        }
        else {
            System.out.println("You Lose.");
        }
    }
}
