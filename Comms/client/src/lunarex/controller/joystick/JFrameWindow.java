package lunarex.controller.joystick;

import java.awt.Color;
import java.awt.Graphics2D;
import javax.swing.JPanel;
import net.java.games.input.Component;

/**
 * 
 * Joystick Test Window
 * 
 * 
 * @author TheUzo007
 *         http://theuzo007.wordpress.com
 * 
 * 
 * 
 */

public class JFrameWindow extends javax.swing.JFrame {
    
    /**
     * Creates new form JFrameWindow
     */
    public JFrameWindow() {
        initComponents();
        
        this.setResizable(false);
        this.setLocationRelativeTo(null);
        this.setVisible(true);
//        this.setVisible(false);
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jPanelAxes = new javax.swing.JPanel();
        jLabelXYAxis = new javax.swing.JLabel();
        progressBarLabel1 = new javax.swing.JLabel();
        progressBarLabel2 = new javax.swing.JLabel();
        progressBar1 = new javax.swing.JProgressBar();
        progressBar2 = new javax.swing.JProgressBar();
        jPanelXYAxis = new javax.swing.JPanel();
        progressBarLabel3 = new javax.swing.JLabel();
        progressBar3 = new javax.swing.JProgressBar();
        jPanelButtons = new javax.swing.JPanel();
        jPanelHatSwitch = new javax.swing.JPanel();
        jLabelControllerName = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("JInput Joystick Test");

        jPanelAxes.setBorder(javax.swing.BorderFactory.createTitledBorder(null, "Axes", javax.swing.border.TitledBorder.DEFAULT_JUSTIFICATION, javax.swing.border.TitledBorder.DEFAULT_POSITION, null, new java.awt.Color(0, 51, 204)));

        jLabelXYAxis.setText("X Axis / Y Axis");

        progressBarLabel1.setText("Z Axis");

        progressBarLabel2.setText("Z Rotation");

        jPanelXYAxis.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));
        jPanelXYAxis.setPreferredSize(new java.awt.Dimension(111, 111));

        javax.swing.GroupLayout jPanelXYAxisLayout = new javax.swing.GroupLayout(jPanelXYAxis);
        jPanelXYAxis.setLayout(jPanelXYAxisLayout);
        jPanelXYAxisLayout.setHorizontalGroup(
            jPanelXYAxisLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 109, Short.MAX_VALUE)
        );
        jPanelXYAxisLayout.setVerticalGroup(
            jPanelXYAxisLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 109, Short.MAX_VALUE)
        );

        progressBarLabel3.setText("Z Axis");

        progressBar3.setMaximum(99);

        javax.swing.GroupLayout jPanelAxesLayout = new javax.swing.GroupLayout(jPanelAxes);
        jPanelAxes.setLayout(jPanelAxesLayout);
        jPanelAxesLayout.setHorizontalGroup(
            jPanelAxesLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanelAxesLayout.createSequentialGroup()
                .addGroup(jPanelAxesLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanelAxesLayout.createSequentialGroup()
                        .addGap(58, 58, 58)
                        .addComponent(jLabelXYAxis))
                    .addGroup(jPanelAxesLayout.createSequentialGroup()
                        .addGap(37, 37, 37)
                        .addComponent(jPanelXYAxis, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addGap(67, 67, 67)
                .addGroup(jPanelAxesLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(progressBar2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(progressBar1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(progressBarLabel2)
                    .addComponent(progressBarLabel1)
                    .addComponent(progressBarLabel3)
                    .addComponent(progressBar3, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap(26, Short.MAX_VALUE))
        );
        jPanelAxesLayout.setVerticalGroup(
            jPanelAxesLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanelAxesLayout.createSequentialGroup()
                .addGroup(jPanelAxesLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabelXYAxis)
                    .addComponent(progressBarLabel1))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(jPanelAxesLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanelAxesLayout.createSequentialGroup()
                        .addComponent(progressBar1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(13, 13, 13)
                        .addComponent(progressBarLabel2)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(progressBar2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(16, 16, 16)
                        .addComponent(progressBarLabel3)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(progressBar3, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addComponent(jPanelXYAxis, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(0, 16, Short.MAX_VALUE))
        );

        jPanelButtons.setBorder(javax.swing.BorderFactory.createTitledBorder(null, "Buttons", javax.swing.border.TitledBorder.DEFAULT_JUSTIFICATION, javax.swing.border.TitledBorder.DEFAULT_POSITION, null, new java.awt.Color(0, 51, 204)));

        javax.swing.GroupLayout jPanelButtonsLayout = new javax.swing.GroupLayout(jPanelButtons);
        jPanelButtons.setLayout(jPanelButtonsLayout);
        jPanelButtonsLayout.setHorizontalGroup(
            jPanelButtonsLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 248, Short.MAX_VALUE)
        );
        jPanelButtonsLayout.setVerticalGroup(
            jPanelButtonsLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 112, Short.MAX_VALUE)
        );

        jPanelHatSwitch.setBorder(javax.swing.BorderFactory.createTitledBorder(null, "Hat Switch", javax.swing.border.TitledBorder.DEFAULT_JUSTIFICATION, javax.swing.border.TitledBorder.DEFAULT_POSITION, null, new java.awt.Color(0, 51, 204)));

        javax.swing.GroupLayout jPanelHatSwitchLayout = new javax.swing.GroupLayout(jPanelHatSwitch);
        jPanelHatSwitch.setLayout(jPanelHatSwitchLayout);
        jPanelHatSwitchLayout.setHorizontalGroup(
            jPanelHatSwitchLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 0, Short.MAX_VALUE)
        );
        jPanelHatSwitchLayout.setVerticalGroup(
            jPanelHatSwitchLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 0, Short.MAX_VALUE)
        );

        jLabelControllerName.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLabelControllerName.setText("Controller name");
        jLabelControllerName.setHorizontalTextPosition(javax.swing.SwingConstants.CENTER);

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(jPanelButtons, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(jPanelHatSwitch, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                    .addComponent(jPanelAxes, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(jLabelControllerName, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                .addContainerGap())
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jLabelControllerName, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jPanelAxes, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                    .addComponent(jPanelButtons, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(jPanelHatSwitch, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                .addContainerGap())
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JLabel jLabelControllerName;
    private javax.swing.JLabel jLabelXYAxis;
    private javax.swing.JPanel jPanelAxes;
    private javax.swing.JPanel jPanelButtons;
    private javax.swing.JPanel jPanelHatSwitch;
    private javax.swing.JPanel jPanelXYAxis;
    private javax.swing.JProgressBar progressBar1;
    private javax.swing.JProgressBar progressBar2;
    private javax.swing.JProgressBar progressBar3;
    private javax.swing.JLabel progressBarLabel1;
    private javax.swing.JLabel progressBarLabel2;
    private javax.swing.JLabel progressBarLabel3;
    // End of variables declaration//GEN-END:variables

    
    
    
    /* Methods for setting components on the window. */
    
    public void setControllerName(String controllerName){
        jLabelControllerName.setText(controllerName);
    }
    
    public void setXYAxis(int xPercentage, int yPercentage){
        Graphics2D g2d = (Graphics2D)jPanelXYAxis.getGraphics();
        g2d.clearRect(1, 1, jPanelXYAxis.getWidth() - 2, jPanelXYAxis.getHeight() - 2);
        g2d.fillOval(xPercentage, yPercentage, 10, 10);
    }
    
    public void setZAxis(int zAxisValueInPercentage){
        progressBar1.setValue(zAxisValueInPercentage);
    }
    
    public void setZRotation(int zRotationValueInPercentage){
        progressBar2.setValue(zRotationValueInPercentage);
    }
    
    public void setZAxisGamepad(int zAxisValueInPercentage){
        progressBar3.setValue(zAxisValueInPercentage);
    }
    
    public void setControllerButtons(JPanel buttonsPanel){
        jPanelButtons.removeAll();
        jPanelButtons.add(buttonsPanel);
        this.validate();
    }

    public void setHatSwitch(float hatSwitchPosition) {
        int circleSize = 100;
        
        Graphics2D g2d = (Graphics2D)jPanelHatSwitch.getGraphics();
        g2d.clearRect(5, 15, jPanelHatSwitch.getWidth() - 10, jPanelHatSwitch.getHeight() - 22);
        g2d.drawOval(20, 22, circleSize, circleSize);
        
        if(Float.compare(hatSwitchPosition, Component.POV.OFF) == 0)
            return;
        
        int smallCircleSize = 10;
        int upCircleX = 65;
        int upCircleY = 17;
        int leftCircleX = 15;
        int leftCircleY = 68;
        int betweenX = 37;
        int betweenY = 17;
        
        int x = 0;
        int y = 0;
        
        g2d.setColor(Color.blue);
                        
        if(Float.compare(hatSwitchPosition, Component.POV.UP) == 0){
            x = upCircleX;
            y = upCircleY;
        }else if(Float.compare(hatSwitchPosition, Component.POV.DOWN) == 0){
            x = upCircleX;
            y = upCircleY + circleSize;
        }else if(Float.compare(hatSwitchPosition, Component.POV.LEFT) == 0){
            x = leftCircleX;
            y = leftCircleY;
        }else if(Float.compare(hatSwitchPosition, Component.POV.RIGHT) == 0){
            x = leftCircleX + circleSize;
            y = leftCircleY;
        }else if(Float.compare(hatSwitchPosition, Component.POV.UP_LEFT) == 0){
            x = upCircleX - betweenX;
            y = upCircleY + betweenY;
        }else if(Float.compare(hatSwitchPosition, Component.POV.UP_RIGHT) == 0){
            x = upCircleX + betweenX;
            y = upCircleY + betweenY;
        }else if(Float.compare(hatSwitchPosition, Component.POV.DOWN_LEFT) == 0){
            x = upCircleX - betweenX;
            y = upCircleY + circleSize - betweenY;
        }else if(Float.compare(hatSwitchPosition, Component.POV.DOWN_RIGHT) == 0){
            x = upCircleX + betweenX;
            y = upCircleY + circleSize - betweenY;
        }
        
        g2d.fillOval(x, y, smallCircleSize, smallCircleSize);
    }
    
    
    public void setProgressBar1Name(String name)
    {
        this.progressBarLabel1.setText(name);
    }
    
    public void setProgressBar2Name(String name)
    {
        this.progressBarLabel2.setText(name);
    }
    
    public void setProgressBar3Name(String name)
    {
        this.progressBarLabel3.setText(name);
    }
    
    
    public void hideProgresBar3()
    {
        this.progressBar3.setVisible(false);
    }
}
