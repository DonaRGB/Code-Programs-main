class Superclass {
    int number = 50;
}
class Subclass extends Superclass {
    int number = 96;
    void printNumber() {
        System.out.println(number);
    }
}
public class SuperPositionalAccessity {
    public static void main(String[] args) {
        Subclass sub = new Subclass();
        sub.printNumber();
    }
}