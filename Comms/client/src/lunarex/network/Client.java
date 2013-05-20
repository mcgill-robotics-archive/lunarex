package lunarex.network;

import java.net.*;
import java.util.*;
import java.awt.font.NumericShaper;
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
		try{
			return Float.parseFloat(xString);
		} catch (NumberFormatException e){
			return 0.0f;
		}
	}
	
	public float getY() {
		int startingIndex = receivedData.indexOf('y') + 4;
		int endingIndex = receivedData.indexOf('\n', startingIndex);
		String yString = receivedData.substring(startingIndex, endingIndex);
		try{
			return Float.parseFloat(yString);
		} catch (NumberFormatException e){
			return 0.0f;
		}
	}

	public float getTheta() {
		int startingIndex = receivedData.indexOf("theta") + 8;
		int endingIndex = receivedData.indexOf(',', startingIndex);
		String thetaString = receivedData.substring(startingIndex, endingIndex);
		try{
			return Float.parseFloat(thetaString);
		} catch (NumberFormatException e){
			return 0.0f;
		}
	}
	public String getCornerStatus(String corner) { 
		int startingIndex = receivedData.indexOf(corner) + 12;
		int endingIndex = receivedData.indexOf(',', startingIndex);
		String cornerString = receivedData.substring(startingIndex, endingIndex);
		return cornerString;
	}
	
	public float getRes() {
		int startingIndex = receivedData.indexOf("mapRes") + 9;
		int endingIndex = receivedData.indexOf(',', startingIndex);
		String s = receivedData.substring(startingIndex, endingIndex);
		try{
			return Float.parseFloat(s);
		} catch (NumberFormatException e){
			return 0.0f;
		}
	}

	public int getWidth() {
		int startingIndex = receivedData.indexOf("mapWidth") + 11;
		int endingIndex = receivedData.indexOf(',', startingIndex);
		String s = receivedData.substring(startingIndex, endingIndex);
		try{
			return Integer.parseInt(s);
		} catch (NumberFormatException e){
			return 0;
		}
	}
	
	public int getHeight() {
		int startingIndex = receivedData.indexOf("mapHeight") + 12;
		int endingIndex = receivedData.indexOf(',', startingIndex);
		String s = receivedData.substring(startingIndex, endingIndex);
		try{
			return Integer.parseInt(s);
		} catch (NumberFormatException e){
			return 0;
		}
	}
	
	public boolean getStartedLeft() {
		int startingIndex = receivedData.indexOf("startedLeft") + 14;
		int endingIndex = receivedData.indexOf(',', startingIndex);
		String s = receivedData.substring(startingIndex, endingIndex);
		try{
			return Boolean.parseBoolean(s);
		} catch (NumberFormatException e){
			return false;
		}
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
							//System.out.println((int)commands[1]);
							out.write(commands);
							/*
							for (int i = 0; i < commands.length; i++) {
								out.write((int) commands[i]);
								//System.out.println((int) commands[i]);
							}
							*/
						}
						
						//out.write(commands);
						//System.out.println(commands);
						this.resetCommands();
					}

					//	The function for receiving data from the server
					if (input.ready()) {
						input.read(buffer);
						this.receivedData = new String(buffer);
						// Do not need this print anymore. But keep it for testing.
//						System.out.println("Current Status: " + "\n" + "X: "
//								+ this.getX() + "\n" + "Y: " + this.getY()
//								+ "\n" + "Theta: " + this.getTheta());
						
//						System.out.println(receivedData);
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
