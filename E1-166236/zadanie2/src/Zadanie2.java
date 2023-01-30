import java.util.ArrayList;

public class Zadanie2 {
    public static <T extends Comparable<T>> T maksNatural(ArrayList<T> tab){
        ArrayList c = (ArrayList);
        .sort(null);
        return tab.get(tab.size() - 1);
    }
}
