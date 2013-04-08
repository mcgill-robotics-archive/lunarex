package lunarex.gui;

import java.awt.*;
import java.awt.event.*;
import java.awt.font.NumericShaper;
import java.awt.geom.Line2D;
import java.awt.image.*;
import java.util.*;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;

import lunarex.input.*;
import lunarex.network.*;

public class GUIMain extends JFrame {

	private static final long serialVersionUID = 1190876640530075607L;
	static final int WIDTH = 1280;
	static final int HEIGHT = (int) (9 / 16.0 * WIDTH);

	String ipAdressString = "142.157.37.138";

	String portNumberString = "5902";

	Client client = null;
	boolean connected = false;

	// hard-coded some pieces of information about the environment, such as width of Mining Area and initial x value of Obstacle Area
	class Bob {

		float x, y, w = 75, h = 100;
		double angVel, linVel;;
		int angle, containerAngle;
		float massInContainer, totalMass;
		double batteryLevel = 14.2;
		float rpm1, rpm2, rpm3, rpm4;
		boolean doorOpen;
		int elevation;
		

	}
	
	class Crater {
		double x, y, rA, rB;
	}

	class Boulder {
		double x, y, rA, rB;
	}

	class MiningArea {
		double w = 294;
	}

	class ObstacleArea {
		Boulder rockA, rockB, rockC;
		Crater craterA, craterB;
		double x = 150;
	}

	class Rect {
		double x, y, w, h;
	}

	KeyboardInput keyboard = new KeyboardInput(); // Keyboard polling
	Canvas canvas; // Our drawing component
	Bob bob = new Bob(); // Our rectangle
	Rect field = new Rect();
	
	Panel panel = new Panel();
	TextField linVelField = new TextField("Linear Velocity");
	TextField angVelField = new TextField("Angular Velocity");
	Button applyButton = new Button("Apply");
	Label status = new Label("                                     ");
	
	Random rand = new Random();// Used for random circle locations
	boolean manualOverride =false;
	byte[] outByte = new byte[6];
	Boulder rockNo1 = new Boulder();
	Boulder rockNo2 = new Boulder();
	Boulder rockNo3 = new Boulder();
	Crater craterOne = new Crater();
	Crater craterTwo = new Crater();
	ObstacleArea obstacleArea1 = new ObstacleArea();
	MiningArea miningArea = new MiningArea();

	public GUIMain() {

		setIgnoreRepaint(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		canvas = new Canvas();
		canvas.setIgnoreRepaint(true);
		canvas.setSize(WIDTH, HEIGHT);
		panel.add(linVelField);
		panel.add(angVelField);
		panel.add(applyButton);
		panel.add(status);
		applyButton.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				sendVelInfo();
			}
		});
		panel.add(canvas);

		this.add(panel);

		pack();
		// Hookup keyboard polling
		addKeyListener(keyboard);
		canvas.addKeyListener(keyboard);

		//bob.w = 75;
		//bob.h = 100;
		field.w = 738 * 1;
		field.h = 388 * 1;
		field.x = WIDTH - field.w - 20;
		field.y = HEIGHT - field.h - 20;
		bob.x = (float) field.x;
		bob.y = (float) field.y;
		manualOverride = true;

	}

	public void updateData() {
		bob.x = (float) field.x + client.getX();
		bob.y = (float) field.y + client.getY();
		bob.angle = (int) client.getTheta();

		/*
		 * bob.velocity = client.getVelocity();

			bob.containerAngle = client.getContainerAngle();
			bob.massInContainer = client.getMassInContainer();

			bob.batteryLevel = client.getBatteryLevel();
			bob.doorOpen = client.getDoorOpen();
			bob.rpm1 = client.getRpm1();
			bob.rpm2 = client.getRpm2();
			bob.rpm3 = client.getRpm3();
			bob.rpm4 = client.getRpm4();
		 *
		 */

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
				processInput();	
					
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
				
				// draw field
				drawField(g2d,(int)field.x,(int)field.y);		
				
				// Draw battery
				drawBattery(g2d,1000,50);				

				// Draw bob				
				drawBob(g2d);
				
				//Draw meters
				drawMeter(g2d,50,200,outByte[1],"Linear Velocity");
				drawMeter(g2d,200,200,outByte[2],"Angular Velocity");
				drawMeter(g2d,350,200,outByte[4],"Ogger");
				drawMeter(g2d,500,200,outByte[3],"Elevation");
				drawMeter(g2d,650,200,outByte[5],"Bucket Incline");
				
				// 
				
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
	//Teleport bob to position x,y
	public void teleport(Bob b, int x, int y, int theta){
		b.x = (float) field.x + client.getX() + x;
		b.y = (float) field.y + client.getY() + y;
		bob.angle = theta;
	}

	public void moveForward(Bob b, int x){
		b.x += x;
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
			
			// Ogger control
			keyCom(KeyEvent.VK_O,KeyEvent.VK_UP,KeyEvent.VK_DOWN,4);
			
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
		
		g2d.drawString("X: " + ((double) (int) ((bob.x - field.x) / 1))
				/ 100 + " m", x, y);
		y+=12;
		g2d.drawString("Y: " + ((double) (int) ((bob.y - field.y) / 1))
				/ 100 + " m", x, y);
		y+=12;
		
		g2d.drawString("Angle: "
				+ (int) (360 * bob.angle / (2 * Math.PI)), x, y);
		y+=12;
		//g2d.drawString("Manual Override: " + manualOverride, 20, 88);
		g2d.drawString("Connected to server: " + connected, x, y);
		y+=12;
		g2d.drawString("Angular velocity: "+bob.angVel, x, y);
		y+=12;
		g2d.drawString("Linear Velocity: "+bob.linVel, x, y);
		y+=12;
		g2d.drawString("Elevation: "+bob.elevation, x, y);
		y+=12;
		g2d.drawString("Container Angle: "+bob.containerAngle, x, y);
		y+=12;
		g2d.drawString("Door "+ (bob.doorOpen?"Open":"Closed"),x,y);
		y+=12;
	}
	private void drawField(Graphics2D g2d, int x, int y){
		g2d.drawString("Starting/Dumping Area", (x + 10),(y - 2) );
		g2d.drawString("Obstacle Area",  (x + 250),(y - 2) );
		g2d.drawString("Mining Area", (x + 550),(y - 2) );

		// Draw Rectangular Field
		g2d.setColor(Color.cyan);
		g2d.drawRect(x, y, (int) field.w,
				(int) field.h);

		// Draw MiningArea on Field
		g2d.setColor(Color.cyan);
		g2d.draw(new Line2D.Double(x + field.w - miningArea.w,
				y, x + field.w - miningArea.w, y
						+ field.h));

		// Draw ObstacleArea on Field
		g2d.setColor(Color.cyan);
		g2d.draw(new Line2D.Double(x + obstacleArea1.x, y,
				x + obstacleArea1.x, y + field.h));

	}
	private void drawBattery(Graphics2D g2d, int x, int y){
		g2d.setColor(Color.WHITE);
		g2d.drawRect(x, y, 100, 33);
		g2d.drawRect(x+100, y+11, 5, 10);
		Color DARKGREEN = new Color(0, 220, 10);
		g2d.setColor(DARKGREEN);
		g2d.fillRect(x+1, y+1, (int)bob.batteryLevel, 32);
		g2d.setColor(Color.WHITE);
		g2d.drawString("" + bob.batteryLevel + "V", x+40, y+20);
	}
	private void drawMeter(Graphics2D g2d, int x, int y, int ang, String title){
		g2d.setColor(Color.WHITE);
		g2d.drawString(title, x+5, y-5);
		g2d.setColor(Color.BLACK);
		g2d.fillOval(x, y, 100, 100);
		g2d.setColor(Color.DARK_GRAY);
		g2d.fillOval(x+10,y+10,80,80);
		g2d.setColor(new Color(128,255,128));
		g2d.rotate((ang/200.)*Math.PI,x+50,y+50);
		g2d.fillRect(x+45, y+10, 10, 50);
		g2d.rotate(-(ang/200.)*Math.PI,x+50,y+50);
		
	}
	private void drawBob(Graphics2D g2d){
		g2d.setColor(Color.RED);
		g2d.rotate(bob.angle, bob.x + bob.w / 2, bob.y + bob.h / 2);
		g2d.drawRect((int) bob.x, (int) bob.y, (int) bob.w, (int) bob.h);
		g2d.draw(new Line2D.Double(bob.x + bob.w, bob.y,
				(bob.x + 3 * bob.w / 2), (bob.y + bob.h / 2)));
		g2d.draw(new Line2D.Double(bob.x + bob.w, bob.y + bob.h,
				(bob.x + 3 * bob.w / 2), (bob.y + bob.h / 2)));
		g2d.draw(new Line2D.Double(bob.x + bob.w / 2,
				bob.y + bob.h / 2, (bob.x + 3 * bob.w / 2),
				(bob.y + bob.h / 2)));
		g2d.rotate(-bob.angle, bob.x, bob.y);
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
			sendVelInfo();
		}
	}
	
	private void sendVelInfo(){
		try{
			int linVel=Integer.parseInt(linVelField.getText());
			int angVel=Integer.parseInt(angVelField.getText());
			outByte[1]= (byte)(linVel * 50);
			outByte[2]= (byte)(angVel * 127);
			bob.linVel= linVel;
			bob.angVel= angVel;
			status.setText("                                     ");
		} catch (NumberFormatException nfe) {
			status.setText("Invalid inputs!");
		}
	}
	
}
