let a = 0;

function setup() {
  var width = 800;
  var height = 937;
  createCanvas(width, height);
  bird = new Bird(width/2, height/2);
}

function draw() {
  background(0);
  bird.show();
  fill(255,0,0);
  ellipse(bird.tv.x, bird.tv.y, 5, 5);
  bird.rotate(90);
}