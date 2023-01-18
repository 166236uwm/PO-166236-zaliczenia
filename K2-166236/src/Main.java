public class Main {
    public static void main(String[] args) {
        Pojazd nowy = new Pojazd("Rewelacyjny", 10000.0, 500);
        System.out.println(nowy.toString());
        Pojazd stary = new Pojazd("Niewiadomo jaki model", 10000.0, 600);
        System.out.println(stary.toString());
        System.out.println(Pojazd.getIle());
        System.out.println(nowy.equals(stary));

    }
}