class Parent {
    public void sayHello() {
        System.out.println("Hello From Parent");
    }
}
class Child extends Parent {
    @Override
    public void sayHello() {
        System.out.println("Hello From Child");
    }
}
public class OverriddenFunctionality {
    public static void main(String[] args) {
        Parent p = new Child();
        p.sayHello();
    }
}