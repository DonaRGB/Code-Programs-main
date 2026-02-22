import java.util.*;
public class ArrListACP {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        System.out.println("Enter the number of integers you want to input :");
        int n = scn.nextInt();
        ArrayList<Integer> al = new ArrayList<>();
        System.out.println("Enter the " + n + " integers :");
        for (int i = 0; i < n; i++) {
            al.add(scn.nextInt());
        }
        System.out.println("\nEnter the integer Q :");
        int q = scn.nextInt();
        if (q > 2) {
            q = (q % 2) + 1;
        } else {
            if (q < 1) {
                q -= (q + 1);
            }
        }
        if (q == 1) {
            System.out.println("Enter index p :");
            int p = scn.nextInt();
            if (p > n) {
                p = p % n;
            } else {
                if (p < 0) {
                    p = n - 1;
                }
            }
            System.out.println("Enter the integer r :");
            int r = scn.nextInt();
            al.add(p,r);
            System.out.println("The modified array is :");
            for (int i = 0; i < n; i++) {
                System.out.print(al.get(i) + "\t");
            }
        } else {
            System.out.println("Enter the integer to find, p :");
            int p = scn.nextInt();
            int lidx = al.lastIndexOf(p);
            System.out.println("The value " + p + " is at index " + lidx);
        }
        scn.close();
    }
}