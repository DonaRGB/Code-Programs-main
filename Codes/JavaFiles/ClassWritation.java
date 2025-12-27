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
        super(name, age);
        this.major = major;
    }

    public String getmajor() {
        return major;
    }
}
class Book {
    private String title;
    private String author;
    private int numPages;
    public Book(String t, String a, int np) {
        this.title = t;
        this.author = a;
        this.numPages = np;
    }
    public String getTitle() {
        return title;
    }
    public String getAuthor() {
        return author;
    }
    public int getNumPages() {
        return numPages;
    }
}
public class ClassWritation {
    public static void main(String[] args) {
        Student stu = new Student("John Doe",20,"Computer Science");
        Book b = new Book("The Hobbit","J.R.R. Tolken",295);
        System.out.println("Student Information :\nName : " + stu.getname() + "\nAge : " + stu.getage() + "\nMajor : " + stu.getmajor());
        System.out.println("\nBook Information :\nTitle : " + b.getTitle() + "\nAuthor : " + b.getAuthor() + "\nNumber of Pages : " + b.getNumPages());
    }
}