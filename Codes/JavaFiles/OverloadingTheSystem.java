class Student {
    int id;
    String name;
    float stipend;
    Student() {}
    Student(int id, String name) {
        this.id = id;
        this.name = name;
    }
    Student(int id, String name, float stipend) {
        this.id = id;
        this.name = name;
        this.stipend = stipend;
    }
    void displayDetails() {
        System.out.println(this.id + "|" + this.name + "|" + this.stipend);
    }
}
public class OverloadingTheSystem {
    public static void main(String[] args) {
        Student st1 = new Student();
        Student st2 = new Student(24,"Abby");
        Student st3 = new Student(21,"Bob",110001);
        st1.displayDetails();
        st2.displayDetails();
        st3.displayDetails();
    }
}