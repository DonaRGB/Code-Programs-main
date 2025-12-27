import java.util.*;
class Digits {
    private ArrayList<Integer> digitList;
    public Digits(int num) {
        digitList = new ArrayList<>();
        if (num == 0) {
            digitList.add(0);
        }
        while (num > 0) {
            digitList.add(0,num % 10);
            num /= 10;
        }
    }
    public ArrayList<Integer> getDigitList() {
        return digitList;
    }
}
public class CumulatingEachOfThemDigits {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        System.out.println("Enter the number to be digitized (must be an integer!) :");
        int num = scn.nextInt();
        Digits d = new Digits(num);
        System.out.println("The digits are " + d.getDigitList());
    }
}