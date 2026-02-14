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
        int min = 0;
        int max = 6;
        int rmx = nr - 1;
        int cmx = nc - 1;
        int count = 0;
        System.out.println("Spiral order traversal of the array :");
        while (count < nr + nc) {
            for (int c = min; c <= max && count < nr + nc; c++) {
                System.out.println(arr[c][count] + " ");
                count++;
            }
            for (int r = min; r <= max && count < nr + nc; r++) {
                System.out.println(arr[r][rmx - count] + " ");
                count++;
            }
            for (int c = max; c >= min && count < nr + nc; c--) {
                System.out.println(arr[cmx][c] + " ");
                count++;
            }
            for (int r = max; r >= min && count < nr + nc; r--) {
                System.out.println(arr[r][min + count] + " ");
                count++;
            }
        }
        scn.close();
    }
}