public class Cat extends AnimalInheritance {
    private boolean isIndoors;
    public Cat(String name, int age, boolean isIndoors) {
        super(name, age);
        this.isIndoors = isIndoors;
    }
    public boolean getIsIndoors() {
        return isIndoors;
    }

    @Override
    public void makeSound() {
        System.out.println("The cat meows.");
    }
}