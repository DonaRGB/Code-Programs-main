class Up {
    public void sayHello() {
        System.out.println("Hello From Parent");
    }
}
class Down extends Up {
    @Override
    public void sayHello() {
        System.out.println("Hello From Child");
    }
}
public class OverriddenFunctionality {
    public static void main(String[] args) {
        Up p = new Down();
        p.sayHello();
    }
}