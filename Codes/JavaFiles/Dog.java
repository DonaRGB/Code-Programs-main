public class Dog extends AnimalInheritance {
    private String breed;
    public Dog(String name, int age, String breed) {
        super(name, age);
        this.breed = breed;
    }
    public String getBreed() {
        return breed;
    }

    @Override
    public void makeSound() {
        System.out.println("The dog barks.");
    }
}