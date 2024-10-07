package Problem1114PrintInOrder;

import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

class Foo {

    private final Lock lock = new ReentrantLock();
    private final Condition condition1 = lock.newCondition();
    private final Condition condition2 = lock.newCondition();
    private boolean task1Completed = false;
    private boolean task2Completed = false;

    public Foo() {}

    public void first(Runnable printFirst) throws InterruptedException {
        lock.lock();
        try {
            printFirst.run();
            task1Completed = true;
            condition1.signal();
        } finally {
            lock.unlock();
        }
    }

    public void second(Runnable printSecond) throws InterruptedException {
        lock.lock();
        try {
            while (!task1Completed) {
                condition1.await();
            }
            printSecond.run();
            task2Completed = true;
            condition2.signal();
        } finally {
            lock.unlock();
        }
    }

    public void third(Runnable printThird) throws InterruptedException {
        lock.lock();
        try {
            while (!task2Completed) {
                condition2.await();
            }
            printThird.run();
        } finally {
            lock.unlock();
        }
    }

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

    public static void main(String[] args) throws InterruptedException {
        Foo foo = new Foo();

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

        thread1.start();
        thread2.start();
        thread3.start();
    }
}
