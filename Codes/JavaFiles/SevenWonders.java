class wonders {
    void name() {
        System.out.println("Name is :");
    }
    void loc() {
        System.out.println("Located in :");
    }
}
class StatueOfLiberty extends wonders {
    void name() {
        System.out.println("I am the Statue of Liberty.");
    }
    void loc() {
        System.out.println("I am located on Liberty Island in New York Harbor, New York City, USA.");
    }
}
class PyramidsOfGiza extends wonders {
    void name() {
        System.out.println("I am the Pyramids of Giza.");
    }
    void loc() {
        System.out.println("I am located in Giza, Egypt.");
    }
}
class GreatWall extends wonders {
    void name() {
        System.out.println("I am the Great Wall of China.");
    }
    void loc() {
        System.out.println("I am located in Northern China.");
    }
}
class TajMahal extends wonders {
    void name() {
        System.out.println("I am the Taj Mahal.");
    }
    void loc() {
        System.out.println("I am located in Agra, Uttar Pradesh, India.");
    }
}
class Colosseum extends wonders {
    void name() {
        System.out.println("I am the Colosseum.");
    }
    void loc() {
        System.out.println("I am located in Rome, Italy.");
    }
}
class ChristTheRedeemer extends wonders {
    void name() {
        System.out.println("I am the Christ the Redeemer.");
    }
    void loc() {
        System.out.println("I am located in Rio de Janeiro, Brazil.");
    }
}
class ChichenItza extends wonders {
    void name() {
        System.out.println("I am the Chichén Itzá.");
    }
    void loc() {
        System.out.println("I am located in Yucatán, Mexico.");
    }
}
public class SevenWonders {
    public static void main(String[] args) {
        wonders W = new wonders();
        wonders SOL = new StatueOfLiberty();
        wonders POG = new PyramidsOfGiza();
        wonders GWOC = new GreatWall();
        wonders TM = new TajMahal();
        wonders C = new Colosseum();
        wonders CTR = new ChristTheRedeemer();
        wonders CI = new ChichenItza();
        W.name();
        W.loc();
        SOL.name();
        SOL.loc();
        POG.name();
        POG.loc();
        GWOC.name();
        GWOC.loc();
        TM.name();
        TM.loc();
        C.name();
        C.loc();
        CTR.name();
        CTR.loc();
        CI.name();
        CI.loc();
    }
}
