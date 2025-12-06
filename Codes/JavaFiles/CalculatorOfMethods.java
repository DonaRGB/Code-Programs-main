import java.util.Scanner;
class InputNumbers {
    double num1, num2;
    void getInput(double a, double b) {
        num1 = a;
        num2 = b;
    }
}
class Operations extends InputNumbers {
    double add() {
        return num1 + num2;
    }
    double subtract() {
        return num1 - num2;
    }
    double multiply() {
        return num1 * num2;
    }
    double divide() {
        if (num2 == 0) {
            System.err.println("Error : Division by zero!");
            return 0;
        }
        return num1 / num2;
    }
}
class Calculator extends Operations {
    void calculate(int choice) {
        switch (choice) {
            case 1:
                System.out.println(num1 + " + " + num2 + " = " + add());
                break;
            case 2:
                System.out.println(num1 + " - " + num2 + " = " + subtract());
                break;
            case 3:
                System.out.println(num1 + " * " + num2 + " = " + multiply());
                break;
            case 4:
                System.out.println(num1 + " / " + num2 + " = " + divide());
                break;
            default:
                System.err.println("Invalid choice!");
        }
    }
}
public class CalculatorOfMethods {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        System.out.println("--- Simple Calculator ---\n(Order Matters!)");
        System.out.println("Enter the first number :");
        double a = scn.nextDouble();
        System.out.println("Enter the second number :");
        double b = scn.nextDouble();
        System.out.println("\nChoose operation :\n1. Add\n2. Subtract\n3. Multiply\n4. Divide");
        System.out.println("Enter choice :");
        int choice = scn.nextInt();
        Calculator c = new Calculator();
        c.getInput(a,b);
        c.calculate(choice);
        scn.close();
    }
}
