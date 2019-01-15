import java.util.LinkedList;

public class Main {
    public static String text = "Wątek A, w nieskończonej pętli losuje słowa z tego akapitu (zaznacz, wklej do swojej klasy jako string), każde losowanie poprzedzone pauzą o czasie od 0.5s do 1s (wybranym losowo z dokładnością do 0.01s), i wrzuca je do kolejki o maks. rozmiarze 3 elementów. Wątek B co 0.7s sprawdza czy kolejka została uaktualniona (od poprzedniego sprawdzenia), i jeśli tak, to wypisuje liczbę wielkich liter w kolejce. Do realizacji kolejki użyj kolekcji LinkedList (jeśli po dodaniu elementu na końcu listy liczba elementów w kolejce wynosiłaby 4, to usuwamy element z początku listy)";
    public static LinkedList l1 = new LinkedList();


    public static void main(String[] args) {


        Runnable watekA = new MyRun(42);

        Thread threads = new Thread(watekA);

        threads.start();
    }
}