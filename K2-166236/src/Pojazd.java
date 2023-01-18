public class Pojazd {
    private String model;
    private double cena;
    private double waga;
    static private int ile;

    public Pojazd(String model, double cena, double waga){
        this.model = model;
        this.cena = cena;
        this.waga = waga;
        ile++;
    }
    public Pojazd(double cena, double waga){
        this.model = "Niewiadomo jaki model";
        this.cena = cena;
        this.waga = waga;
        ile++;
    }

    public String getModel() {return model;}

    public double getCena() {return cena;}

    public double getWaga() {return waga;}

    @Override
    public String toString() {
        String temp = "Pojazd\n[";
        if(!this.model.equals("Niewiadomo jaki model"))
            temp += this.model + ", ";
        temp += String.format("%f, %f]", this.cena, this.waga);
        return temp;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o instanceof Pojazd) {
            if(this.cena == ((Pojazd) o).cena
                    && this.waga == ((Pojazd) o).waga
                    && this.model.equals(((Pojazd) o).model))
                return true;
        }
        return false;
    }
    public void zwiekszCene(double procent){
        this.cena += getCena() * procent;
    }
    static int getIle() {return ile;}

}
