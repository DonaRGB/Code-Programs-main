import java.util.ArrayList;
class Student {
    private String name;
    private int id;
    private ArrayList<Course> courses;
    public Student(String name, int id) {
        this.name = name;
        this.id = id;
        courses = new ArrayList<>();
    }
    public void addCourse(Course c) {
        courses.add(c);
    }
    public void removeCourse(Course c) {
        courses.remove(c);
    }
    public double getGPA() {
        if (courses.isEmpty()) return 0.0;
        double total;
        for (Course cou : courses) {
            total += cou.getGrade();
        }
        return total / courses.size();
    }
    public String getTranscript() {
        StringBuilder transcript = new StringBuilder();
        transcript.append("Name : ").append(name).append("\n").append("ID : ").append(id).append("\n");
        for (Course co : courses) {
            transcript.append("Course : ").append(co.getName()).append(" (").append(co.getCredits()).append(" credits)\n").append("Grade : ").append(co.getGrade()).append(" (").append(co.getLetterGrade()).append(")\n\n");
        }
        return transcript.toString();
    }
}
public class CourseMainFile {
    public static void main(String[] args) {
        Course cs = new Course("Computer Science",4.0);
        cs.setGrade(3.7);
        Student alice = new Student("Alice",1234);
        alice.addCourse(cs);
        System.out.println("Alice\'s Intial GPA : " + alice.getGPA());
        Course math = new Course("Math",3.0);
        alice.addCourse(math);
        System.out.println("Alice\'s Updated GPA : " + alice.getGPA());
        Course csBob = new Course("Computer Science",4.0);
        csBob.setGrade(3.0);
        Course mathBob = new Course("Math",3.0);
        mathBob.setGrade(3.5);
        Student bob = new Student("Bob",5678);
        bob.addCourse(csBob);
        bob.addCourse(mathBob);
        System.out.println("\n Bob\'s GPA : " + bob.getGPA());
        System.out.println("Bob\'s Transcript :\n" + bob.getTranscript());
    }
}