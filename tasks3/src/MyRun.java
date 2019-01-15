import java.util.Random;

public class MyRun implements Runnable {

    Random rand = new Random();
    int randomNum;


    public MyRun(int id) {
    }

    @Override
    public void run() {
        while(Main.text.length()>0) {
            randomNum = rand.nextInt((500 - 0) + 1) + 500;



            System.out.println("Watek A sleep");
            System.out.println("Uśpiony na "+randomNum + " ms");
            try {
                //usypiamy wątek na 100 milisekund
                Thread.sleep(randomNum);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("Watek A start");
            System.out.println("print whole table: " + Main.text);
            System.out.println("first word end at: " + Main.text.indexOf(" "));
            String temp = Main.text.substring(0,Main.text.indexOf(" "));
            Main.text = Main.text.substring(Main.text.indexOf(" ")+1,Main.text.length());
            Main.l1.add(temp);
            System.out.println("last copy word: "+ Main.l1.getLast());
            System.out.println("print whole table: " + Main.text);
            if(Main.l1.size()==4) Main.l1.removeFirst();
//            for (String s: Main.l1) {
            System.out.println("WYPISUJE:");

            for (int i=0;i<Main.l1.size();i++) {
                System.out.println(Main.l1.get(i));
                
            }
        }
    }
}