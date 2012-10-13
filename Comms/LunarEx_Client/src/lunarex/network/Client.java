package lunarex.network;

import java.net.*;
import java.util.*;
import java.io.*;

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

	public void send(String data) {
		list.push(data);
	}

	public String receive() {
		return receivedData;
	}

	public void close() {
		closeConnection = true;
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
					// PrintWriter out = new
					// PrintWriter(client.getOutputStream(),
					// true);
					OutputStream outToServer = client.getOutputStream();
					DataOutputStream out = new DataOutputStream(outToServer);
					// BufferedReader in = new BufferedReader(new
					// InputStreamReader(client.getInputStream()));

					while (list.size() > 0) {
						listData = list.pop();
						out.writeUTF(listData);
						System.out.println(listData);
					}
					if (closeConnection) {
						break;
					}

				} catch (Exception e) {
					//e.printStackTrace();
				}
			}
			client.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}