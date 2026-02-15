import java.util.Scanner;
public class Spiralinator {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        System.out.println("Enter the numbr of rows :");
        int nr = scn.nextInt();
        System.out.println("Enter the numeber of columns :");
        int nc = scn.nextInt();
        if (nr == 0 || nc == 0) {
            System.err.println("Array dimensions cannot be zero.");
            scn.close();
            return;
        }
        int[][] arr = new int[nr][nc];
        System.out.println("Enter the elements in the array :");
        for (int i = 0; i < nr; i++) {
            for (int j = 0; j < nc; j++) {
                arr[i][j] = scn.nextInt();
            }
        }
        int t = 0;
        int b = nr - 1;
        int l = 0;
        int r = nc - 1;
        System.out.println("Spiral order traversal of the array :");
        while (t <= b && l <= r) {
            for (int i = l; i <= r; i++) {
                System.out.print(arr[t][i] + " ");
            }
            t++;
            for (int i = t; i <= b; i++) {
                System.out.print(arr[i][r] + " ");
            }
            r--;
            if (t <= b) {
                for (int i = r; i >= l; i--) {
                    System.out.print(arr[b][i] + " ");
                }
                b--;
            }
            if (l <= r) {
                for (int i = b; i >= t; i--) {
                    System.out.print(arr[i][l] + " ");
                }
                l++;
            }
        }
        scn.close();
    }
}