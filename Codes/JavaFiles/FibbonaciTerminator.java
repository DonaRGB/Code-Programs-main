import java.util.Scanner;
public class FibbonaciTerminator {
    public static long Fibbonaci(long nth) {
        long a = 0;
        long b = 1;
        long temp = 0;
        for (int i = 2; i <= nth; i++) {
            temp = a + b;
            a = b;
            b = temp;
        }
        return b;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        long fib = 0;
        if (n <= 0) {
            System.err.println("Input can only be greater than 0.");
        }
        if (n == 1) {
            fib = 0;
        }
        if (n == 2) {
            fib = 1;
        }
        if (n >= 3) {
            fib = Fibbonaci(n);
        }
        System.out.println("The " + n + "th fibbonaci number is " + fib + ".");
        sc.close();
    }
}