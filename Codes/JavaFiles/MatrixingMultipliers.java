import java.util.Scanner;
public class MatrixingMultipliers {
    public static int[][] inputMatrix(int rows, int cols) {
        Scanner scn = new Scanner(System.in);
        int[][] matrix = new int[rows][cols];
        System.out.println("Enter the elements in the matrix :");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                matrix[i][j] = scn.nextInt();
            }
        }
        scn.close();
        return matrix;
    }
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        System.out.println("Enter the number of rows of Matrix A :");
        int rA = scn.nextInt();
        System.out.println("Enter the number of columns of Matrix A :");
        int cA = scn.nextInt();
        int[][] mA = new int[rA][cA];
        System.out.println("Enter the elements in Matrix A :");
        for (int i = 0; i < rA; i++) {
            for (int j = 0; j < cA; j++) {
                mA[i][j] = scn.nextInt();
            }
        }
        System.out.println("Enter the number of rows of Matrix B :");
        int rB = scn.nextInt();
        System.out.println("Enter the number of columns of Matrix B :");
        int cB = scn.nextInt();
        int[][] mB = new int[rB][cB];
        System.out.println("Enter the elements in Matrix B :");
        for (int i = 0; i < rB; i++) {
            for (int j = 0; j < cB; j++) {
                mB[i][j] = scn.nextInt();
            }
        }
        if (cA != rB) {
            System.out.println("⚠️ Error : Matrix multiplication not possible\\nColumns of Matrix A must equal Rows of Matrix B");
            scn.close();
            return;
        }
        int[][] answer = new int[rA][cB];
        for (int i = 0; i < rA; i++) {
            for (int j = 0; j < cB; j++) {
                for (int k = 0; k < cA; k++) {
                    answer[i][j] += mA[i][k] * mB[k][j];
                }
            }
        }
        System.out.println("The result of multiplying Matrix A :");
        for (int i = 0; i < rA; i++) {
            for (int j = 0; j < cA; j++) {
                System.out.print(mA[i][j] + "\t");
            }
            System.out.println();
        }
        System.out.println("and Matrix B :");
        for (int i = 0; i < rB; i++) {
            for (int j = 0; j < cB; j++) {
                System.out.print(mB[i][j] + "\t");
            }
            System.out.println();
        }
        System.out.println("is");
        for (int i = 0; i < answer.length; i++) {
            for (int j = 0; j < answer[0].length; j++) {
                System.out.print(answer[i][j] + "\t");
            }
            System.out.println();
        }
        scn.close();
    }
}