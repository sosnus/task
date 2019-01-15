public class Main {
    public static void main(String[] args) {

        Runnable runners = new MyRun(42);

        Thread threads = new Thread(runners);

        threads.start();
    }
}