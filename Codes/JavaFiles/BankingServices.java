import java.util.Scanner;
class InvalidMenuException extends Exception {
    public InvalidMenuException(String message) {
        super(message);
    }
}
class MinimumBalanceException extends Exception {
    public MinimumBalanceException(String message) {
        super(message);
    }
}
class InsufficientFundsException extends Exception {
    public InsufficientFundsException(String message) {
        super(message);
    }
}
class InvalidAmountException extends Exception {
    public InvalidAmountException(String message) {
        super(message);
    }
}
class BankAccount {
    private double balance;
    private static final double MIN_OPERATING_BALANCE = 500.0;
    public BankAccount(double opening_balance) throws MinimumBalanceException {
        if (opening_balance < MIN_OPERATING_BALANCE) {
            throw new MinimumBalanceException("Opening balance must be at least $" + MIN_OPERATING_BALANCE);
        }
        this.balance = opening_balance;
    }
    public void deposit(double amount) throws InvalidAmountException {
        if (amount <= 0) {
            throw new InvalidAmountException("Deposit amount must be greater than zero.");
        }
        balance += amount;
        System.out.println("Deposit successful. Current balance : $" + balance);
    }
    public void withdraw(double amount) throws InvalidAmountException,InsufficientFundsException {
        if (amount <= 0) {
            throw new InvalidAmountException("Withdrawal amount must be greater than zero.");
        }
        if (amount > balance) {
            throw new InsufficientFundsException("Insufficient balance.");
        }
        balance -= amount;
        System.out.println("Withdrawal successful. Current balance : $" + balance);
    }
    public void checkBalance() {
        System.out.println("Current Balance : $" + balance);
    }
}
public class BankingServices {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        BankAccount account = null;
        try {
            System.out.println("Enter opening balance :");
            double opening_balance = scn.nextDouble();
            account = new BankAccount(opening_balance);
            while (true) {
                System.out.println("\n----- Banking Menu -----\n1. Deposit\n2. Withdraw\n3. Check balance\n4. Exit\nChoose an option : ");
                int choice = scn.nextInt();
                if (choice < 1 || choice > 4) {
                    throw new InvalidMenuException("Invalid menu option selected.");
                }
                switch (choice) {
                    case 1:
                        System.out.println("Enter deposit amount :");
                        double depositAmount = scn.nextDouble();
                        account.deposit(depositAmount);
                        break;
                    case 2:
                        System.out.println("Enter withdrawal amount :");
                        double withdrawalAmount = scn.nextDouble();
                        account.withdraw(withdrawalAmount);
                        break;
                    case 3:
                        account.checkBalance();
                        break;
                    case 4:
                        System.out.println("Thank you for using our bank services.");
                        return;
                }
            }
        } catch (MinimumBalanceException | InvalidMenuException | InvalidAmountException | InsufficientFundsException e) {
            System.out.println("Error : " + e.getMessage());
        } catch (Exception e) {
            System.out.println("Unexpected error occurred.");
        } finally {
            if (scn != null) {
                scn.close();
            }
            System.out.println("Session ended.");
        }
    }
}