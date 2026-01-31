import java.time.LocalDate;
public abstract class Item {
    private String id;
    private String title;
    private LocalDate publicationDate;
    private int maxCheckoutDays;
    public Item(String id, String title, LocalDate pD, int mCD) {
        this.id = id;
        this.title = title;
        this.publicationDate = pD;
        this.maxCheckoutDays = mCD;
    }
    public String getID() {
        return this.id;
    }
    public String getTitle() {
        return this.title;
    }
    public LocalDate getPublicationDate() {
        return this.publicationDate;
    }
    public int getMaxCheckoutDays() {
        return this.maxCheckoutDays;
    }
}
public class Book extends Item {
    private String author;
    private int pages;
    public Book(String id, String title, LocalDate pD, String author, int pages) {
        super(id,title,pD,21);
        this.author = author;
        this.pages = pages;
    }
    public String getAuthor() {return this.author;}
    public int getPages() {return this.pages;}
}
public class DVD extends Item {
    private String director;
    private int runningTime;
    public DVD(String id, String titlee, LocalDate pD, String director, int rT) {
        super(id,title,pD,7);
        this.director = director;
        this.runningTime = rT;
    }
    public String getDirector() {return this.director;}
    public int getRunningTime() {return this.runningTime;}
}
public class CD extends Item {
    private String artist;
    private int tracks;
    public CD(String id, String title, LocalDate pD, String artist, int tracks) {
        super(id,title,pD,14);
        this.artist = artist;
        this.tracks = tracks;
    }
    public String getArtist() {return this.artist;}
    public int getTracks() {return this.tracks;}
}
public class Main {
    public static void main(String[] args) {
        Book b = Book("B001","1984",LocalDate.of(1949,6,8),"George Orwell",328);
        DVD d = DVD("D001","Inception",LocalDate.of(2010,7,16),"Christhopher Nolan",148);
        CD c = CD("C001","Thriller",LocalDate.of(1982,11,30),"Michael Jackson",9);
    }
}