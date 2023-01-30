import java.util.ArrayList;

public class Zadanie2 {
    public static <T extends Comparable<T>> T maksNatural(ArrayList<T> tab){
        ArrayList c = (ArrayList) tab.clone();
        c.sort(null);
        return (T) c.get(c.size() - 1);
    }
}
