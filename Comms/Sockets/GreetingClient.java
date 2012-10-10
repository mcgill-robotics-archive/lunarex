import java.net.*;
import java.io.*;

public class GreetingClient
{
   public static void main(String [] args)
   {
      String serverName;
      int port = 11;
      try
      {
         LunarexDataStream stream = new LunarexDataStream();
         stream.xpos = 1; 
         stream.ypos = 2;
    	 BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    	 System.out.print("IP Address: ");
         serverName = bf.readLine();
    	 System.out.println("Connecting to " + serverName
                             + " on port " + port);
         Socket client = new Socket(serverName, port);
         System.out.println("Just connected to "
                      + client.getRemoteSocketAddress());
         OutputStream outToServer = client.getOutputStream();
         //DataOutputStream out =
           //            new DataOutputStream(outToServer);
         ObjectOutputStream out = new ObjectOutputStream(outToServer);
         out.writeObject(stream);
         out.flush();
         //while(true){
        	 //out.writeUTF(bf.readLine());
         	//InputStream inFromServer = client.getInputStream();
         	//DataInputStream in =
                        //new DataInputStream(inFromServer);
         	//System.out.println("Server: " + in.readUTF());
         	//if(bf.readLine().equals("quit"))
         		client.close();
         //}
      }catch(IOException e)
      {
         e.printStackTrace();
      }
   }
}