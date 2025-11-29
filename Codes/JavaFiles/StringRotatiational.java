import java.util.Scanner;
import java.math.BigInteger;

public class StringRotatiational {
    public static BigInteger rotate(BigInteger n, int k, boolean dir, int digits) {
        BigInteger sign = n.signum() < 0 ? BigInteger.valueOf(-1) : BigInteger.ONE;
        n = n.abs();
        BigInteger powDigits = BigInteger.TEN.pow(digits);
        n = n.mod(powDigits);
        k = k % digits;
        if (k == 0)
            return n.multiply(sign);
        BigInteger lp, rp;
        if (dir) {
            BigInteger move = BigInteger.TEN.pow(digits - k);
            lp = n.mod(move);
            rp = n.divide(move);
            n = lp.multiply(BigInteger.TEN.pow(k)).add(rp);
        } else {
            BigInteger move = BigInteger.TEN.pow(k);
            lp = n.divide(move);
            rp = n.mod(move);
            n = rp.multiply(BigInteger.TEN.pow(digits - k)).add(lp);
        }
        return n.multiply(sign);
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
        boolean db;
        if (d.equalsIgnoreCase("l") || d.equalsIgnoreCase("left")) {
            db = true;
        } else {
            db = false;
        }
        System.out.println("Enter the number of digits to keep :");
        int dtokeep = scn.nextInt();
        BigInteger rtd = rotate(num, r, db, dtokeep);
        System.out.println("The rotated form of " + num + " is " + rtd + ".");
        scn.close();
    }
}
