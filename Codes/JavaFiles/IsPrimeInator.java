import java.util.Scanner;
public class IsPrimeInator {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int num = scn.nextInt();
        for (int i = 1; i <= num; i++) {
            int n = scn.nextInt();
            int count = 0;
            for (int div = 2; div * div <= n; div++) {
                if (n % div == 0) {
                    count++;
                    break;
                }
            }
            if (count == 0) {
                System.out.println(num + " is prime.");
            } else {
                System.out.println(num + " is not prime.");
            }
        }
        scn.close();
    }
}
