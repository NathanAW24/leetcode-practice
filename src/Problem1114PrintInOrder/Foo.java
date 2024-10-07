package Problem1114PrintInOrder;

import java.util.concurrent.atomic.AtomicInteger;

class Foo {

    private AtomicInteger firstJobDone = new AtomicInteger(0);
    private AtomicInteger secondJobDone = new AtomicInteger(0);

    public Foo() {}

    public void first(Runnable printFirst) throws InterruptedException {
        // printFirst.run() outputs "first".
        printFirst.run();
        // mark the first job as done, by increasing its count.
        firstJobDone.incrementAndGet();
    }

    public void second(Runnable printSecond) throws InterruptedException {
        while (firstJobDone.get() != 1) {
            // waiting for the first job to be done.
        }
        // printSecond.run() outputs "second".
        printSecond.run();
        // mark the second as done, by increasing its count.
        secondJobDone.incrementAndGet();
    }

    public void third(Runnable printThird) throws InterruptedException {
        while (secondJobDone.get() != 1) {
            // waiting for the second job to be done.
        }
        // printThird.run() outputs "third".
        printThird.run();
    }

    // helpers for printFirst printSecond and printThird

    public static class PrintFirst implements Runnable {
        @Override
        public void run() {
            System.out.print("first");
        }
    }

    public static class PrintSecond implements Runnable {
        @Override
        public void run() {
            System.out.print("second");
        }
    }

    public static class PrintThird implements Runnable {
        @Override
        public void run() {
            System.out.print("third");
        }
    }

    // Main method to run the example
    public static void main(String[] args) throws InterruptedException {
        Foo foo = new Foo();

        // Instantiate the static inner classes
        Runnable printFirst = new Foo.PrintFirst();
        Runnable printSecond = new Foo.PrintSecond();
        Runnable printThird = new Foo.PrintThird();

        Thread thread1 = new Thread(() -> {
            try {
                foo.first(printFirst);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });

        Thread thread2 = new Thread(() -> {
            try {
                foo.second(printSecond);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });

        Thread thread3 = new Thread(() -> {
            try {
                foo.third(printThird);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });

        thread3.start();
        thread1.start();
        thread2.start();

    }
}
