class Shape {
    public double getArea() {
        return 0;
    }
}
class Triangle extends Shape {
    private double base;
    private double height;
    public Triangle(double base,double height) {
        this.base = base;
        this.height = height;
    }
    public double getArea() {
        return 0.5 * base * height;
    }
}
class Square extends Shape {
    private double side;
    public Square(double side) {
        this.side = side;
    }
    public double getArea() {
        return side *side;
    }
}
public class ShapePolymorphism {
    public static void main(String[] args) {
        Shape[] s = new Shape[2];
        s[0] = new Square(5);
        s[1] = new Triangle(2,2);
        System.out.println("Area of the Square : " + s[0].getArea());
        System.out.println("Area of the Triangle : " + s[1].getArea());
    }
}
