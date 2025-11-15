import java.util.Scanner;
public class LeapYearChecker {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a year : ");
        int yearinput = sc.nextInt();
        String text = isYearALeapYear(yearinput);
        System.out.println(text);
    }
    public static String isYearALeapYear(int year) {
        boolean isLeapYear = (year % 400 == 0) ? true : (year % 100 == 0) ? false : (year % 4 == 0) ? true : false;
        String isLeapYearAsWord = isLeapYear ? " is a leap year." : "is not a leap year.";
        return "The year " + year + isLeapYearAsWord;
    }
}
