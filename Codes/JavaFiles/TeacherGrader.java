import java.util.Scanner;
public class TeacherGrader {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a num : ");
        int marks = sc.nextInt();
        if (marks > 90) {
            System.out.println("O");
        } else if (marks <= 90 && marks >80) {
            System.out.println("A+");
        } else if (marks <= 80 && marks > 70) {
            System.out.println("A");
        } else if (marks <= 70 && marks > 60) {
            System.out.println("B");
        } else {
            System.out.println("C");
        }
        sc.close();
    }
}