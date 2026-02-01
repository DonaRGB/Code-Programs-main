import java.util.Scanner;
public class Spannerator {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        System.out.println("Enter the number of elements in the array :");
        int n = scn.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter the " + n + " elements of the array :");
        for (int i = 0; i < n; i++) {
            arr[i] = scn.nextInt();
        }
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            if (max < arr[i]) {
                max = arr[i];
            }
        }
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            if (max > arr[i]) {
                min = arr[i];
            }
        }
        int span = max - min;
        System.out.println("The span of this array is " + span + ".");
        scn.close();
    }
}