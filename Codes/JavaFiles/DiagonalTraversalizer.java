import java.util.Scanner;
public class DiagonalTraversalizer {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        System.out.println("Enter the size of the matrix (n * n) :");
        int n = scn.nextInt();
        if (n <= 0) {
            System.err.println("⚠️ Error : Size cannot be zero or less!");
        }
        int[][] arr = new int[n][n];
        System.out.println("Enter the elements in the " + n + " by " + n + " matrix :");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                arr[i][j] = scn.nextInt();
            }
        }
        System.out.println("The diagonally traversed matrix :");
        for (int move = 0; move < n; move++) {
            int i = 0;
            int j = move;
            while (i < n && j < n) {
                System.out.print(arr[i][j] + " ");
                i++;
                j++;
            }
            System.out.println();
        }
        for (int move = 1; move < n; move++) {
            int i = move;
            int j = 0;
            while (i < n && j < n) {
                System.out.print(arr[i][j] + " ");
                i++;
                j++;
            }
            System.out.println();
        }
        scn.close();
    }
}