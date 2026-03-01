import java.util.*;
public class ArrayListeTrializer {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        System.out.print("Enter the number of arrays you want to input : ");
        int n = scn.nextInt();
        ArrayList<ArrayList<Integer>> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            System.out.print("Enter the size of array " + (i+1) + " : ");
            int n1 = scn.nextInt();
            ArrayList<Integer> l2 = new ArrayList<>();
            System.out.println("Enter the " + n1 + " elements of array " + (i+1) + " : ");
            for (int j = 0; j < n1; j++) {
                l2.add(scn.nextInt());
            }
            list.add(i,l2);
        }
        System.out.print("Enter the number of queries to process : ");
        int num = scn.nextInt();
        for (int k = 0; k < num; k++) {
            System.out.print("Enter row and column for query " + (k+1) + " : ");
            int m = scn.nextInt();
            int o = scn.nextInt();
            try {
                System.out.println("Element at (" + m + ", " + o + ") : " + list.get(m - 1).get(o - 1));
            } catch (Exception e) {
                System.err.println("ERROR!");
            }
        }
        scn.close();
    }
}