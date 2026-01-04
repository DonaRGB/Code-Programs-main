public class AnimalInheritingMain {
    public static void main(String[] args) {
        AnimalInheritance a = new AnimalInheritance("Mickey",5);
        Dog d = new Dog("Rex",3,"Golden Retriever");
        Cat c = new Cat("Whiskers",5,true);
        a.makeSound();
        System.out.println(a.getName() + " is " + a.getAge() + " years old.");
        d.makeSound();
        System.out.println(d.getName() + " is a " + d.getBreed() + " and is " + d.getAge() + " years old.");
        c.makeSound();
        System.out.println(c.getName() + " is " + c.getAge() + " years old and is " + (c.getIsIndoors() ? "indoors" : "outdoors") + ".");
    }
}