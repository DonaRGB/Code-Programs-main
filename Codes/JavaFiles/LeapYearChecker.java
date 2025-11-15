import java.util.Scanner;
public class LeapYearChecker {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a year : ");
        int year = sc.nextInt();
        boolean isLeapYear = (year % 400 == 0) ? true:(year % 100 == 0) ? false:(year % 4 == 0) ? true:false;
        String isLeapYearAsWord = isLeapYear ? " is a leap year.":"is not a leap year.";
        System.out.println("The year " + year + isLeapYearAsWord);
    }
}
