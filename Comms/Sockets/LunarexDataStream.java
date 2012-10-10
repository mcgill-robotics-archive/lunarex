import java.io.*;

@SuppressWarnings("serial")
public class LunarexDataStream implements Serializable{
    public short xpos;
    public short ypos;
    public short angle;
    public float mass;
    public short rpm1;
    public short rpm2;
    public short rpm3;
    public short rpm4;
    public short batteryVolume;
    public boolean doorStatus;
    public int augerAngle;
    public short augerRpm;
    public short totalMass;
    public short elevation; 
    public void print()
    {
    	System.out.println("Simulation conditions(listing just x-position and y-position as an example):" + "\n"
                            + "xpos: " + xpos + "\n" + "ypos: " + ypos);
    }
}
