import java.util.Scanner;
public class TryAndExceptionOfErrors {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        try {
            System.out.println("Enter two numbers :");
            int x = sc.nextInt();
            int y = sc.nextInt();
            int z = x / y;
            System.out.println(x + " / " + y + " = " + z);
        } catch (ArithmeticException ex) {
            System.out.println("----- Catch Block -----");
            System.out.println(ex.toString());
        } finally {
            System.out.println("----- Finally Block -----");
            System.out.println("Application Developed and Designed by\nThe Coder Cods");
            scn.close();
        }
        System.out.println("--- DONE ---");
    }
}