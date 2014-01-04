/**
 * this class will create a celestial body
 */
import java.util.Random;

public class CelestialBody {
    //declare some local variables
    private double radius;
    private double mass;
    private double volume;
    private double density;
    private double gravity;
    private String planetName;
    private double position;
    private int distance;
    
    //constructor (defined parameter)
    public CelestialBody (double radiusNum, double massNum, String name) {
        
        this.radius = radiusNum;
        this.mass = massNum;
        this.planetName = name;
    }
    
    //default constructor (no parameter)
    public CelestialBody() {

        this.radius = 1;
        this.mass = 1;
    }
    
    //volume caluclation method
    public double calcVolume() {

        setVolume((4.0/3.0)*Math.PI*(getRadius()*getRadius()*getRadius()));
        return getVolume();
    }
    
    //density calculation method
    public double calcDensity() {
        
        setDensity(getMass() / calcVolume());
        return getDensity();
    }
    
    //graity calculation method
    public double calcGravity() {
        
        setGravity((6.67e-11 * getMass()) / (getRadius()*getRadius()));
        return getGravity();
    }
    
    //positional method
    public double calcPosition() {
        
        Random num = new Random();
        this.position = num.nextInt(360) + 1;
        
        return position;
    }
    
    /**
     * getter
     * @return the position
     */
    public double getPosition() {
        return position;
    }

    /**
     * setter
     * @param position the position to set
     */
    public void setPostion(double position) {
        this.position = position;
    }
    
    /**
     * getter
     * @return the distance
     */
    public int getDistance() {
        return distance;
    }
    
    /**
     * setter
     * @param distance the distance to set
     */
    public void setDistance(int distance) {
        this.distance = distance;
    }
    
    /**
     * getter
     * @return the radius
     */
    public double getRadius() {
        return radius;
    }

    /**
     * setter
     * @param radius the radius to set
     */
    public void setRadius(double radius) {
        this.radius = radius;
    }

    /**
     * getter
     * @return the mass
     */
    public double getMass() {
        return mass;
    }

    /**
     * setter
     * @param mass the mass to set
     */
    public void setMass(double mass) {
        this.mass = mass;
    }

    /**
     * getter
     * @return the planetName
     */
    public String getPlanetName() {
        return planetName;
    }

    /**
     * setter
     * @param planetName the planetName to set
     */
    public void setPlanetName(String planetName) {
        this.planetName = planetName;
    }

    /**
     * @return the volume
     */
    public double getVolume() {
        return volume;
    }

    /**
     * @param volume the volume to set
     */
    public void setVolume(double volume) {
        this.volume = volume;
    }

    /**
     * @return the density
     */
    public double getDensity() {
        return density;
    }

    /**
     * @param density the density to set
     */
    public void setDensity(double density) {
        this.density = density;
    }

    /**
     * @return the gravity
     */
    public double getGravity() {
        return gravity;
    }

    /**
     * @param gravity the gravity to set
     */
    public void setGravity(double gravity) {
        this.gravity = gravity;
    }
}
