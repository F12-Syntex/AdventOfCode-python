import javax.swing.*;
import java.awt.*;
import java.io.File;
import java.nio.file.Files;
import java.util.List;

public class Test extends JFrame {

    private JPanel panel;

    public Test() {
        panel = new MyPanel();
        add(panel);

        setTitle("Movement Visualizer");
        setSize(400, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setVisible(true);

        renderMovements();
    }

    private void renderMovements() {
        File input = new File("D:\\git-repo\\AdventOfCode-python\\advent_of_code\\2023\\day18\\input.txt");
        try {
            List<String> lines = Files.readAllLines(input.toPath());
            
            MyPanel myPanel = (MyPanel) panel; // Cast to access custom methods
            myPanel.setLines(lines); // Pass the lines to the panel for rendering

            panel.revalidate(); // Refresh the panel to reflect the added components
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(Test::new);
    }

    // Custom JPanel to override paintComponent for drawing
    private class MyPanel extends JPanel {
        private List<String> lines;

        public void setLines(List<String> lines) {
            this.lines = lines;
        }

        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
        
            int x = 10;
            int y = 10;
        
            // Fill the entire panel with black color
            g.setColor(Color.BLACK);
            g.fillRect(0, 0, getWidth(), getHeight());
        
            for (String line : lines) {
                String[] parts = line.split(" ");
                String direction = parts[0];
                int distance = Integer.parseInt(parts[1]) * 1;
                String color = parts[2].substring(1, parts[2].length() - 1);
        
                g.setColor(Color.decode(color));
        
                if (direction.equals("R")) {
                    g.drawLine(x, y, x + distance, y);
                    x += distance;
                } else if (direction.equals("L")) {
                    g.drawLine(x, y, x - distance, y);
                    x -= distance;
                } else if (direction.equals("U")) {
                    g.drawLine(x, y, x, y - distance);
                    y -= distance;
                } else if (direction.equals("D")) {
                    g.drawLine(x, y, x, y + distance);
                    y += distance;
                }
            }
        }
        
    }
}
