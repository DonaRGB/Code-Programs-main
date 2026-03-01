import java.util.*;
public class FirstSwapLastArrayingListeristics {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        System.out.print("Enter the number of elements in the list : ");
        int n = scn.nextInt();
        ArrayList<Integer> al = new ArrayList<>();
        System.out.println("Enter the " + n + " integers : ");
        for (int i = 0; i < n; i++) {
            al.add(scn.nextInt());
        }
        System.out.println("\nSwapping first and last elements...\n");
        swapLastFirst(al);
        System.out.println("The altered ArrayList is : " + al);
        scn.close();
    }
    public static void swapLastFirst(ArrayList<Integer> list) {
        if (list.size() > 1) {
            Collections.swap(list, 0, list.size() - 1);
        }
    }
}