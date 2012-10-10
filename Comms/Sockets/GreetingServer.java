import java.net.*;
import java.io.*;

public class GreetingServer extends Thread
{
   private ServerSocket serverSocket;
   
   public GreetingServer(int port) throws IOException
   {
      serverSocket = new ServerSocket(port);
      serverSocket.setSoTimeout(1200000);
   }

   public void run()
   {
      while(true)
      {
         try
         {
            System.out.println("Local Address: " + serverSocket.getLocalSocketAddress() + "\n" + 
            "Waiting for client on port " +
            serverSocket.getLocalPort() + "...");
            Socket server = serverSocket.accept();
            System.out.println("Just connected to "
                  + server.getRemoteSocketAddress());
        	//DataInputStream in = new DataInputStream(server.getInputStream());
            ObjectInputStream in = new ObjectInputStream(server.getInputStream());
            LunarexDataStream input = null;
            input = (LunarexDataStream) in.readObject();
            input.print();
            server.close();
            //while(true)
            //{
            	//if(in.readUTF().equals("quit"))
            		//server.close();
            	//System.out.println("Client: " + in.readUTF());
            //}
         }catch(SocketTimeoutException s)
         {
            System.out.println("Socket timed out!");
            break;
         }catch(IOException e)
         {
            e.printStackTrace();
            break;
         } catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
      }
   }
   public static void main(String [] args)
   {
      int port = 11;
      try
      {
         Thread t = new GreetingServer(port);
         t.start();
      }catch(IOException e)
      {
         e.printStackTrace();
      }
   }
}