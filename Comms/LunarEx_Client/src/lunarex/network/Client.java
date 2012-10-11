package lunarex.network;

import java.net.*;
import java.util.*;
import java.io.*;

public class Client extends Thread
{
    public String IP;
    public int port;
    public Client(String ip_address, int in_port){
    this.IP = ip_address;
    this.port = in_port;

   }
   public void run()
   {
	      try
	      {
		     DataOperaion operation = new DataOperaion(); //Operations on data, sent from client to server
	    	 System.out.println("Connecting to " + this.IP
	                             + " on port " + this.port);
	         Socket client = new Socket(this.IP, this.port);
	         System.out.println("Connected to "
	                      + client.getRemoteSocketAddress()); //All above is used to make a connection to Server.
             Scanner data = new Scanner(System.in);
	         while(true){
	        	 try
	        	 {
	        		 OutputStream outToServer = client.getOutputStream();
                     InputStream inFromServer = client.getInputStream();
                     ObjectOutputStream out =
	                        new ObjectOutputStream(outToServer);
                     ObjectInputStream in = 
	                        new ObjectInputStream(inFromServer); //Read and write object
                     DataStream stream = null; //Status of the robot, sent from server to client
                     System.out.print("Quit?");
                     if(data.hasNext()){
	        		 operation.q = data.nextBoolean();} //Close connection or not
	        		 if(!operation.quit()) // If not quiting
	        		 {
	        			 System.out.print("Accelerate or decelerate? (true/false): ");
                         if(data.hasNext()){                        
	        			 operation.status = data.nextBoolean();}
	        			 System.out.print("Acceleration: ");
                         if(data.hasNext()){
	        			 operation.acceleration = data.nextShort();}
	        			 System.out.print("Cycle:");
                         if(data.hasNext()){
	        			 operation.cycle = data.nextShort();}
	        			 System.out.println("Simulate data-input process...");
	        			 out.writeObject(operation); //Send commands to Server
                         out.flush();
	        		 }
	        		 else
	        		 {
	        			 out.writeObject(operation);
	        			 break; //Close the socket.
	        		 }
	        		 //for(int i = 0; i < operation.getCycle(); i++) //For-loop retained.
	        		 //{
	        			 stream = (DataStream)in.readObject();
	        			 System.out.println("Current Status(rpm):" + "\n"
	        					 			+ "Wheel 1: " + stream.getRpm1() + "\n"
	        					 			+ "Wheel 2: " + stream.getRpm2() + "\n"
	        					 			+ "Wheel 3: " + stream.getRpm3() + "\n"
	        					 			+ "Wheel 4: " + stream.getRpm4() + "\n");
	        			 System.out.println("-------------------------------------");
	        		// }

	        	 }catch(Exception e)
	        	 {
	        		 e.printStackTrace();
	        	 }
	         }
    	  data.close();   
          client.close();
	      }catch(IOException e)
	      {
	         e.printStackTrace();
	      }
   }
}