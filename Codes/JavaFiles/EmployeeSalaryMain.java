import java.util.Scanner;
public class EmployeeSalaryMain {
    public static Employee getEmployeeDetails() {
        Scanner scn = new Scanner(System.in);
        int id;
        String name;
        double salary;
        System.out.println("Enter id :");
        id = scn.nextInt();
        System.out.println("Enter name :");
        name =  scn.nextLine();
        System.out.println("Enter salary : ");
        salary = scn.nextDouble();
        Employee emp = new Employee();
        emp.setEmployeeID(id);;
        emp.setEmployeeName(name);;
        emp.setEmployeeSalary(salary);;
        scn.close();
        return emp;
    }
    public static int getPFPercentage() {
        Scanner scn = new Scanner(System.in);
        int pfp;
        System.out.println("Enter PF Percentage :");
        pfp = scn.nextInt();
        scn.close();
        return pfp;
    }
    public static void main(String[] args) {
        Employee emp = getEmployeeDetails();
        int pfp = getPFPercentage();
        emp.calculateNetSalary(pfp);
        System.out.println("ID : " + emp);
        System.out.println("Name : " + emp);
        System.out.println("Salary : " + emp);
        System.out.println("Net Salary : " + emp);
    }
}
class Employee {
    private int id;
    private String name;
    private double salary;
    private double netSalary;
    public int getEmployeeID() {
        return id;
    }
    public String getEmployeeName() {
        return name;
    }
    public double getEmployeeSalary() {
        return salary;
    }
    public double getEmployeeNetSalary() {
        return netSalary;
    }
    public void setEmployeeID(int id) {
        this.id = id;
    }
    public void setEmployeeName(String name) {
        this.name = name;
    }
    public void setEmployeeSalary(double salary) {
        this.salary = salary;
    }
    public void calculateNetSalary(int pfp) {
        double pfa = (salary * pfp) / 100;
        this.netSalary = salary - pfa;
    }
}