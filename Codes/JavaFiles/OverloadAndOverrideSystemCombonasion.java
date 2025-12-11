class InfosOfStudauntes {
    int id;
    String name;
    int score;
    void collect() {}
    void collect(int id, String name) {
        this.id = id;
        this.name = name;
    }
    void collect(int id, String name,int score) {
        this.id = id;
        this.name = name;
        this.score = score;
    }
    void display() {
        System.out.println(this.id + " | " + this.name + " | " + this.score);
    }
}
class SubClassification extends InfosOfStudauntes {
    @Override
    void collect(int id, String name) {
        this.id = id + 1;
        this.name = "Student " + name;
    }
}
public class OverloadAndOverrideSystemCombonasion {
    public static void main(String[] args) {
        InfosOfStudauntes ios = new InfosOfStudauntes();
        ios.collect(10, "Abby", 100);
        ios.display();
        SubClassification sc = new SubClassification();
        sc.collect(2,"Bob");
        sc.display();
        sc.collect(1,"Sim",129);
        sc.display();
    }
}