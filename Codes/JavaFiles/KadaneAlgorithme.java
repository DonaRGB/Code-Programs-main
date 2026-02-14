import java.util.Scanner;
public class KadaneAlgorithme {
    static int maxSubArraySum(int[] a) {
        int size = a.length;
        int msf = Integer.MIN_VALUE;
        int meh = 0;
        for (int i = 0; i < size; i++) {
            meh += a[i];
            if (msf < meh) {
                msf = meh;
            }
            if (meh < 0) {
                meh = 0;
            }
        }
        return msf;
    }

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        System.out.println("Enter the number of elements in the array :");
        int n = scn.nextInt();
        int[] a = new int[n];
        System.out.println("Enter the elements in the array :");
        for (int i = 0; i < n; i++) {
            a[i] = scn.nextInt();
        }
        System.out.println("Maximum contiguous sum is " + maxSubArraySum(a));
        scn.close();
    }
}