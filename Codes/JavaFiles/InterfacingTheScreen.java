interface MyInterface {
    public void method1();
    public void method2();
}
public class InterfacingTheScreen implements MyInterface{
    public void method1() {
        System.out.println("Implementation of Method1");
    }
    public void method2() {
        System.out.println("Implementation of Method2");
    }
    public static void main(String[] args) {
        MyInterface obj = new InterfacingTheScreen();
        obj.method1();
        obj.method2();
    }
}
