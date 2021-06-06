class Rectangle{
    Rectangle(int x, int y){
        this.x = x;
        this.y = y;
    }

    void show(){
        fill(255,0,0);
        rect(this.x, this.y, 50, 50);
    }
}