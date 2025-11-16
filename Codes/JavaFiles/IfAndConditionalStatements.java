import java.util.Scanner;
public class IfAndConditionalStatements {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        System.out.println("The String is \"" + str + "\".");
        int num = sc.nextInt();
        System.out.println("The Number is " + num + ".");
        float fnum = sc.nextFloat();
        System.out.println("The Floating Number is " + fnum + ".");
        sc.close();
    }
}