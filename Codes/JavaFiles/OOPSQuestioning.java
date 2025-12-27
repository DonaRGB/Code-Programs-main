class Person {
    private String name;
    private int age;
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    public String getname() {
        return name;
    }
    public int getage() {
        return age;
    }
}
class Student extends Person {
    private String major;
    public Student(String name, int age, String major) {
        super(name,age);
        this.major = major;
    }
    public String getmajor() {
        return major;
    }
}
public class OOPSQuestioning {
    public static void main(String[] args) {
        Student stu = new Student("Alice",20,"Computer Science");
        System.out.println("Name : " + stu.getname());
        System.out.println("Age : " + stu.getage());
        System.out.println("Major : " + stu.getmajor());
    }
}