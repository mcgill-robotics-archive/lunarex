package lunarex.network;

import java.net.*;
import java.util.*;
import java.io.*;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

public class Client extends Thread {
	public String IP;
	public int port;
	public boolean closeConnection;
	public String receivedData;
	public byte[] commands;
	public boolean isManualOverride;
	public boolean sended = false;

	public Client(String ip_address, int in_port) {
		this.IP = ip_address;
		this.port = in_port;
		this.closeConnection = false;
		this.isManualOverride = false;
	}

	public void send(byte[] data) {
		// this.isManualOverride = true;
		this.sended = true;
		this.commands = data.clone();
	}

	public void resetCommands() {
		this.sended = false;
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
			PrintWriter output = null;
			BufferedReader input = null;
			DataOutputStream out = null;
			while (true) {
				try {
					output = new PrintWriter(client.getOutputStream(), true);// For
																				// python
																				// Server
					input = new BufferedReader(new InputStreamReader(
							client.getInputStream()));// Reading String from
														// python server.
					out = new DataOutputStream(client.getOutputStream());
					char[] buffer = new char[1024];

					if (this.sended) {
						if (commands != null) {
							for (int i = 0; i < commands.length; i++) {
								out.write((int) commands[i]);
								System.out.println((int) commands[i]);
							}
						}
						this.resetCommands();
					}

					if (input.ready()) {
						input.read(buffer);
						this.receivedData = new String(buffer);
						System.out.println("Current Status: " + "\n" + "X: "
								+ this.getX() + "\n" + "Y: " + this.getY()
								+ "\n" + "Theta: " + this.getTheta());
					}

					if (closeConnection) {
						break;
					}

				} catch (Exception e) {
					e.printStackTrace();
				}
			}
			output.close();
			input.close();
			client.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}