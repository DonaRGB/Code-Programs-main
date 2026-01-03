public class Instantation {
    public static void main(String[] args) {
        OOPSNumberTwo dataset = new OOPSNumberTwo();
        dataset.add(10);
        dataset.add(12);
        dataset.add(14);
        dataset.add(16);
        dataset.add(18);
        System.out.println("Standard Deviation : " + dataset.getLowStandardDeviation());
        OOPSNumberTwo datasets = new OOPSNumberTwo[3];
        OOPSNumberTwo ds1 = new OOPSNumberTwo();
        ds1.add(2);
        ds1.add(4);
        ds1.add(6);
        OOPSNumberTwo ds2 = new OOPSNumberTwo();
        ds2.add(1);
        ds2.add(3);
        ds2.add(5);
        OOPSNumberTwo ds3 = new OOPSNumberTwo();
        ds3.add(10);
        ds3.add(20);
        datasets[0] = ds1;
        datasets[1] = ds2;
        datasets[2] = ds3;
        System.out.println("Average of Averages : " + datasets.calculateAverage());
    }
}