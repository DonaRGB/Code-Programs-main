import java.util.Scanner;
public class ArrayRepresentation {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        System.out.println("Enter the number of rows :");
        int nr = scn.nextInt();
        System.out.println("Enter the number of columns :");
        int nc = scn.nextInt();
        int[][] arr = new int[nr][nc];
        System.out.println("Enter the elements in the array :");
        for (int i = 0; i < nr; i++) {
            for (int j = 0; j < nc; j++) {
                arr[i][j] = scn.nextInt();
            }
        }
        System.out.println("The entered 2D array is :");
        for (int i = 0; i < nr; i++) {
            for (int j = 0; j < nc; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
        scn.close();
    }
}