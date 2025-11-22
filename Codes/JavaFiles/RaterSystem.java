import java.util.Scanner;
public class RaterSystem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a rating number (must be greater than 0!) : ");
        int rating = sc.nextInt();
        System.out.println("Rating : ");
        if (rating > 5000 && rating <= 25000) {
            System.out.print("Good");
        } else if (rating > 25000 && rating <= 45000) {
            System.out.print("Better");
        } else if (rating > 45000 && rating <= 75000) {
            System.out.print("Best");
        } else if (rating > 75000) {
            System.out.print("Out of this world");
        } else {
            System.out.print("Not very satisfactory");
        }
        sc.close();
    }
}
