class Hillstations {
    void location() {
        System.out.println("Location is :");
    }
    void famousfor() {
        System.out.println("Famous for :");
    }
}
class Manali extends Hillstations {
    void location() {
        System.out.println("Manali is in Himachal Pradesh.");
    }
    void famousfor() {
        System.out.println("It is famous for Hadimba Temple and adventure sports.");
    }
}
class Mussoorie extends Hillstations {
    void location() {
        System.out.println("Mussoorie is in Uttarakhand.");
    }
    void famousfor() {
        System.out.println("It is famous for educational institutions.");
    }
}
class Gulmarg extends Hillstations {
    void location() {
        System.out.println("Gulmarg is in Jammu.");
    }
    void famousfor() {
        System.out.println("It is famous for skiing.");
    }
}
public class PolymorphisingOfNamingFamousThingsFamousPeopleDid {
    public static void main(String[] args) {
        Hillstations A = new Hillstations();
        Hillstations M = new Manali();
        Hillstations Mu = new Mussoorie();
        Hillstations G = new Gulmarg();
        A.location();
        A.famousfor();
        M.location();
        M.famousfor();
        Mu.location();
        Mu.famousfor();
        G.location();
        G.famousfor();
    }
}