import java.util.Scanner;
public class MaxusMinusInputFinder {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num;
        int min = Integer.MIN_VALUE;
        int max = Integer.MAX_VALUE;
        char choice;
        do {
            System.out.println("Enter a number : ");
            num = sc.nextInt();
            if (num > max) {
                max = num;
            }
            if (num < min) {
                min = num;
            }
            System.out.println("Do you want to continue y/n? : ");
            choice = sc.next().charAt(0);
        } while (choice == 'y' || choice == 'Y');
        System.out.println("Largest number : " + max);
        System.out.println("Smallest number : " + min);
        sc.close();
    }
}