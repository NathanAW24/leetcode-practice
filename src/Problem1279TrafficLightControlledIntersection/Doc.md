# Thought Process
When will a `Deadlock` happen in this case? (From ChatGPT)
- Both Roads Wait for Green Light
  - if the light is green for road A but all cars have crossed, the cars on road B are waiting for their light to turn green. However, if another car arrives on road A, it may prevent the light from switching, leaving cars on road B waiting indefinitely.
- Alternating Green Light Requests
  - if a car from road A crosses and immediately afterward, a car from road B arrives and turns the light green for road B, then if another car on road A arrives right when the last car from road B is done, the lights would switch back and forth without allowing one road to clear out fully.
- High Traffic on One Road Blocks the Other
  - If the other road has cars waiting but can't get their turn because the traffic light never switches, those cars are effectively deadlocked.

# Answer from community 1: [1 car move at a time, with lock](https://leetcode.com/problems/traffic-light-controlled-intersection/solutions/1015108/java-reentrantlock-with-boolean-concise-solution/)
The reason I don't use semaphore here is because, we only need one resource to allow one car to run at a time only.
```java
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
```
