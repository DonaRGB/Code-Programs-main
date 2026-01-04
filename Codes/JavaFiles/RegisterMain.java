public class RegisterMain {
    public static void main(String[] args) {
        Register r = new Register();
        r.recordPurchase(1000.0);
        r.recordPayment(10000.0);
        System.out.println("Change : " + r.giveChange() + "\n");
        Register[] registers = new Register[3];
        
        Register r1 = new Register();
        r1.recordPayment(100);
        r1.recordPurchase(10);
        r1.recordPurchase(10);
        r1.recordPurchase(10);
        r1.recordPurchase(10);
        r1.recordPurchase(10);

        Register r2 = new Register();
        r2.recordPayment(100);
        r2.recordPurchase(90);

        Register r3 = new Register();
        r3.recordPayment(1500);
        r3.recordPurchase(1000);
        r3.recordPurchase(250);

        registers[0] = r1;
        registers[1] = r2;
        registers[2] = r3;
        
        System.out.println("Total Purchases : " + Register.countTotal(registers));
    }
}