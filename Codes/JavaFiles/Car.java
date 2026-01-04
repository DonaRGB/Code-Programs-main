public class Car extends Vehicle {
    private int numDoors;
    public Car(String make, String model, int year, int numDoors) {
        super(make,model,year);
        this.numDoors = numDoors;
    }

    @Override
    public void drive() {
        System.out.println("Driving car...");
    }

    public int getNumDoors() {
        return numDoors;
    } 
}