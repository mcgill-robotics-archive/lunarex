package lunarex.network;

import java.net.*;
import java.util.*;
import java.io.*;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

public class Client extends Thread {
	public String IP;
	public int port;
	public LinkedList<String> list;
	public boolean closeConnection;
	public String listData;
	public String receivedData;

	public Client(String ip_address, int in_port) {
		this.IP = ip_address;
		this.port = in_port;
		this.list = new LinkedList<String>();
		this.closeConnection = false;
	}

	public void send(byte[] data) {
		//nothing temporarily
	}

	public String receive() {
		return receivedData;
	}

	public void close() {
		closeConnection = true;
	}

	public float getX() {
		int startingIndex = receivedData.indexOf('x') + 4;
		int endingIndex = receivedData.indexOf(',', startingIndex);
		String xString = receivedData.substring(startingIndex, endingIndex);
		return Float.parseFloat(xString);
	}

	public float getY() {
		int startingIndex = receivedData.indexOf('y') + 4;
		int endingIndex = receivedData.indexOf('\n', startingIndex);
		String yString = receivedData.substring(startingIndex, endingIndex);
		return Float.parseFloat(yString);
	}

	public float getTheta() {
		int startingIndex = receivedData.indexOf("theta") + 8;
		int endingIndex = receivedData.indexOf(',', startingIndex);
		String thetaString = receivedData.substring(startingIndex, endingIndex);
		return Float.parseFloat(thetaString);		
	}

	public void run() {
		try {
			System.out.println("Connecting to " + this.IP + " on port "
					+ this.port);
			Socket client = new Socket(this.IP, this.port);
			System.out.println("Connected to "
					+ client.getRemoteSocketAddress()); // All above is used to
														// make a connection to
														// Server.
			while (true) {
				try {
					PrintWriter out = new PrintWriter(client.getOutputStream(),
							true);// For python Server
					 BufferedReader in = new BufferedReader(new
					 InputStreamReader(client.getInputStream()));// Reading String from python server.
					// DataOutputStream out = new
					// DataOutputStream(client.getOutputStream());//For Java
					// Server
					char[] buffer = new char[1024];

					/*while (list.size() > 0) {
						listData = list.pop();
						out.println(listData);
						System.out.println(listData);
					} */// The while above is for Keyboard inputs.

					in.read(buffer);
					this.receivedData = new String(buffer);
					System.out.println("Current Status: " + "\n" + "X: "
							+ this.getX() + "\n" + "Y: " + this.getY() + "\n"
							+ "Theta: " + this.getTheta()); // Codes above
															// receives the json
															// object and print
															// it out.

					if (closeConnection) {
						break;
					}

				} catch (Exception e) {
					// Do nothing here. Exceptions are redundant.
				}
			}
			client.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}