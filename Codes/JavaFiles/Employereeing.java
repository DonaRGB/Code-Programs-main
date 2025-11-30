class Employee {
    int empno;
    String name;
    float sal;
    Employee() {
        System.out.println("*****");
        empno = 808;
        name = "Bob";
        sal = 5000f;
    }
    void displayDetails() {
        System.out.println(empno + "|" + name + "|" + sal);
    }
}
public class Employereeing {
    public static void main(String[] args) {
        Employee emp1 = new Employee();
        Employee emp2 = new Employee();
        Employee emp3 = new Employee();
        emp1.displayDetails();
        emp2.displayDetails();
        emp3.displayDetails();
    }
}