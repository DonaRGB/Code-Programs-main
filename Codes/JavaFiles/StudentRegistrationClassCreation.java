import java.util.Scanner;
class StudentDetails {
    int id;
    String name;
    int classs;
    public StudentDetails(int idin, String namein, int classsin) {
        this.id = idin;
        this.name = namein;
        this.classs = classsin;
    }
    public void show() {
        System.out.println(id + "|" + name + "|" + classs);
    }
}
public class StudentRegistrationClassCreation {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        System.out.println("Input the name of the student :");
        String n = scn.nextLine();
        System.out.println("Input the student's ID :");
        int i = scn.nextInt();
        System.out.println("Input the student's class no. :");
        int c = scn.nextInt();
        StudentDetails s = new StudentDetails(i, n, c);
        s.show();
        scn.close();
    }
}