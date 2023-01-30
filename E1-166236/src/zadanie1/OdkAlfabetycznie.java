package zadanie1;

import java.util.Comparator;

public class OdkAlfabetycznie implements Comparator {
    public int porownaj(CordlessVacuumCleaner o1, CordlessVacuumCleaner o2) {
        return o1.getName().compareTo(o2.getName());
    }

    @Override
    public int compare(Object o1, Object o2) {
        return porownaj((CordlessVacuumCleaner) o1, (CordlessVacuumCleaner) o2);
    }
}
