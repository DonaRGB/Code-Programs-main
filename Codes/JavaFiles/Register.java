public class Register {
    private double purchase;
    private double payment;
    private int purchaseCount;
    public Register() {
        purchase = 0;
        payment = 0;
        purchaseCount = 0;
    }
    public void recordPurchase(double amount) {
        purchase += amount;
        purchaseCount++;
    }
    public void recordPayment(double amount) {
        payment += amount;
    }
    public double giveChange() {
        double change = payment - purchase;
        purchase = 0;
        payment = 0;
        return change;
    }
    public int getItemCount() {
        return purchaseCount;
    }
    public static int countTotal(Register[] registers) {
        int total = 0;
        for (Register reg : registers) {
            total += reg.getItemCount();
        }
        return total;
    }

    @Override
    public String toString() {
        return "Register[Purchase = " + purchase + ", Payment = " + payment + ", Change = " + giveChange() + ", Item Count = " + getItemCount() + "]";
    }
}