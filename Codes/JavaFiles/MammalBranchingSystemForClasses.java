class Mammals {
    void mam() {
        System.out.println("Inside Mammal Class");
    }
}
class Lion extends Mammals {
    void roar() {
        System.out.println("Inside Lion Class");
    }
}
class Human extends Mammals {
    void hum() {
        System.out.println("Inside Human Class");
    }
}
public class MammalBranchingSystemForClasses {
    public static void main(String[] args) {
        Lion obj = new Lion();
        Human person = new Human();
        obj.roar();
        obj.mam();
        person.hum();
        person.mam();
    }
}