import java.lang.Math;
public class OOPSNumberTwo {
    private double[] data;
    private int dataSize;
    private double sum;
    public OOPSNumberTwo() {
        data = new double[100];
        dataSize = 0;
        sum = 0;
    }
    public void add(double value) {
        data[dataSize] = value;
        dataSize++;
        sum += value;
    }
    public double getAverage() {
        return (dataSize == 0) ? 0 : sum / dataSize;
    }
    public double getLowStandardDeviation() {
        double mean = getAverage();
        double sumOfSquares = 0.0;
        for (int i = 0; i < dataSize; i++) {
            double diff = data[i] - mean;
            sumOfSquares += diff * diff;
        }
        return Math.sqrt(sumOfSquares / dataSize);
    }
    public static double calculateAverage(OOPSNumberTwo[] datasets) {
        double total = 0.0;
        for (OOPSNumberTwo ds : datasets) {
            total += ds.getAverage();
        }
        return total / datasets.length;
    }
    @Override
    public String toString() {
        return "DataSet[Size = " + dataSize + ", Avg = " + getAverage() + "]";
    }
}