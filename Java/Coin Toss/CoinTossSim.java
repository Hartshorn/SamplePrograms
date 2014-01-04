/*
 * This program demonstrates a solution to the
 * Coin Toss Simulator Challenge from pg 404 #12.
 * This part of the problem is required to finish
 * the second (assigned) problem on pg 405 #13.
 * 
 * Student Name: Michael Palmer
 * Date: 11/17/2013
 * 
 * 
*/

// import the random number module
import java.util.Random;
// declare the public class CoinTossSim; this will
// allow us to create objects of this class.
public class CoinTossSim {
    // declare private variables (scope only within
    // this class)
    private String sideUp;
    private double randBig;
    private double randSm;
    // constructor method; takes no parameters, but 
    // will assign a random side up (heads or tails)
    // initially. Use this to create a new CoinTossSim object.
    public CoinTossSim() {
        Random rand = new Random();
        randBig = rand.nextInt(100) + 1;
        randSm = (randBig / 100);
        
        if(randSm <= 0.5) {
            this.sideUp = "Heads";
        }
        else {
            this.sideUp = "Tails";
        }
    }
    // Toss method will flip the coin and reset the
    // side up value randomly. Use this to flip the
    // coin.
    public void Toss() {
        Random rand = new Random();
        randBig = rand.nextInt(100) + 1;
        randSm = (randBig / 100);
        
        if(randSm <= 0.5) {
            this.sideUp = "Heads";
        }
        else {
            this.sideUp = "Tails";
        }
    }
    // getter: returns the current side up.
    public String getSideUp() {
        return sideUp;
    }
    // setter: sets the side up when given a string
    // as a parameter.
    public void setSideUp(String sideUp) {
        this.sideUp = sideUp;
    }
    
} // end CoinTossSim class definition
