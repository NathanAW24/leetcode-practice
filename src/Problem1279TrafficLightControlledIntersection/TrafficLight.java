package Problem1279TrafficLightControlledIntersection;

import java.util.concurrent.locks.ReentrantLock;

class TrafficLight {
    private final ReentrantLock lock = new ReentrantLock();
    private boolean road1IsGreen = true; // if `false`, means road2IsGreen

    public TrafficLight() {

    }

    public void carArrived(
            int carId,           // ID of the car
            int roadId,          // ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
            int direction,       // Direction of the car
            Runnable turnGreen,  // Use turnGreen.run() to turn light to green on current road
            Runnable crossCar    // Use crossCar.run() to make car cross the intersection
    ) {
        lock.lock();
        try {
            if ((!road1IsGreen && (roadId == 1)) || (road1IsGreen && (roadId == 2))) {
                // just need to turn the other light green when the roadId wanted is not green
                road1IsGreen = !road1IsGreen;
                turnGreen.run();
            }
            crossCar.run();
        } finally {
            lock.unlock();
        }
    }

    public static void main(String[] args) {
        TrafficLight trafficLight = new TrafficLight();
        Runnable turnGreenRoad1 = () -> System.out.println("turnGreen on Road 1 (A)");
        Runnable turnGreenRoad2 = () -> System.out.println("turnGreen on Road 2 (B)");
        Runnable crossCar1 = () -> System.out.println("crossCar for car1");
        Runnable crossCar2 = () -> System.out.println("crossCar for car2");
        Runnable crossCar3 = () -> System.out.println("crossCar for car3");
        Runnable crossCar4 = () -> System.out.println("crossCar for car4");
        Runnable crossCar5 = () -> System.out.println("crossCar for car5");


        // CASE 1
        Thread car1 = new Thread(() -> {
            trafficLight.carArrived(1,1, 2, turnGreenRoad1, crossCar1); // direction 1 or 2 --> roadId 1
        });

        Thread car3 = new Thread(() -> {
            trafficLight.carArrived(3,1, 1, turnGreenRoad1, crossCar3); // direction 1 or 2 --> roadId 1
        });

        Thread car5 = new Thread(() -> {
            trafficLight.carArrived(5,1, 2, turnGreenRoad1, crossCar5); // direction 1 or 2 --> roadId 1
        });

        Thread car2 = new Thread(() -> {
            trafficLight.carArrived(2,2, 4, turnGreenRoad2, crossCar2); // direction 1 or 2 --> roadId 1
        });

        Thread car4 = new Thread(() -> {
            trafficLight.carArrived(4,2, 3, turnGreenRoad2, crossCar4); // direction 1 or 2 --> roadId 1
        });

        car1.start();
        car2.start();
        car3.start();
        car4.start();
        car5.start();

    }
}