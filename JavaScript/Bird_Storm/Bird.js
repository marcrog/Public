class Bird{
    constructor(x, y){
        this.x = x;
        this.y = y;
        this.pos = createVector(this.x, this.y);
      
        let inc = 15;           
        let t_y = this.pos.y - (Math.sqrt(3)/3) * inc * 2;
        let t_x = this.pos.x; 

        let r_x = this.pos.x + inc/2;
        let r_y = this.pos.y + 1/(2*Math.sqrt(3)) * inc*2;

        let l_x = this.pos.x - inc/2;
        let l_y = this.pos.y + 1/(2*Math.sqrt(3)) * inc*2;

        this.tv = createVector(t_x, t_y);
        this.rv = createVector(r_x, r_y);
        this.lv = createVector(l_x, l_y);
        
        
    }

    show(){
        stroke(255);
        fill(255);
        triangle(this.tv.x, this.tv.y, this.lv.x, this.lv.y, this.rv.x, this.rv.y);
    }

    update(){
        this.pos.add(this.speed);
    }

    moveTo(x, y){
        let point = createVector(x, y);
        let i  = p5.Vector.sub(point, this.pos);

        stroke(255,0,0);
        line(this.pos.x, this.pos.y, point.x, point.y);
        stroke(0,0,255);
        line(this.pos.x, this.pos.y, point.x, this.pos.y);
        stroke(0,255,0);
        line(point.x, this.pos.y, point.x, point.y);

        // console.log(this.pos.dist(point));
        let angle = degrees(Math.acos(i.x/(this.pos.dist(point))));
        angleMode(DEGREES);
        translate(this.pos.x, this.pos.y);
        rotate();
    }

    rotate(angle){
      angleMode(DEGREES);
      let beta = 90 - angle;
      let teta = (180 - angle - 2*beta) / 2;
      let diametro = Math.abs(this.tv.y - this.y) * Math.sin(angle);
      this.tv.x = this.tv.x + diametro / Math.cos(teta);
      this.tv.y = this.tv.y + diametro / Math.sin(teta);
    }
}