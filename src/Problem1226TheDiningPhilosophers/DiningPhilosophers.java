package Problem1226TheDiningPhilosophers;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Semaphore;

class DiningPhilosophers {
    Semaphore[] s;
    Semaphore mutex;

    public DiningPhilosophers() {
        s = new Semaphore[5];
        for (int i = 0; i < 5; i++) {
            s[i] = new Semaphore(1);
        }
        mutex = new Semaphore(1);
    }

    // call the run() method of any runnable to execute its code

    // keep in mind synchronized usage
    public void wantsToEat(int philosopher,
            Runnable pickLeftFork,
            Runnable pickRightFork,
            Runnable eat,
            Runnable putLeftFork,
            Runnable putRightFork) throws InterruptedException {

        mutex.acquire();
        s[philosopher].acquire(); // permission to run pickLeftFork
        s[(philosopher + 1) % 5].acquire(); // permission to run pickRightFork
        mutex.release();

        // actually picking up the forks
        pickLeftFork.run();
        pickRightFork.run();

        eat.run();

        putLeftFork.run();
        s[philosopher].release(); // allow other philosopher to get permission to run with fork on `philosopher`
        putRightFork.run();
        s[(philosopher + 1) % 5].release();
    }

    public static void main(String[] args) {
        int n = 5; // Number of times each philosopher eats
        int philosophersCount = 5; // Number of philosophers

        DiningPhilosophers diningPhilosophers = new DiningPhilosophers();

        // Define the actions
        Runnable pickLeftFork = () -> System.out.println("PickLeftFork run");
        Runnable pickRightFork = () -> System.out.println("PickRightFork run");
        Runnable eat = () -> System.out.println("Eat run");
        Runnable putLeftFork = () -> System.out.println("PutLeftFork run");
        Runnable putRightFork = () -> System.out.println("PutRightFork run");

        // Create a fixed thread pool with the number of philosophers
        ExecutorService executorService = Executors.newFixedThreadPool(philosophersCount);

        // Submit tasks to the executor
        for (int i = 0; i < philosophersCount; i++) {
            int philosopher = i;
            executorService.submit(() -> {
                for (int j = 0; j < n; j++) {
                    try {
                        diningPhilosophers.wantsToEat(philosopher, pickLeftFork, pickRightFork, eat, putLeftFork,
                                putRightFork);
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                        System.out.println("Thread was interrupted");
                    }
                }
            });
        }

        // Shutdown the executor service
        executorService.shutdown();
    }
}
