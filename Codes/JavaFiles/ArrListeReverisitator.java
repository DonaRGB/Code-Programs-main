import java.util.*;
public class ArrListeReverisitator {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        System.out.print("Enter the number of elements in the list : ");
        int n = scn.nextInt();
        ArrayList<Integer> al = new ArrayList<>();
        System.out.println("Enter the " + n + " integers : ");
        for (int i = 0; i < n; i++) {
            al.add(scn.nextInt());
        }
        ArrayList<Integer> ans = reverse(al);
        System.out.println("Reversed List : " + ans);
        scn.close();
    }
    public static ArrayList<Integer> reverse(ArrayList<Integer> list) {
        ArrayList<Integer> ans = new ArrayList<Integer>();
        for (int i = list.size() - 1; i >= 0; i--) {
            ans.add(list.get(i));
        }
        return ans;
    }
}