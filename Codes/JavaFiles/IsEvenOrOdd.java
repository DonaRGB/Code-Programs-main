import java.util.Scanner;
public class IsEvenOrOdd {
    public static String isOddOrEven(int num) {
        if (num % 2 == 0) {
            return "even";
        } else {
            return "odd";
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number : ");
        int numberInput = sc.nextInt();
        String isOddOrEvenAsWord =  isOddOrEven(numberInput);
        System.out.println(numberInput + " is an " + isOddOrEvenAsWord + " number.");
        sc.close();
    }
}
