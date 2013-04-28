package lunarex.gui;

import java.awt.*;
import java.awt.event.*;
import java.awt.geom.Line2D;
import java.awt.image.*;
import java.util.*;

import javax.swing.JFrame;
import javax.swing.JOptionPane;

import net.java.games.input.Controller;
import joystick.JFrameWindow;
import joystick.JInputJoystick;
import joystick.JInputJoystickTest;
import joystick.JoystickTest;
import lunarex.input.*;
import lunarex.network.*;

public class GUIMain extends JFrame {

	private static final long serialVersionUID = 1190876640530075607L;
	static final int WIDTH = /*1280*/800;
	static final int HEIGHT = /*(int) (9 / 16.0 * WIDTH)*/800;
	static final int LINE_SPACING = 20;
	static final float MAX_LIN_SPEED = 1.8f;
	static final float MAX_ANG_SPEED = 4f;
	static final double calibFactorLinV = 127/MAX_LIN_SPEED;
	static final double calibFactorAngV = 127/MAX_ANG_SPEED;

	//FOR NETBOOK
	//String ipAdressString = "142.157.37.138";
	
	//FOR LOCALHOST
	String ipAdressString = "127.0.0.1";

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

	TextField linVelField = new TextField("0",5);
	TextField angVelField = new TextField("0",5);
	Button applyButton = new Button("Apply");
	Label linVelLabel = new Label("Linear Velocity");
	Label angVelLabel = new Label("Angular Velocity");
	Label status = new Label("                                     ");
	
	Random rand = new Random();// Used for random circle locations
	boolean manualOverride =true;
	boolean controller =false;
	boolean prevController = false;
	byte[] outByte = new byte[6];

	int fontsize = 40000;
	Font font = new Font("Helvetica", Font.PLAIN, fontsize);

	/*COMMANDS TO ROBOT*/
	
	//Commands we're sending out
	byte OUT_angVel, OUT_linVel, OUT_suspension, OUT_augerSpeed;
	boolean OUT_doorOpen, OUT_bucketPos;
	
	//used for processing
	double angVel, linVel;
	int suspensionPos; // 0 to 255
	int augerSpeed; //0 to 255
	
	final int SUSPENSION_DELAY = 2;
	final int AUGER_DELAY = 5;
	
	
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
		testPanel.add(applyButton);
		testPanel.add(status);
		applyButton.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
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


//		manualOverride = true;
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
//		jinputJoystickTest.pollControllerAndItsComponents(Controller.Type.STICK);
		
		while (true) {
			try {
				processInput();	
				try{
					processControllerInput();
					JoystickTest.updateControllerWindow(joystick, window);
					
					if(!this.prevController&&joystick.getButtonValue(3)) {
						controller = !controller;
					}
					this.prevController = joystick.getButtonValue(3);
					
					if(!this.prevConnected&&joystick.getButtonValue(0)) {
						if(!connected){
							client = new Client(ipAdressString,
									Integer.parseInt(portNumberString));
							client.start();
						}
						connected = !connected;
					}
					this.prevConnected = joystick.getButtonValue(0);
					
				} catch (Exception e){
					
				}
					
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

				// Draw info text
				drawTextInfo(g2d,20,40);
				g2d.setFont(font);
				
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

	// keyboard input
	protected void processInput() {
		if (manualOverride) {
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
			
		}
		// IP ADDRESS BOXtrue
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
		if (keyboard.keyDownOnce(KeyEvent.VK_C)) {
			int reply = JOptionPane.showConfirmDialog(null,
					"Toggle controller state?",
					"Controller", JOptionPane.YES_NO_OPTION);
			if (reply == JOptionPane.YES_OPTION) {
				controller = !controller;
			}
		}
	}
	private void processControllerInput() {
		if(manualOverride&&controller){
			ArrayList<Boolean> buttons = joystick.getButtonsValues();
			if(buttons.get(12)&&suspensionPos<=255-SUSPENSION_DELAY){ //triangle
				suspensionPos+=SUSPENSION_DELAY;
			}	else if(buttons.get(14)&&suspensionPos>=SUSPENSION_DELAY){ //X
				suspensionPos-=SUSPENSION_DELAY;
			}  	else if (buttons.get(15)) //square
				suspensionPos=0;
				else if (buttons.get(13)) //circle
				suspensionPos=255;
				
			if(buttons.get(4)&&augerSpeed<=255-AUGER_DELAY){ //up arrow
				augerSpeed+=AUGER_DELAY;
			}	else if(buttons.get(6)&&augerSpeed>=AUGER_DELAY){ //down arrow
				augerSpeed-=AUGER_DELAY;
			}	else if(buttons.get(7)) //left arrow
				augerSpeed=0;
				else if(buttons.get(5)) //right arrow
				augerSpeed=255;
			
			if(buttons.get(11)) OUT_doorOpen = true; //R1
			else if(buttons.get(10)) OUT_doorOpen = false; //L1
			
			if(buttons.get(9)) OUT_bucketPos = true; //R2
			else if(buttons.get(8))  OUT_bucketPos = false; //L2
			//Linear Velocity
			 double yValue = (-1)*MAX_LIN_SPEED*joystick.getYAxisValue();
			 //Angular Velocity
			 double xValue = MAX_ANG_SPEED*joystick.getZAxisValue();
			 sendVelocities(yValue, xValue); 
		}
	}
	public static void main(String[] args) {
		GUIMain app = new GUIMain();
		app.setTitle("Simple Keyboard Input");
		app.setVisible(true);
		app.run();
		System.exit(0);
	}
	
	private void drawTextInfo(Graphics2D g2d,int x,int y){
		g2d.setColor(Color.WHITE);
				
		g2d.drawString("----CLIENT STATUS ----", x, y); 
		y+=LINE_SPACING;
		g2d.drawString("Connected to server: " + connected, x, y);
		y+=LINE_SPACING;
		g2d.drawString("Input from Controller: " + controller  , x, y);
		y+=LINE_SPACING*2;
		g2d.drawString("----OUTGOING TO SERVER ----", x, y); 
		y+=LINE_SPACING;
		g2d.drawString("Angular velocity: "+OUT_angVel+" ("+angVel+")", x, y);
		y+=LINE_SPACING;
		g2d.drawString("Linear Velocity: "+OUT_linVel+" ("+linVel+")", x, y);
		y+=LINE_SPACING;
		g2d.drawString("Door open? : "+OUT_doorOpen, x, y);
		y+=LINE_SPACING;
		g2d.drawString("Bucket up? : "+OUT_bucketPos, x, y);
		y+=LINE_SPACING;
		g2d.drawString("Suspension position: "+ /*OUT_suspension*/ suspensionPos,x,y);
		y+=LINE_SPACING;
		g2d.drawString("Auger speed: " + /*OUT_augerSpeed*/augerSpeed, x, y);
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
	 * Get values from textfields & send them to sendVelInfo
	 */
	private void getFromTextBoxesAndSendVelocities(){
		try{
			this.linVel=Double.parseDouble(linVelField.getText());
			this.angVel=Double.parseDouble(angVelField.getText());
			sendVelocities(linVel, angVel);
			status.setText("                                     ");
		} catch (NumberFormatException nfe) {
			status.setText("Invalid inputs!");
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
			status.setText("                                     ");
		} catch (NumberFormatException nfe) {
			status.setText("Invalid inputs!");
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