import java.util.Scanner;
public class SaddlePointalizer {
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
        int[] rmin = new int[n];
        int[] cmax = new int[n];
        for (int i = 0; i < n; i++) {
            rmin[i] = arr[i][0];
            for (int j = 1; j < n; j++) {
                if (arr[i][j] < rmin[i]) {
                    rmin[i] = arr[i][j];
                }
            }
        }
        for (int j = 0; j < n; j++) {
            cmax[j] = arr[0][j];
            for (int i = 1; i < n; i++) {
                if (arr[i][j] > cmax[j]) {
                    cmax[j] = arr[i][j];
                }
            }
        }
        boolean saddleFound = false;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (arr[i][j] == rmin[i] && arr[i][j] == cmax[j]) {
                    System.out.println("Saddle point at (" + i + ", " + j + ") : " + arr[i][j]);
                    saddleFound = true;
                }
            }
        }
        if (!saddleFound) {
            System.out.println("No saddle points found.");
        }
        System.out.println("\nMatrix with highlighted saddle points (enclosed in brackets []) :");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (arr[i][j] == rmin[i] && arr[i][j] == cmax[j]) {
                    System.out.print("[" + arr[i][j] + "]\t");
                } else {
                    System.out.print(arr[i][j] + "\t");
                }
            }
            System.out.println();
        }
        scn.close();
    }
}