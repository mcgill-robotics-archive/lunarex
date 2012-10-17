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
	public JSONObject DataStream;// Transfer message by JSON

	public Client(String ip_address, int in_port) {
		this.IP = ip_address;
		this.port = in_port;
		this.list = new LinkedList<String>();
		this.closeConnection = false;
	}

	public void send(String data) {
		list.push(data);
	}

	public String receive() {
		return receivedData;
	}

	public void close() {
		closeConnection = true;
	}
	
	public JSONObject getReceivedData()
	{
		return this.DataStream;
	}
	
	public double getX()
	{
		return (double)this.getReceivedData().get("X");
	}
	
	public double getY()
	{
		return (double)this.getReceivedData().get("Y");
	}
	
	public double getTheta()
	{
		return (double)this.getReceivedData().get("Theta");
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
					PrintWriter out = new PrintWriter(client.getOutputStream(), true);//For python Server
					BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream()));
					//DataOutputStream out = new DataOutputStream(client.getOutputStream());//For Java Server
					char[] buffer = new char[1024];

					while (list.size() > 0) {
						listData = list.pop();
						out.println(listData);
						System.out.println(listData);
					}
					if(in.ready()){
						in.read(buffer);
						System.out.println(buffer);
					}
					if (closeConnection) {
						break;
					}

				} catch (Exception e) {
					//Do nothing here. Exceptions are redundant.
				}
			}
			client.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}