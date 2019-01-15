import java.util.Random;

public class MyRunB implements Runnable {

    private int id;
    Random rand = new Random();
    int randomNum;

    public MyRunB(int id) {
        this.id = id;
    }

    @Override
    public void run() {
        if(true) {
            randomNum = rand.nextInt((500 - 0) + 1) + 500;

            System.out.println("Watek B start");

            try {
                //usypiamy wątek na 100 milisekund
                Thread.sleep(700);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("Watek "+id + " end");
            System.out.println("Uśpiony na "+randomNum + " ms");
        }
    }
}