/**
   This program demonstrates a solution to the
   Morse Code programming challenge.
   * 
   * Student Name: Michael Palmer
   * Date: 12/4/2013
   * 
*/
// import the swing and ArrayList modules
import javax.swing.JOptionPane;
import java.util.ArrayList;


public class MorseCode {
    // begin main class
    public static void main(String[] args) {
        
        // a string array to hold all of the Morse Code values
        String[] morseCode = {" ", "--..--", ".-.-.-", "..--..", "-----",
            ".----", "..---", "...---", "....-", ".....", "-....", "--...",
            "---..", "----.", ".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
            "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", 
            "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", 
            "--.."};
        // a string of english letter, numbers and punctuation that 
        // corresponds to the Morse Code list
        String english = " ,.?0123456789abcdefghijklmnopqrstuvwxyz";
        // turn that english string into an array of characters
        // this will allow us to iterate over it
        char[] englishArray = english.toCharArray();
        
        // make an ArrayList to hold our index values as we find them.
        // also initialize a StringBuilder object that will help us in
        // printing out a clean string of morse code values
        ArrayList<Integer> holdList = new ArrayList<>();
        StringBuilder holdBuilder = new StringBuilder();
        //user message
        JOptionPane.showMessageDialog(null, "This program will convert your "
                + "sentence into Morse Code.", "Morse Code Converter", 
                + JOptionPane.INFORMATION_MESSAGE);
        // user input, convert to lowercase for simplicity
        String userUp = JOptionPane.showInputDialog("Enter a "
                + "sentence: ");
        String userString = userUp.toLowerCase();
        // convert the input to a character array. This will
        // allow iteration
        char[] userArray = userString.toCharArray();
        // loop through each character in the userArray, and match
        // them up with values in the array of english characters.
        // save the index value of the english array
        for(int i = 0; i < userArray.length; i++) {
            for(int n = 0; n < englishArray.length; n++) {
                if(userArray[i] == englishArray[n]) {
                    holdList.add(n);
                }
            }
        }
        // print out the message: first append all morse codes associated
        // with the english array indexes to the StringBuilder object.
        // Then convert that object to a string and print it out.
        for(int i = 0; i < holdList.size(); i++) {
            holdBuilder.append(morseCode[holdList.get(i)]);
        }
        String moCode = holdBuilder.toString();
        JOptionPane.showMessageDialog(null, "This is your sentence in morse "
                + "code: \n" + moCode + "\n", "Morse Code", 
                JOptionPane.INFORMATION_MESSAGE);
    }// end main method
}
