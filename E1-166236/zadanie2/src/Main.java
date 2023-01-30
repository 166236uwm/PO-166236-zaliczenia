import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> test = new ArrayList<>();
        test.add("zzzzz");
        test.add("abc");
        test.add("abcd");
        test.add("gh");
        test.add("z");
        System.out.println(Zadanie2.maksNatural(test));
        System.out.println(test);
        test.sort(null);
        System.out.println(test);
    }
}