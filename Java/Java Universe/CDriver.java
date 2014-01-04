/*
 */
import java.util.ArrayList;
import javax.swing.JOptionPane;

public class CDriver {
    // main method informs user, and runs all other methods.
    public static void main(String[] args) {

        // create an arrayList to hold the universe
        // and an int array to hold each planet's position;
        // this will work with the horoscope, which is dependent
        // on each planets position.
        
        ArrayList<Object> universe = new ArrayList<>();
        double[] position = new double[8];
        String horoscope;
        // user message
        JOptionPane.showMessageDialog(null, "This program will create a "
                + "solar system.\nPlease enter planet names, or hit ENTER "
                + "for default.\n", "Build Your Own Universe", 
                JOptionPane.INFORMATION_MESSAGE);
        // all work done here
        createUniverse(universe);
        getInfo(universe);
        getArray(position, universe);
        horoscope = getHoroscope(position);
        JOptionPane.showMessageDialog(null, horoscope, "Your Horoscope", 
                    JOptionPane.INFORMATION_MESSAGE);
    } // end main method
    
    // this method will create a user defined universe, allowing for
    // default inputs if none are given. The default solar system is
    // similar to our own.
    public static void createUniverse(ArrayList<Object> arrayList) {
        
        int iterator = 0;
        int count = 0;
        int distance = 1;
        String name;
        
        String[] planetNames = {"Mercury", "Venus", "Earth", "Mars", 
            "Jupiter", "Saturn", "Uranus", "Neptune"};
        
        Double[] planetRadius = {2.439e6, 6.051e6, 6.378e6, 3.397e6, 
            7.149e7, 6.027e7, 2.556e7, 2.477e7};
        
        Double[] planetMass = {3.32e23, 4.896e24, 5.974e24, 6.419e23, 
            1.899e27, 5.685e26, 8.685e25, 1.02e26};
        
        
        while(count < 8) {
            
            CelestialBody planet = new CelestialBody();

            name = JOptionPane.showInputDialog(null, "Enter the name of a "
                    + "planet: ", "Planet Names", 
                    JOptionPane.QUESTION_MESSAGE);
            
            if(name.isEmpty()) {
                planet.setPlanetName(planetNames[iterator]);
            }
            else if(name.length() == 0) {
                System.exit(0);
            }
            else {
                planet.setPlanetName(name);
            }
            
            planet.setRadius(planetRadius[iterator]);
            planet.setMass(planetMass[iterator]);
            planet.calcPosition();
            planet.calcDensity();
            planet.calcVolume();
            planet.calcGravity();
            planet.setDistance(distance);

            iterator++;
            distance ++;
            count++;
            
            arrayList.add(planet);
        }
        
    } // end createUniverse method
    
    // this array will pull information about each of the celestial
    // bodies that have been created. It uses a uniquely created 
    // object holding the chosen arrayList items information.
    // This allows the user to pull information from each different
    // planet.
    public static void getInfo(ArrayList<Object> arrayList) {
        
        int choice;
        
        String choiceStr;
        String choiceLow;
        
        Boolean info = true;
        
        
        
        while(info) {
            choice = Integer.parseInt(JOptionPane.showInputDialog(null, 
                    "\nChoose a planet to get information about (1-8): "
                            + "(9 to quit)", "Planetary Information", 
                            JOptionPane.QUESTION_MESSAGE));
            
            if(choice == 9) {
                JOptionPane.showMessageDialog(null, "Thank You!", "GoodBye", 
                        JOptionPane.INFORMATION_MESSAGE);
                break;
            }
            
            CelestialBody chosenPlanet = (CelestialBody) arrayList.get(choice-1);

            choiceStr = JOptionPane.showInputDialog(null, "\nWhat information "
                    + "would you like?\n Volume, Density, Position, or "
                    + "Distance? (q to quit)", "Choose", 
                    JOptionPane.QUESTION_MESSAGE);

            choiceLow = choiceStr.toLowerCase();
            
            switch (choiceLow) {
                case "volume":
                    JOptionPane.showMessageDialog(null, "The volume of " 
                            + chosenPlanet.getPlanetName()
                            + " is: " + chosenPlanet.getVolume());
                    break;
                case "density":
                    JOptionPane.showMessageDialog(null, "The density of " 
                            + chosenPlanet.getPlanetName()
                            + " is: " + chosenPlanet.getDensity());
                    break;
                case "position":
                    JOptionPane.showMessageDialog(null, "The position of " 
                            + chosenPlanet.getPlanetName()
                            + " is: " + chosenPlanet.getPosition());
                    break;
                case "distance":
                    JOptionPane.showMessageDialog(null, "The distance of " 
                            + chosenPlanet.getPlanetName() 
                            + " is: " + chosenPlanet.getDistance());
                    break;
                default:
                    JOptionPane.showMessageDialog(null, "Thank You!", 
                            "GoodBye", JOptionPane.INFORMATION_MESSAGE);
                    info = false;
                    break;
            }
        }
    }// end getInfo method
    
    // this method simply makes an array out of the assigned planet
    // positions. This is used later by the horoscope method.
    public static void getArray(double[] array, ArrayList<Object> arrayList) {
        
        for(int i = 0; i < arrayList.size(); i++) {
            CelestialBody chosenPlanet = (CelestialBody) arrayList.get(i);
            array[i] = chosenPlanet.getPosition();
        }
    }// end getArray method
    
    // this method will return a horoscope depending on what position
    // the planets in the universe were assigned. 
    public static String getHoroscope(double[] array) {
        
        String horoscope;
        int quad1 = 0;
        int quad2 = 0;
        int quad3 = 0;
        int quad4 = 0;
        // iterate through given array and assign values to different
        // quadrants depending on value. 
        for(int i = 0; i < array.length; i++) {
            if(0 < array[i] && array[i] <= 90) {
                quad1 += 1;
            }
            else if(90 < array[i] && array[i] <= 180) {
                quad2 += 1;
            }
            else if(180 < array[i] && array[i] <= 270) {
                quad3 += 1;
            }
            else {
                quad4 += 1;
            }
        }
        // create an array with quadrant values
        // iterate through for index with highest value
        int[] quad = {quad1, quad2, quad3, quad4};
        int hold = 0;
        int holdIndex = 0;
        
        for(int i = 0; i < quad.length; i++) {
            if(quad[i] > hold) {
                hold = quad[i];
                holdIndex = i;
            }
        }
        // swtich returns horoscope depending on quadrant with most planets
        switch (holdIndex) {
            case 1:
                horoscope = "The day will be good to you.";
                break;
            case 2:
                horoscope = "Don't think too hard about it all.";
                break;
            case 3:
                horoscope = "This might not be your day.";
                break;
            case 4:
                horoscope = "Let's talk about something else.";
                break;
            default:
                horoscope = "All signs point to yes!";
                break;
        }
        // return horoscope message
        return horoscope;
    }
}// end getHoroscope method
