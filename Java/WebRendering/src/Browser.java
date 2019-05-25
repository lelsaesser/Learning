import javafx.geometry.HPos;
import javafx.geometry.VPos;
import javafx.scene.layout.Region;
import javafx.scene.web.WebEngine;
import javafx.scene.web.WebView;

class Browser extends Region {
    final WebView webView = new WebView();
    final WebEngine webEngine = webView.getEngine();

    public Browser() {
        webEngine.load("http://www.stackoverflow.com");
        //add web view to scene
        //webView.setVisible(false);
        getChildren().add(webView);
    }

    public WebView getWebView() {
        return this.webView;
    }

    @Override protected void layoutChildren() {
        double w = getWidth();
        double h = getHeight();
        layoutInArea(webView,0,0,w,h,0, HPos.CENTER, VPos.CENTER);
    }
}