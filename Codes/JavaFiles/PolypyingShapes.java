interface Shape {
    double getArea();
}
class Rectangle implements Shape {
    private double width;
    private double height;
    public Rectangle(double width,double height) {
        this.width = width;
        this.height = height;
    }

    @Override
    public double getArea() {
        return width * height;
    }
}
class Circle implements Shape {
    private double radius;
    public Circle(double radius) {
        this.radius = radius;
    }

    @Override
    public double getArea() {
        return Math.PI * radius * radius;
    }
}
class AreaCalculator {
    public double sumAreas(Shape[] shapes) {
        double totalArea = 0;
        for (Shape s : shapes) {
            totalArea += s.getArea();
        }
        return totalArea;
    }
}
public class PolypyingShapes {
    public static void main(String[] args) {
        Shape[] shapes = new Shape[2];
        shapes[0] = new Rectangle(3,5);
        shapes[1] = new Circle(100);
        AreaCalculator ac = new AreaCalculator();
        double totalArea = ac.sumAreas(shapes);
        System.out.println("Total Area : " + totalArea);
    }
}