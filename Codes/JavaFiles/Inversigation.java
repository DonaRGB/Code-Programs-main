import java.util.Scanner;
public class Inversigation {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        System.out.println("Enter the number of elements in the array :");
        int n = scn.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter the " + n + " elements of the array :");
        for (int i = 0; i < n; i++) {
            arr[i] = scn.nextInt();
        }
        int[] inv = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            inv[arr[i]] = i;
        }
        System.out.println("The inverse of the array is :");
        for (int x : inv) {
            System.out.print(x + " ");
        }
        scn.close();
    }
}