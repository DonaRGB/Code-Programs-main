import java.util.Scanner;
public class IsGreaterThanTen {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number : ");
        int num = sc.nextInt();
        if (num > 10) {
            System.out.println("Yes, I'm Greater!");
        } else {
            System.out.println("Sorry I feel bad");
        }
        sc.close();
    }
}