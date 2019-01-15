public class MyRun implements Runnable {

    private int id;

    public MyRun(int id) {
        this.id = id;
    }

    @Override
    public void run() {
        if(true) {
            System.out.println("Watek "+id + " start");
            try {
                //usypiamy wątek na 100 milisekund
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("Watek "+id + " end");
        }
    }
}