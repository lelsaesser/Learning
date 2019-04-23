import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.io.IOException;

public class Render extends JFrame {

    private Image image;

    @Override
    public void paint(Graphics g) {
        super.paint(g);

        try {
            image = ImageIO.read(getClass().getResourceAsStream("/screen01.png"));
        } catch (IOException e) {
            e.printStackTrace();
        }

        g.drawImage(image, 90, 90, null);
    }
}
