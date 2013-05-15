package lunarex.gui;

import java.awt.BorderLayout;
import java.awt.Button;
import java.awt.Canvas;
import java.awt.Checkbox;
import java.awt.CheckboxGroup;
import java.awt.Color;
import java.awt.Container;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.GraphicsConfiguration;
import java.awt.GraphicsDevice;
import java.awt.GraphicsEnvironment;
import java.awt.Label;
import java.awt.Panel;
import java.awt.TextField;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.image.BufferStrategy;
import java.awt.image.BufferedImage;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.Random;

import javax.swing.JFrame;
import javax.swing.JOptionPane;

import lunarex.controller.joystick.*;
import lunarex.input.KeyboardInput;
import lunarex.network.Client;
import net.java.games.input.Controller;

public class GUIMain extends JFrame {

	private static final long serialVersionUID = 1190876640530075607L;
	
	/*DISPLAY CONSTANTS*/
	static final int WIDTH = /*1280*/800;
	static final int HEIGHT = 800;  /*(int) (9 / 16.0 * WIDTH)*/
	static final int LINE_SPACING = 20;
	static final int COLUMN_WIDTH = 250;
	static final int PERC_COLUMN_WIDTH = 50;
	static final int FONTSIZE = 20;

	//FOR MACBOOK AIR ON MCGILL NETWORK

	String ipAdressString = "142.157.42.13";
	
	//FOR MACBOOK AIR ON OUR NETWORK
	String ipAdressString = "192.168.1.100";

	
	//FOR LOCALHOST
	//String ipAdressString = "127.0.0.1";

	String portNumberString = "5902";

	Client client = null;
	boolean connected = false;
	boolean prevConnected = false;
	// Creates controller
    JInputJoystick joystick = new JInputJoystick(Controller.Type.STICK);
	KeyboardInput keyboard = new KeyboardInput(); // Keyboard polling
    final JFrameWindow window = new JFrameWindow();
    JInputJoystickTest jinputJoystickTest = new JInputJoystickTest();
 
    Canvas canvas; // Our drawing component
	Panel testPanel = new Panel();
	Panel ctrlPanel = new Panel();
	Container contentPane = this.getContentPane();	
	Font font = new Font("Helvetica", Font.PLAIN, FONTSIZE);

	TextField linVelField = new TextField("0",5);
	TextField angVelField = new TextField("0",5);
	TextField suspField = new TextField("0",5);
	TextField bucketField = new TextField("0",5);
	TextField augerField = new TextField("0",5);
	CheckboxGroup doorField = new CheckboxGroup();
	Button sendButton = new Button("Send");
	Label linVelLabel = new Label("lin vel");
	Label angVelLabel = new Label("ang vel");
	Label suspLabel = new Label("susp lvl (%)");
	Label bucketLabel = new Label("bucket lvl (%)");
	Label augerLabel = new Label("auger speed (%)");
	Label doorLabel = new Label("door");
	
	Random rand = new Random();// Used for random circle locations
	boolean controller =false;
	boolean prevController = false;
	
	boolean manualOverride= false;
	
	byte[] outByte = new byte[6];
	/*
	 * BYTE 0: OUT_doorOpen
	 * BYTE 1: OUT_linVel
	 * BYTE 2: OUT_angVel
	 * BYTE 3: OUT_suspension
	 * BYTE 4: OUT_augerSpeed
	 * BYTE 5: OUT_bucketPos
	 */
	

	/*COMMANDS TO ROBOT*/
	
	//Commands we're sending out
	byte OUT_angVel, OUT_linVel, OUT_suspension, OUT_augerSpeed, OUT_doorOpen, OUT_bucketPos; 
	
	final int SUSPENSION_POS_HIGH = 0;
	final int SUSPENSION_POS_LOW = 255;
	final int BUCKET_POS_HIGH = 0;
	final int BUCKET_POS_LOW = 255;
	
	//used for processing
	double angVel = 0;
	double linVel = 0;
	int suspensionPos = SUSPENSION_POS_HIGH; // 0 to 255
	int augerSpeed = 0; //0 to 255
	int bucketPos = BUCKET_POS_LOW; // 0 to 255
	int doorOpen = 0;
	String doorStatus = "";
	
	/*COMMAND CONSTANTS*/
	final int SUSPENSION_INCREMENT = 2;
	final int AUGER_INCREMENT = 5;
	final int BUCKET_INCREMENT = 3;
	
	static final float MAX_LIN_SPEED = 1.8f; //1.8 before
	static final float MAX_ANG_SPEED = 2.0f; //4  before
	
	public GUIMain() {
		
		window.dispose();
		setIgnoreRepaint(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		canvas = new Canvas();
		canvas.setIgnoreRepaint(true);
		canvas.setSize(WIDTH, HEIGHT);		
		
		testPanel.add(linVelLabel);
		testPanel.add(linVelField);
		testPanel.add(angVelLabel);
		testPanel.add(angVelField);
		testPanel.add(suspLabel);
		testPanel.add(suspField);
		testPanel.add(bucketLabel);
		testPanel.add(bucketField);
		testPanel.add(augerLabel);
		testPanel.add(augerField);
		testPanel.add(doorLabel);
		testPanel.add(new Checkbox("open", false, doorField));
		testPanel.add(new Checkbox("close", true, doorField));
		testPanel.add(sendButton);

		sendButton.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				sendTextBoxesValues();
				getFromTextBoxesAndSendVelocities();
			}

		});

		ctrlPanel.add(window.getContentPane());
		
		contentPane.add(ctrlPanel,BorderLayout.LINE_START);
		contentPane.add(testPanel,BorderLayout.PAGE_START);
		contentPane.add(canvas,BorderLayout.LINE_END);
		
		pack();
		// Hookup keyboard polling
		addKeyListener(keyboard);
		canvas.addKeyListener(keyboard);

		try{
			JoystickTest.initControllerWindow(joystick, window);
		} catch (Exception e){
			
		}
	}

	public void run() {

		canvas.createBufferStrategy(2);
		BufferStrategy buffer = canvas.getBufferStrategy();
		GraphicsEnvironment ge = GraphicsEnvironment
				.getLocalGraphicsEnvironment();
		GraphicsDevice gd = ge.getDefaultScreenDevice();
		GraphicsConfiguration gc = gd.getDefaultConfiguration();
		BufferedImage bi = gc.createCompatibleImage(WIDTH, HEIGHT);

		Graphics graphics = null;
		Graphics2D g2d = null;
		              
		Color background = Color.DARK_GRAY;
		
		while (true) {
			try {
				processKeyboardInput();	
				try{
					if(manualOverride&&controller){
						processControllerInput();
					}
						
					JoystickTest.updateControllerWindow(joystick, window);
					
					//if "Start" is pressed, set manual override and controller to true
					if(!this.prevController&&joystick.getButtonValue(3)) {
						if(!manualOverride){
							int reply = JOptionPane.showConfirmDialog(null,
									"Do you really want to take over manual control?",
									"Man Override", JOptionPane.YES_NO_OPTION);
							if (reply == JOptionPane.YES_OPTION) {
								manualOverride = true;
							}
						}
						controller = !controller;
					}
					this.prevController = joystick.getButtonValue(3);
					
					//if not connected, press "Select" to connect to server
					if(!connected&&joystick.getButtonValue(0)) {
						client = new Client(ipAdressString,
								Integer.parseInt(portNumberString));
						client.start();
						connected = true;
					}
					this.prevConnected = joystick.getButtonValue(0);
					
				} catch (Exception e){}
					
				/*The above functions have only changed the non-OUT variables.
				 * Now update all OUT* variables, and the outByte array
				 */
				updateAllOUTValues();				
				populateOUTArray();

				//send the array of bytes to the client
				if (client != null) {
					client.send(outByte);						
				}		
			
				// Poll the keyboard
				keyboard.poll();
				// Should we exit?
				if (keyboard.keyDownOnce(KeyEvent.VK_ESCAPE))
					break;

				// Clear the back buffer
				g2d = bi.createGraphics();
				g2d.setColor(background);
				g2d.fillRect(0, 0, WIDTH, HEIGHT);
				g2d.setFont(font);
				
				// Draw info text
				drawTextInfo(g2d,20,40);
				
				// Blit image and flip...
				graphics = buffer.getDrawGraphics();
				graphics.drawImage(bi, 0, 0, null);
				if (!buffer.contentsLost())
					buffer.show();

				// Let the OS have a little time...
				try {
					Thread.sleep(10);
				} catch (InterruptedException e) {
				}

			} finally {
				// Release resources
				if (graphics != null)
					graphics.dispose();
				if (g2d != null)
					g2d.dispose();
			}
		}
	}
	
	private void processControllerInput() {
		ArrayList<Boolean> buttons = joystick.getButtonsValues();
		
		/*SUSPENSION BUTTONS*/
		if(buttons.get(14)&&suspensionPos<=255-SUSPENSION_INCREMENT){ //X
			suspensionPos+=SUSPENSION_INCREMENT;
		}	else if(buttons.get(12)&&suspensionPos>=SUSPENSION_INCREMENT){ //triangle
			suspensionPos-=SUSPENSION_INCREMENT;
		}  	else if (buttons.get(13)) //circle
			suspensionPos=SUSPENSION_POS_HIGH;
			else if (buttons.get(15)) //square
			suspensionPos=SUSPENSION_POS_LOW;
		
		/*AUGER BUTTONS*/
		if(buttons.get(4)&&augerSpeed<=255-AUGER_INCREMENT){ //up arrow
			augerSpeed+=AUGER_INCREMENT;
		}	else if(buttons.get(6)&&augerSpeed>=AUGER_INCREMENT){ //down arrow
			augerSpeed-=AUGER_INCREMENT;
		}	else if(buttons.get(7)) //left arrow
			augerSpeed=0;
			else if(buttons.get(5)) //right arrow
			augerSpeed=255;
		
		/*DOOR BUTTONS*/
		if(buttons.get(11)){
			doorOpen = 255; //R1. 255 is door open
		}
		else if(buttons.get(10)){
			doorOpen = 0; //L1. 0 is door closed
		}
		
		/*BUCKET BUTTONS*/
		if(buttons.get(8) && bucketPos<=255-BUCKET_INCREMENT) {
			bucketPos+=BUCKET_INCREMENT; //L2
		}
		else if(buttons.get(9) && bucketPos >= BUCKET_INCREMENT){
			bucketPos -= BUCKET_INCREMENT; //R2
		}
		
		/*VELOCITY JOYSTICKS*/
		//Linear Velocity
		linVel = (-1)*MAX_LIN_SPEED*joystick.getYAxisValue();
		//Angular Velocity
		angVel = (-1)*MAX_ANG_SPEED*joystick.getZAxisValue();
	}
	
	public static void main(String[] args) {
		GUIMain app = new GUIMain();
		app.setTitle("LunarEx Control Dashboard");
		app.setVisible(true);
		app.run();
		System.exit(0);
	}
	
	private void updateAllOUTValues(){
		OUT_linVel=mapVelToByte((float)linVel);
		OUT_angVel=mapAngToByte((float)angVel);
		OUT_suspension =(byte) suspensionPos;
		OUT_augerSpeed =(byte)augerSpeed;
		OUT_bucketPos =	(byte) bucketPos;
		OUT_doorOpen = (byte) doorOpen;
	}
	
	private void populateOUTArray(){
		outByte[0] = OUT_doorOpen;
		outByte[1] = OUT_linVel;
		outByte[2] = OUT_angVel;
		outByte[3] = OUT_suspension;
		outByte[4] = OUT_augerSpeed;
		outByte[5] = OUT_bucketPos;
	}
	
	private void drawTextInfo(Graphics2D g2d,int x,int y){
		int bucketPosPercentage = (255-bucketPos)*100/255;
		int suspPosPercentage = (255-suspensionPos)*100/255;
		int augerSpeedPercentage = augerSpeed*100/255;
		
		g2d.setColor(Color.WHITE);
				
		g2d.drawString("----CLIENT STATUS ----", x, y); 
		y+=LINE_SPACING;
		g2d.drawString("Manual Override: ", x, y);
		g2d.drawString(""+manualOverride, x+COLUMN_WIDTH, y);
		y+=LINE_SPACING;
		g2d.drawString("Connected to Server: ", x, y);
		g2d.drawString(""+connected, x+COLUMN_WIDTH, y);
		y+=LINE_SPACING;
		g2d.drawString("Input from Controller: ", x, y);
		g2d.drawString(""+controller, x+COLUMN_WIDTH, y);
		y+=LINE_SPACING*2;
		g2d.drawString("----OUTGOING TO SERVER ----", x, y); 
		y+=LINE_SPACING;
		g2d.drawString("Angular Velocity: ", x, y);
		g2d.drawString(""+OUT_angVel, x+COLUMN_WIDTH, y);
		g2d.drawString("("+ new DecimalFormat("#.###").format(angVel)+")", x+COLUMN_WIDTH+PERC_COLUMN_WIDTH, y);
		y+=LINE_SPACING;
		g2d.drawString("Linear Velocity: ", x, y);
		g2d.drawString(""+OUT_linVel, x+COLUMN_WIDTH, y);
		g2d.drawString("("+new DecimalFormat("#.###").format(linVel)+")", x+COLUMN_WIDTH+PERC_COLUMN_WIDTH, y);
		y+=LINE_SPACING;
		g2d.drawString("Door Status : ", x, y);
		doorStatus = OUT_doorOpen != 0 ? "Open" : "Closed";
		g2d.drawString(""+doorStatus, x+COLUMN_WIDTH, y);
		y+=LINE_SPACING;
		g2d.drawString("Bucket Position : ", x, y);
		g2d.drawString(""+bucketPos, x+COLUMN_WIDTH, y);
		g2d.drawString("("+bucketPosPercentage+"% Up)", x+COLUMN_WIDTH+PERC_COLUMN_WIDTH, y);
		y+=LINE_SPACING;
		g2d.drawString("Suspension Position: ",x,y);
		g2d.drawString(""+suspensionPos, x+COLUMN_WIDTH, y);
		g2d.drawString("("+suspPosPercentage+"% Up)", x+COLUMN_WIDTH+PERC_COLUMN_WIDTH, y);
		y+=LINE_SPACING;
		g2d.drawString("Auger Speed: ", x, y);
		g2d.drawString(""+augerSpeed, x+COLUMN_WIDTH, y);
		g2d.drawString("("+augerSpeedPercentage+"% Up)", x+COLUMN_WIDTH+PERC_COLUMN_WIDTH, y);
		y+=LINE_SPACING*2;
		g2d.drawString("----INCOMING FROM SERVER ----", x, y); 
		y+=LINE_SPACING;
		g2d.drawString("slam_out_pose:", x, y);
		y+=LINE_SPACING;
		g2d.drawString("x: ", x, y);
		if(client!=null&&client.receive()!=null)
			g2d.drawString(""+client.getX(), x+COLUMN_WIDTH,y);
		y+=LINE_SPACING;
		g2d.drawString("y: " , x, y);
		if(client!=null&&client.receive()!=null)
			g2d.drawString(""+client.getY(), x+COLUMN_WIDTH,y);
		y+=LINE_SPACING;
		g2d.drawString("w: ", x, y);
		if(client!=null&&client.receive()!=null)
			g2d.drawString(""+client.getTheta(), x+COLUMN_WIDTH,y);
	}
	
	private void keyCom(int key, String stopSign) {
		if (keyboard.keyDown(key)) {
			if (stopSign.equals("jerkyHold")) {
				outByte[1] >>= 1;
				outByte[2] >>= 1;
			} 
			else{
				for (int i = 1; i <= 2; i++) {
					if (outByte[i] < (byte)0) {
						outByte[i]++;
					} else {
						outByte[i]--;
					}
				}
			}
		}
	}
	private void keyCom(int key, int i){
		if(keyboard.keyDownOnce(key)){
			
			if((outByte[0]&(0b00000001<<i))==0){
				outByte[0] |= 1<<i;
			}else{
				outByte[0] &= 0b11111111-1<<i;
			}
		}
	}
	private void keyCom(int keyMain, int keyUp, int keyDown, int i){
		if (keyboard.keyDown(keyMain)) {
			if(keyboard.keyDown(keyUp)){
				if(outByte[i]!=127){
					outByte[i]++;
				}
			}
			if(keyboard.keyDown(keyDown)){
				if(outByte[i]!=-128){
					outByte[i]--;
				}
			}
			if(keyboard.keyDown(KeyEvent.VK_SPACE)){
				outByte[i] =0;
			}
		}
	
	}
	// sends linear and angular velocity on "Enter" key
	private void keyCom(int key){
		if (keyboard.keyDownOnce(key)){
			getFromTextBoxesAndSendVelocities();
		}
	}
	/**
	 * 	Get values from textfields & send them to server
	 */

	private void sendTextBoxesValues() {
		getFromTextBoxesAndSendVelocities();
		//TODO: add other send methods
	}
	/**
	 * Get values from textfields & send them to sendVelInfo
	 */
	private void getFromTextBoxesAndSendVelocities(){
		try{
			this.linVel=Double.parseDouble(linVelField.getText());
			this.angVel=Double.parseDouble(angVelField.getText());
			sendVelocities(linVel, angVel);
		} catch (NumberFormatException nfe) {
		}
	}

	/**
	 * Send the params to the server
	 * @param linVel
	 * @param angVel
	 */
	private void sendVelocities(double linVel, double angVel){
		try{
			this.linVel = linVel;
			this.angVel = angVel;
			//byte linVel=mapVelToByte(Float.parseFloat(linVelField.getText()));
			this.OUT_linVel=mapVelToByte((float)linVel);
			this.OUT_angVel=mapAngToByte((float)angVel);
			outByte[1]= this.OUT_linVel;
			outByte[2]= this.OUT_angVel;
		} catch (NumberFormatException nfe) {
		}
	}
	

	// keyboard input
	protected void processKeyboardInput() {
		// IP ADDRESS BOX
		if (keyboard.keyDownOnce(KeyEvent.VK_SPACE) && !connected) {
			client = new Client(ipAdressString,
					Integer.parseInt(portNumberString));
			client.start();
			connected = true;
		}
		if (keyboard.keyDownOnce(KeyEvent.VK_M)) {
			int reply = JOptionPane.showConfirmDialog(null,
					"Do you really want to take over manual control?",
					"Man Override", JOptionPane.YES_NO_OPTION);
			if (reply == JOptionPane.YES_OPTION) {
				manualOverride = !manualOverride;
			}
		}
		if(manualOverride){
			// Linear Velocity
			keyCom(KeyEvent.VK_Q,KeyEvent.VK_UP,KeyEvent.VK_DOWN,1);

			// Angular Velocity CCW is positive
			keyCom(KeyEvent.VK_W,KeyEvent.VK_LEFT,KeyEvent.VK_RIGHT,2);

			//Elevation
			keyCom(KeyEvent.VK_E,KeyEvent.VK_UP,KeyEvent.VK_DOWN,3);

			// Auger control
			keyCom(KeyEvent.VK_A,KeyEvent.VK_UP,KeyEvent.VK_DOWN,4);

			// Bucket Incline
			keyCom(KeyEvent.VK_B,KeyEvent.VK_UP,KeyEvent.VK_DOWN,5);

			// Dooor open/close
			keyCom(KeyEvent.VK_S,0);

			// Stop everything
			keyCom(KeyEvent.VK_H, "smoothHold");

			//	A smooth break
			keyCom(KeyEvent.VK_J, "jerkyHold");

			// Set linear and angular velocity manually
			keyCom(KeyEvent.VK_ENTER);

			if (keyboard.keyDownOnce(KeyEvent.VK_C)) {
				int reply = JOptionPane.showConfirmDialog(null,
						"Toggle controller state?",
						"Controller", JOptionPane.YES_NO_OPTION);
				if (reply == JOptionPane.YES_OPTION) {
					controller = !controller;
				}
			}
		}
	}
	
	private byte mapVelToByte(float realVel){
		//realVel is the desired speed in m/s
		// max speed is approx 1.8 m/s
		//map it to int between 0 and 255
		
		float tempSpeed = realVel + MAX_LIN_SPEED; // shift up to positives
		tempSpeed = tempSpeed*255/(2*MAX_LIN_SPEED); //scale
		byte byteSpeed = (byte) Math.min(Math.max(tempSpeed,0),255); //constrain values to be only within [0,255] - saturates values otherwise				
		return byteSpeed;
	}
	
	private byte mapAngToByte(float realAng){
		//realVel is the desired speed in m/s
		// max speed is approx 4.0 rad/s
		//map it to int between 0 and 255
		
		float tempSpeed = realAng + MAX_ANG_SPEED; // shift up to positives
		tempSpeed = tempSpeed*255/(2*MAX_ANG_SPEED); //scale
		byte byteSpeed = (byte) Math.min(Math.max(tempSpeed,0),255); //constrain values to be only within [0,255] - saturates values otherwise				
		return byteSpeed;
	}
	
}