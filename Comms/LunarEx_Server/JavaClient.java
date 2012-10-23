import java.io.*;
import java.net.*;

public class JavaClient {
    public static void main(String[] args) throws IOException {
        Socket echoSocket = null;
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        
        String test;

        try {
            echoSocket = new Socket("localhost", 5902);
        } catch (UnknownHostException e) {
            System.exit(1);
        } catch (IOException e) {
            System.exit(1);
        }

        OutputStream outToServer = echoSocket.getOutputStream();
        DataOutputStream out = new DataOutputStream(outToServer);
        int a = 1;

        while(true){
            System.out.print("Send: ");
            test=read.readLine();
            out.writeChars(test);
            /*
            a=a<<1;
            System.out.println("" + a);
            if(a>32){
                a=1;
            }*/
        }

    }
}


