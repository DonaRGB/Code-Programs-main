import java.time.LocalDate;
abstract class Item {
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
class Book extends Item {
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
class DVD extends Item {
    private String director;
    private int runningTime;
    public DVD(String id, String title, LocalDate pD, String director, int rT) {
        super(id,title,pD,7);
        this.director = director;
        this.runningTime = rT;
    }
    public String getDirector() {return this.director;}
    public int getRunningTime() {return this.runningTime;}
}
class CD extends Item {
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
public class LibraryManagerator {
    public static void main(String[] args) {
        Book b = new Book("B001","1984",LocalDate.of(1949,6,8),"George Orwell",328);
        DVD d = new DVD("D001","Inception",LocalDate.of(2010,7,16),"Christhopher Nolan",148);
        CD c = new CD("C001","Thriller",LocalDate.of(1982,11,30),"Michael Jackson",9);
        System.out.println(b.getTitle());
        System.out.println(d.getTitle());
        System.out.println(c.getTitle());
    }
}