import javafx.application.Application;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.concurrent.Worker.State;
import javafx.embed.swing.SwingFXUtils;
import javafx.scene.Scene;
import javafx.scene.SnapshotParameters;
import javafx.scene.image.WritableImage;
import javafx.scene.paint.Color;
import javafx.scene.web.WebEngine;
import javafx.scene.web.WebView;
import javafx.stage.Stage;

import javax.imageio.ImageIO;
import java.io.File;
import java.io.IOException;


public class Main extends Application {
    private Scene scene;
    @Override public void start(Stage stage) {
        final Browser browser = new Browser();
        final WebEngine webEngine = browser.getWebView().getEngine();
        final WebView webView = browser.getWebView();

        //add listener to know when rendering is finished
        webEngine.getLoadWorker().stateProperty().addListener(
                new ChangeListener<State>() {
                    @Override
                    public void changed(ObservableValue<? extends State> observable, State oldValue, State newValue) {
                        if(newValue == State.SUCCEEDED) {
                            saveSnapshot(webView);
                            stage.close();
                        }
                    }
                }
        );

        scene = new Scene(browser,1500,800, Color.web("#666970"));
        stage.setScene(scene);
        stage.show();
        stage.setFullScreen(true);
    }

    public static void main(String[] args){
        launch(args);
    }

    private void saveSnapshot(WebView webView) {
        WritableImage snapshot = webView.snapshot(new SnapshotParameters(), null);
        try {
            ImageIO.write(SwingFXUtils.fromFXImage(snapshot, null), "png", new File("C:\\Users\\D071137\\Desktop\\snapshot.png"));
        } catch(IOException ioe) {
            System.err.println("Error while writing file");
        }
    }
}