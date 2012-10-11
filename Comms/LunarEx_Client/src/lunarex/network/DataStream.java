package lunarex.network;

import java.io.*;

public class DataStream implements Serializable{

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	public short rpm1;
	public short rpm2;
	public short rpm3;
	public short rpm4;
	
	public DataStream(short r1, short r2, short r3, short r4) {
		this.rpm1 = r1;
		this.rpm2 = r2;
		this.rpm3 = r3;
		this.rpm4 = r4;
	}
	public short getRpm1()
	{
		return rpm1;
	}
	public short getRpm2()
	{
		return rpm2;
	}
	public short getRpm3()
	{
		return rpm3;
	}
	public short getRpm4()
	{
		return rpm4;
	}
	public void setRpm1(short value)
	{
		rpm1 = value;
	}
	public void setRpm2(short value)
	{
		rpm2 = value;
	}
	public void setRpm3(short value)
	{
		rpm3 = value;
	}
	public void setRpm4(short value)
	{
		rpm4 = value;
	}

}
