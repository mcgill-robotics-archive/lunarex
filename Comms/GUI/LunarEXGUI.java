import java.awt.*;
import java.awt.event.*;
import java.awt.geom.Line2D;
import java.awt.image.*;
import java.util.*;
import javax.swing.JFrame;
import javax.swing.JOptionPane;

public class LunarEXGUIWORKINGVERSION extends JFrame {

	static final int WIDTH = 1080;
	static final int HEIGHT = (int) (9 / 16.0 * WIDTH);

	String ipAdressString = "";
	String portNumberString = "";

	class Bob {
		double x, y, w, h, dx, dy;
		double angle, dangle;
	}

	class Rect {
		double x, y, w, h;
	}

	KeyboardInput keyboard = new KeyboardInput(); // Keyboard polling
	Canvas canvas; // Our drawing component
	Vector<Point> circles = new Vector<Point>(); // Circles
	Bob bob = new Bob(); // Our rectangle
	Rect field = new Rect();
	Random rand = new Random();// Used for random circle locations
	Boolean manualOverride;

	public LunarEXGUIWORKINGVERSION() {

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

		bob.dx = bob.dy = 1 / 1;
		bob.w = bob.h = 25;
		bob.dangle = Math.PI / 90;
		field.w = 738 * 1;
		field.h = 388 * 1;
		field.x = WIDTH - field.w - 20;
		field.y = HEIGHT - field.h - 20;
		bob.x = field.x;
		bob.y = field.y;
		manualOverride = false;
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
		Color background = Color.LIGHT_GRAY;

		while (true) {
			try {

				// Poll the keyboard
				keyboard.poll();
				// Should we exit?
				if (keyboard.keyDownOnce(KeyEvent.VK_ESCAPE))
					break;

				// Clear the back buffer
				g2d = bi.createGraphics();
				g2d.setColor(background);
				g2d.fillRect(0, 0, WIDTH, HEIGHT);

				// Draw help
				g2d.setColor(Color.BLACK);
				g2d.drawString("Use arrow keys to move rect", 20, 20);
				g2d.drawString("Press SPACE to add IP ADDRESS", 20, 32);
				// g2d.drawString("Press C to clear circles", 20, 44);
				g2d.drawString("Press ESC to exit", 20, 44);
				g2d.drawString("X: " + ((double) (int) ((bob.x - field.x) / 1))
						/ 100 + " m", 20, 68);
				g2d.drawString("Y: " + ((double) (int) ((bob.y - field.y) / 1))
						/ 100 + " m", 20, 80);
				// g2d.drawString("Speed: ");
				g2d.drawString("Angle: "
						+ (int) (360 * bob.angle / (2 * Math.PI)), 20, 104);
				g2d.drawString("(0,0)", (int) (field.x - 25),
						(int) (field.y - 2));

				// Move bob and add circles
				processInput();

				// Draw random circles
				g2d.setColor(Color.BLUE);
				for (Point p : circles) {
					g2d.drawOval(p.x, p.y, 25, 25);
				}

				// Draw Rectangular Field
				g2d.drawRect((int) (field.x), (int) (field.y), (int) field.w,
						(int) field.h);

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
		// If moving backward
		if (keyboard.keyDown(KeyEvent.VK_DOWN)) {
			bob.x -= bob.dx * Math.cos(bob.angle);
			bob.y -= bob.dy * Math.sin(bob.angle);
			// Check collision with bottom
			if (bob.x < field.x)
				bob.x = field.x;
			if (bob.y < field.y)
				bob.y = field.y;
			if (bob.x > field.x + field.w)
				bob.x = field.x + field.w;
			if (bob.y > field.y + field.h)
				bob.y = field.y + field.h;
			if (bob.x > field.x + field.w - bob.w)
				bob.x = field.x + field.w - bob.w;
			if (bob.y > field.y + field.h - bob.h)
				bob.y = field.y + field.h - bob.h;
		}
		// If moving forward
		if (keyboard.keyDown(KeyEvent.VK_UP)) {
			bob.x += bob.dx * Math.cos(bob.angle);
			bob.y += bob.dy * Math.sin(bob.angle);
			// Check collision with top
			if (bob.x < field.x)
				bob.x = field.x;
			if (bob.y < field.y)
				bob.y = field.y;
			if (bob.x > field.x + field.w - bob.w)
				bob.x = field.x + field.w - bob.w;
			if (bob.y > field.y + field.h - bob.h)
				bob.y = field.y + field.h - bob.h;
			if (bob.x > field.x + field.w)
				bob.x = field.x + field.w;
			if (bob.y > field.y + field.h)
				bob.y = field.y + field.h;
		}
		// If Rotate left
		if (keyboard.keyDown(KeyEvent.VK_LEFT)) {
			bob.angle -= bob.dangle;
			bob.x += (bob.dx * Math.cos(bob.angle)) / 2;
			bob.y += (bob.dy * Math.sin(bob.angle)) / 2;
			// Check collision with left
			if (Math.abs(bob.angle) > 2 * Math.PI)
				bob.angle = 0;
			if (bob.x < field.x)
				bob.x = field.x;
			if (bob.y < field.y)
				bob.y = field.y;
			if (bob.x > field.x + field.w - bob.w)
				bob.x = field.x + field.w - bob.w;
			if (bob.y > field.y + field.h - bob.h)
				bob.y = field.y + field.h - bob.h;
		}
		// If rotate right
		if (keyboard.keyDown(KeyEvent.VK_RIGHT)) {
			bob.angle += bob.dangle;
			bob.x += (bob.dx * Math.cos(bob.angle)) / 2;
			bob.y += (bob.dy * Math.sin(bob.angle)) / 2;
			// Check collision with left
			if (Math.abs(bob.angle) > 2 * Math.PI)
				bob.angle = 0;
			if (bob.x < field.x)
				bob.x = field.x;
			if (bob.y < field.y)
				bob.y = field.y;
			if (bob.x > field.x + field.w - bob.w)
				bob.x = field.x + field.w - bob.w;
			if (bob.y > field.y + field.h - bob.h)
				bob.y = field.y + field.h - bob.h;
		}
		if (keyboard.keyDown(KeyEvent.VK_W)) {
			if (bob.dx >= 2.5 && bob.dy >= 2.5) {
				bob.dx = bob.dx;
				bob.dx = bob.dy;
			} else {
				bob.dx += bob.dx * 0.1;
				bob.dy += bob.dy * 0.1;
			}
		}
		if (keyboard.keyDown(KeyEvent.VK_S)) {
			if (bob.dx == 0 && bob.dy == 0) {
				bob.dx = bob.dx;
				bob.dx = bob.dy;
			} else {
				bob.dx -= bob.dx * 0.1;
				bob.dy -= bob.dy * 0.1;
			}
		}
		// IP ADDRESS BOX
		if (keyboard.keyDownOnce(KeyEvent.VK_SPACE)) {
			ipAdressString = JOptionPane
					.showInputDialog("Please enter an IP Adress to connect to");
			portNumberString = JOptionPane
					.showInputDialog("Pleane enter a port number to connect to");
		}
		// Clear circles if they press C
		if (keyboard.keyDownOnce(KeyEvent.VK_C)) {
			circles.clear();
		}
		if (keyboard.keyDownOnce(KeyEvent.VK_O)) {

		}
	}

	public static void main(String[] args) {
		LunarEXGUIWORKINGVERSION app = new LunarEXGUIWORKINGVERSION();
		app.setTitle("Simple Keyboard Input");
		app.setVisible(true);
		app.run();
		System.exit(0);
	}
}
