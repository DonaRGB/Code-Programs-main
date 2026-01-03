public class MainCiricular {
    public static void main(String[] args) {
        Circle c = new Circle(5.0);
        System.out.println("Radius : %.2f\n" + c.getRadius());
        System.out.println("Area : %.2f\n" + c.area());
        System.out.println("Circumference : %.2f\n" + c.circumference());
    }
}