public class AnimalInheritance {
    private String name;
    private int age;
    public AnimalInheritance(String name, int age) {
        this.name = name;
        this.age = age;
    }
    public String getName() {
        return name;
    }
    public int getAge() {
        return age;
    }
    public void makeSound() {
        System.out.println("The animal makes a sound.");
    }
}