package lunarex.testArena;

import java.awt.*;
import java.awt.event.*;
import java.awt.geom.Line2D;
import java.awt.image.*;
import java.util.*;
import javax.swing.JFrame;
import javax.swing.JOptionPane;

//import lunarex.gui.GUIMain;
import lunarex.input.*;

public class Arena extends JFrame{

	/**
	 * @param args
	 */
	
	static final int WIDTH = 1280;
	static final int HEIGHT = (int) (9 / 16.0 * WIDTH);
	static final double PIXELRATIO = 1.5; // .. pixel/cm
	
	class Bob {

		float x, y, w = (float) (75*PIXELRATIO), h = (float) (100*PIXELRATIO), velocity;
		int angle, containerAngle;
		float massInContainer, totalMass;
		int batteryLevel = 50;
		float rpm1, rpm2, rpm3, rpm4;
		boolean doorOpen;
		int elevationWheel1, elevationWheel2, elevationWheel3, elevationWheel4;

	}

	class Crater {
		double x, y;
		double r = 30*PIXELRATIO;
	}

	class Boulder {
		double x, y, r;
	}

	class MiningArea {
		double x = 294*PIXELRATIO;
	}

	class ObstacleArea {
		Boulder rockA, rockB, rockC;
		Crater craterA, craterB;
		double x = 150*PIXELRATIO;
	}

	class Rect {
		double x, y, w, h;
	}
	
	KeyboardInput keyboard = new KeyboardInput(); // Keyboard polling
	Canvas canvas; // Our drawing component
	Bob bob = new Bob(); // Our rectangle
	Rect field = new Rect();
	Random rand = new Random();// Used for random circle locations
	
	Boulder rock1 = new Boulder();
	Boulder rock2 = new Boulder();
	Boulder rock3 = new Boulder();
	Crater crater1 = new Crater();
	Crater crater2 = new Crater();
	ObstacleArea obstacleArea = new ObstacleArea();
	MiningArea miningArea = new MiningArea();
	
	
	
	public Arena() {

		setIgnoreRepaint(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		canvas = new Canvas();
		canvas.setIgnoreRepaint(true);
		canvas.setSize(WIDTH, HEIGHT);
		
		add(canvas);
		pack();

		// Hookup keyboard polling
		addKeyListener(keyboard);
		canvas.addKeyListener(keyboard);

		//bob.w = 75;
		//bob.h = 100;
		field.w = 738 *PIXELRATIO;
		field.h = 388 *PIXELRATIO;
		field.x = WIDTH - field.w - 20;
		field.y = HEIGHT - field.h - 20;
		bob.x = (float) field.x;
		bob.y = (float) field.y;
		//manualOverride = true;
		
		rock1.r = 30*PIXELRATIO;
		rock1.x = field.x+(Math.random()*(miningArea.x-rock1.r)+rock1.r/2)+obstacleArea.x;
		rock1.y = field.y+(rock1.r/2+Math.random()*(field.h-rock1.r));
		
		rock2.r = 30*PIXELRATIO;
		rock2.x = field.x+(Math.random()*(miningArea.x-rock2.r)+rock2.r/2)+obstacleArea.x;
		rock2.y = field.y+(rock2.r/2+Math.random()*(field.h-rock2.r));
		
		rock3.r = 30*PIXELRATIO;
		rock3.x = field.x+(Math.random()*(miningArea.x-rock3.r)+rock3.r/2)+obstacleArea.x;
		rock3.y = field.y+(rock3.r/2+Math.random()*(field.h-rock3.r));
		
		crater1.x = field.x+(Math.random()*(miningArea.x-crater1.r)+crater1.r/2)+obstacleArea.x;
		crater1.y = field.y+(crater1.r/2+Math.random()*(field.h-crater1.r));
		
		crater2.x = field.x+(Math.random()*(miningArea.x-crater2.r)+crater2.r/2)+obstacleArea.x;
		crater2.y = field.y+(crater2.r/2+Math.random()*(field.h-crater2.r));
		
	}

//	public void updateData() {
//		bob.x = (float) field.x;
//		bob.y = (float) field.y;
//		
//
//		/*
//		 * bob.velocity = client.getVelocity();
//		
//			bob.containerAngle = client.getContainerAngle();
//			bob.massInContainer = client.getMassInContainer();
//		
//			bob.batteryLevel = client.getBatteryLevel();
//			bob.doorOpen = client.getDoorOpen();
//			bob.rpm1 = client.getRpm1();
//			bob.rpm2 = client.getRpm2();
//			bob.rpm3 = client.getRpm3();
//			bob.rpm4 = client.getRpm4();
//		 * 
//		 */
//
//	}
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
		Color background = Color.BLACK;

		while (true) {
			try {
				/*// System.out.println(outByte[0]);
				if (outByte[0] != 0) {
					// client.send(outByte);
					if (client != null) {
						client.send(outByte);
						// System.out.println(outByte[0]);
					}
					for (int i = 0; i < outByte.length; i++) {
						outByte[i] = 0;
					}
				}*/

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
				g2d.setColor(Color.WHITE);
				g2d.drawString("X: " + ((double) (int) ((bob.x - field.x) / 1))
						/ 100 + " m", 20, 40);
				g2d.drawString("Y: " + ((double) (int) ((bob.y - field.y) / 1))
						/ 100 + " m", 20, 52);
				// g2d.drawString("Speed: ");
				g2d.drawString("Angle: "
						+ (int) (360 * bob.angle / (2 * Math.PI)), 20, 64);
			//	g2d.drawString("Manual Override: " + manualOverride, 20, 88);
			//	g2d.drawString("Connected to server: " + connected, 20, 100);

				g2d.drawString("(0,0)", (int) (field.x - 25),
						(int) (field.y - 2));

				// Move bob
				//processInput();

				// Draw Rectangular Field
				g2d.setColor(Color.cyan);
				g2d.drawRect((int) (field.x), (int) (field.y), (int) field.w,
						(int) field.h);
				
				// Draw MiningArea on Field
				g2d.setColor(Color.cyan);
				g2d.draw(new Line2D.Double(field.x + field.w - miningArea.x,
						field.y, field.x + field.w - miningArea.x, field.y
								+ field.h));

				// Draw ObstacleArea on Field
				g2d.setColor(Color.cyan);
				g2d.draw(new Line2D.Double(field.x + obstacleArea.x, field.y,
						field.x + obstacleArea.x, field.y + field.h));
	
				// Draw battery
				g2d.setColor(Color.WHITE);
				g2d.drawRect(1000, 50, 100, 33);
				g2d.drawRect(1100, 61, 5, 10);
				Color DARKGREEN = new Color(0, 220, 10);
				g2d.setColor(DARKGREEN);
				g2d.fillRect(1001, 51, bob.batteryLevel, 32);
				g2d.setColor(Color.WHITE);
				g2d.drawString("" + bob.batteryLevel + "%", 1040, 70);

				// Draw bob
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
				
				//draw the obstacles
				g2d.setColor(Color.GRAY);
				g2d.fillOval((int)rock1.x, (int) rock1.y, (int) rock1.r,(int) rock1.r);
				g2d.fillOval((int)rock2.x, (int) rock2.y, (int) rock2.r,(int) rock2.r);
				g2d.fillOval((int)rock3.x, (int) rock3.y, (int) rock3.r,(int) rock3.r);
				
				g2d.setColor(Color.DARK_GRAY);
				g2d.fillOval((int)crater1.x, (int) crater1.y, (int) crater1.r,(int) crater1.r);
				g2d.fillOval((int)crater2.x, (int) crater2.y, (int) crater2.r,(int) crater2.r);
				

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
		b.x = (float) field.x + x;
		b.y = (float) field.y + y;
		bob.angle = theta;
	}

	public void moveForward(Bob b, int dx) {
		b.x += dx * Math.cos(b.angle * 2 * Math.PI / 360);
		b.y += dx * Math.sin(b.angle * 2 * Math.PI / 360);
	}
	
	public void moveBackward(Bob b, int dx){
		b.x -= dx * Math.cos(b.angle * 2 * Math.PI / 360);
		b.y -= dx * Math.sin(b.angle * 2 * Math.PI / 360);
	}
	
	public void turn(Bob b, int dAngle){
		b.angle +=dAngle;
	}
	
	// this method returns a value depending on where bob is. 
	// -1 is in the starting/dumping area, 0 is in the obstacle area and 1 is in the mining area
	public int whatArea()
	{
		if (bob.x-field.x<obstacleArea.x)
		{
			return -1;
		}
		if (bob.x-field.x<miningArea.x)
		{
			return 0;
		}
		return 1;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Arena app = new Arena();
		app.setTitle("Arena");
		app.setVisible(true);
		app.run();
		System.exit(0);
	}

}
