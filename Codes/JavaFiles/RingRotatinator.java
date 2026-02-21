import java.util.Scanner;
public class RingRotatinator {
    public static void main(String[] args) throws Exception {
        Scanner scn = new Scanner(System.in);
        System.out.println("Enter the number of rows :");
        int n = scn.nextInt();
        System.out.println("Enter the number of columns :");
        int m = scn.nextInt();
        int[][] arr = new int[n][m];
        System.out.println("Enter the elements in the " + n + " by " + m + " matrix :");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                arr[i][j] = scn.nextInt();
            }
        }
        System.out.println("Enter the ring number (sno) :");
        int sno = scn.nextInt();
        System.out.println("Enter the number of rotations (rno) :");
        int rno  = scn.nextInt();
        ringrotate(arr,sno,rno);
        display(arr);
        scn.close();
    }
    public static void ringrotate(int[][] arr, int sno, int rno) {
        int[] la = fill1Dfrom2D(arr,sno);
        rotate1D(la,rno);
        fill2Dfrom1D(arr,la,sno);
    } 
    public static int[] fill1Dfrom2D(int[][] arr, int sno) {
        int rmin = sno - 1;
        int cmin = sno - 1;
        int rmax = arr.length - sno;
        int cmax = arr[0].length - sno;
        int sz = 2 * (rmax - rmin + cmax - cmin);
        int[] la = new int[sz];
        int idx = 0;
        for (int r = rmin; r <= rmax; r++) {
            la[idx] = arr[r][cmin];
            idx++;
        }
        cmin++;
        for (int c = cmin; c <= cmax; c++) {
            la[idx] = arr[rmax][c];
            idx++;
        }
        rmax--;
        for (int r = rmax; r >= rmin; r--) {
            la[idx] = arr[r][cmax];
            idx++;
        }
        cmax--;
        for (int c = cmax; c >= cmin; c--) {
            la[idx] = arr[rmin][c];
            idx++;
        }
        rmin++;
        return la;
    }
    public static void rotate1D(int[] la, int rno) {
        rno = rno % la.length;
        if (rno < 0) {
            rno += la.length;
        }
        reverse(la,0,la.length - 1);
        reverse(la,0,rno - 1);
        reverse(la,rno,la.length - 1);
    }
    public static void reverse(int[] la, int left, int right) {
        while (left < right) {
            int temp = la[left];
            la[left] = la[right];
            la[right] = temp;
            left++;
            right--;
        }
    }
    public static void fill2Dfrom1D(int[][] arr, int[] la, int sno) {
        int rmin = sno - 1;
        int cmin = sno - 1;
        int rmax = arr.length - sno;
        int cmax = arr[0].length - sno;
        int idx = 0;
        for (int r = rmin; r <= rmax; r++) {
            arr[r][cmin] = la[idx];
            idx++;
        }
        cmin++;
        for (int c = cmin; c <= cmax; c++) {
            arr[rmax][c] = la[idx];
            idx++;
        }
        rmax--;
        for (int r = rmax; r >= rmin; r--) {
            arr[r][cmax] = la[idx];
            idx++;
        }
        cmax--;
        for (int c = cmax; c > cmin; c--) {
            arr[rmin][c] = la[idx];
            idx++;
        }
        rmin++;
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