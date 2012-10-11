import java.net.*;
import java.io.*;

public class Server extends Thread
{
   private ServerSocket serverSocket;
   
   public Server(int port) throws IOException
   {
      serverSocket = new ServerSocket(port);
      serverSocket.setSoTimeout(1200000);
   }

   public void run()
   {
      DataStream stream = new DataStream((short)0,(short)0,(short)0,(short)0);//Operations on data, sent from client to server
	  while(true)
      {
         try
         {
        	System.out.println("Waiting for client on port " +
            serverSocket.getLocalPort() + "..." + "\n" + "Time out in 120 seconds.");
            Socket server = serverSocket.accept();
            System.out.println("Just connected to "
                  + server.getRemoteSocketAddress());
            while(true)
            {
                ObjectInputStream in =
                  new ObjectInputStream(server.getInputStream());
                ObjectOutputStream out =
                  new ObjectOutputStream(server.getOutputStream());
                short a; //Acceleration. Received from client in the Operations.
            	System.out.println("Waiting for commands from Client...");
            	try{
            		DataOperaion operation = null;//Status of the robot, sent from server to client
                    operation = (DataOperaion)in.readObject();//receive operation commands from the client.
            		if(operation.quit()) break; //Tell whether to close the socket.
                    System.out.println("Received command to " + operation.OperationDescription()); //Command receit confirmation
            		for(int i = 0; i < operation.getCycle(); i++) //For-loop is retained to realize the function of printing the process of accelerating later on.
            		{
            			if(operation.status()) a = operation.getAcceleration();
            			else a = (short)(0 - operation.getAcceleration());
            			stream.setRpm1((short)(stream.getRpm1() + a));
            			stream.setRpm2((short)(stream.getRpm2() + a));
            			stream.setRpm3((short)(stream.getRpm3() + a));
            			stream.setRpm4((short)(stream.getRpm4() + a));
            			//out.writeObject(stream);
            		}
            	out.writeObject(stream); // Send the status of the robot to Client.
                out.flush();
            	}catch(Exception e)
            	{
            		System.out.println(e);
            		break;
            	}
            	
            }
            System.out.println("Connection closed by Client.");
            server.close();
         }catch(SocketTimeoutException s)
         {
            System.out.println("Socket timed out!");
            break;
         }catch(IOException e)
         {
            e.printStackTrace();
            break;
         }
      }
   }
   public static void main(String [] args)
   {
      try
      {
         Thread t = new Server(11);
         t.start();
      }catch(IOException e)
      {
         e.printStackTrace();
      }
   }
}