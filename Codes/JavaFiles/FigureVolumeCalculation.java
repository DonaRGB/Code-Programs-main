class Figure {
    public double getVolume() {
        return 0;
    }
}
class Cube extends Figure {
    private double edge;
    public Cube(double edge) {
        this.edge = edge;
    }
    public double getVolume() {
        return edge * edge * edge;
    }
}
class Cylinder extends Figure {
    private double radius;
    private double height;
    public Cylinder(double radius,double height) {
        this.radius = radius;
        this.height = height;
    }
    public double getVolume() {
        return 3.14 * radius * radius * height;
    }
}
class Cuboid extends Figure {
    private double length;
    private double width;
    private double height;
    public Cuboid(double length,double width,double height) {
        this.length = length;
        this.width = width;
        this.height = height;
    }
    public double getVolume() {
        return length * width * height;
    }
}
class Sphere extends Figure {
    private double radius;
    public Sphere(double radius) {
        this.radius = radius;
    }
    public double getVolume() {
        return (4 * 3.14 * radius * radius * radius) / 3;
    }
}
class Pyramid extends Figure {
    private double length;
    private double width;
    private double height;
    public Pyramid(double length, double width, double height) {
        this.length = length;
        this.width = width;
        this.height = height;
    }
    public double getVolume() {
        return (length * width * height) / 3;
    }
}
class Cone extends Figure {
    private double radius;
    private double height;
    public Cone(double radius, double height) {
        this.radius = radius;
        this.height = height;
    }
    public double getVolume() {
        return (radius * radius * height) / 3;
    }
}
public class FigureVolumeCalculation { //all units are cm
    Shape[] s = new Shape[6];
    s[0] = new Cube(5);
    s[1] = new Cylinder(5,4);
    s[2] = new Cuboid(2,3,4);
    s[3] = new Sphere(3);
    s[4] = new Pyramid(5,4,6);
    s[5] = new Cone(3,5);
    System.out.println("Volume of Cube : " + s[0].getVolume());
    System.out.println("Volume of Cylinder : " + s[1].getVolume());
    System.out.println("Volume of Cuboid : " + s[2].getVolume());
    System.out.println("Volume of Sphere : " + s[3].getVolume());
    System.out.println("Volume of Pyramid : " + s[4].getVolume());
    System.out.println("Volume of Cone : " + s[5].getVolume())
}