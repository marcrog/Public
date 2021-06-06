import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class Prova extends PApplet {

public void setup() {
    
    background(0);
}

public void draw() {
    fill(255,0,0);
    rect(50, 50, 50, 50);
}
  public void settings() {  size(300, 200); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "Prova" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
