let img;
function setup() {
    createCanvas(1000, 1250);
    img = loadImage('assets/laDefense.jpeg'); // Load the image
  }
function draw() {
    // Displays the image at its actual size at point (0,0)
    img.resize(500, 625)
    image(img, 0, 0);

    // Displays the image at point (0, height/2) at half size
}