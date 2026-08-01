public class AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAATest {
    public static void main(String[] args) {
        double x = -1000;
        double lastx = 0;
        double percentage = 0;
        String wordInDecreasing = "";
        double begin = x;
        double percentChange = 0;
        int count = 0;
        while (x < 500) {
            lastx = x;
            if (x > -1 & x < 0) {
                x *= -1.05;
            } else {
                if (x > 0) {
                    x *= 1.0025;
                } else {
                    x *= 0.9975;
                }
            }
            percentage = ((x - lastx) / x)*100;
            if (percentage < 0) {
                wordInDecreasing = "decrease";
            } else {
                wordInDecreasing = "increase";
            }
            System.out.println("x = " + x + ", % " + wordInDecreasing + " : " + percentage + "%");
            count += 1;
        }
        percentChange = ((x - begin) / begin) * 100;
        System.out.println("\nNumber of Iterations : " + count + "\nPercent Difference (" + begin + " - " + x + ") : " + percentChange + "%");
    }
}