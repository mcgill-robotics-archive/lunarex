package lunarex.network;

import java.io.*;

@SuppressWarnings("serial")
public class DataOperation implements Serializable{

	public boolean status;
	public boolean q;
	public short acceleration;
	public short cycle;
	
	public DataOperation(boolean flag, boolean quit, short acc, short cyc)
	{
		this.status = flag;
		this.q = quit;
		this.acceleration = acc;
		this.cycle = cyc;
	}
	public DataOperation() {
		// TODO Auto-generated constructor stub
	}
	public boolean quit()
	{
		return q;
	}
	public boolean status()
	{
		return status;
	}
	public short getAcceleration()
	{
		return acceleration;
	}
	public short getCycle()
	{
		return cycle;
	}
    public String OperationDescription()
    {
        if(this.status())
        {
            return "accelerate at " + this.getAcceleration() + " rpm/s for " + this.getCycle()+ " Cycles.";
        }
        return "decelerate at " + this.getAcceleration() + " rpm/s for " + this.getCycle()+ " Cycles.";
    }
}
