public class VehicleMain {
    public static void main(String[] args) {
        Vehicle car = new Car("Toyota","Camry",2023,4);
        Vehicle truck = new Truck("Ford","F-150",2023,2000);
        car.drive();
        truck.drive();
    }
}
