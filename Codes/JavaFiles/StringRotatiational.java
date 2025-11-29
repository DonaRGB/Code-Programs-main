import java.util.Scanner;
import java.math.BigInteger;
public class StringRotatiational {
    public static BigInteger rotate(BigInteger n, int k, String dir) {
        String sn = String.valueOf(n);
        int len = sn.length();
        k = k % len;
        BigInteger rtdn;
        if (dir.equalsIgnoreCase("left")) {
            rtdn = new BigInteger(sn.substring(k) + sn.substring(0, k));
        } else {
            rtdn = new BigInteger(sn.substring(len - k) + sn.substring(0, len - k));
        }
        return rtdn;
    }

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        String d = "";
        System.out.println("Enter a number to rotate :");
        BigInteger num = scn.nextBigInteger();
        System.out.println("Enter the number of digits to rotate :");
        int r = scn.nextInt();
        System.out.println("Enter the direction in which to rotate (left/right):");
        d = scn.next();
        if (d.equalsIgnoreCase("l") || d.equalsIgnoreCase("left")) {
            d = "left";
        } else {
            d = "right";
        }
        BigInteger rtd = rotate(num, r, d);
        System.out.println("The rotated form of " + num + " is " + rtd + ".");
        scn.close();
    }
}
