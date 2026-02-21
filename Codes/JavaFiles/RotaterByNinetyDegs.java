import java.util.Scanner;
public class RotaterByNinetyDegs {
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
        rotateby90(arr);
        System.out.println("The rotated matrix is :");
        display(arr);
        scn.close();
    }
    public static void rotateby90(int[][] arr) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                int temp = arr[i][j];
                arr[i][j] = arr[j][i];
                arr[j][i] = temp;
            }
        }
        for (int i = 0; i < arr.length; i++) {
            int left = 0;
            int right = arr[i].length - 1;
            while (left < right) {
                int temp = arr[i][left];
                arr[i][left]= arr[i][right];
                arr[i][right] = temp;
                left++;
                right--;
            }
        }
    }
    public static void display(int[][] arr) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }
}