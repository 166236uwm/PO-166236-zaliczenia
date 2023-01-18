import java.time.LocalDate;

public class Samochod extends Pojazd{
    private String rodzajPaliwa;
    private LocalDate dataProdukcji;
    public Samochod(String model, double cena, double waga, String rodzajPaliwa, int rok, int miesiac, int dzien){
        super(model, cena, waga);
        this.dataProdukcji = LocalDate.of(rok, miesiac, dzien);
        this.rodzajPaliwa = rodzajPaliwa;
    }
    public Samochod(String model, double cena, double waga, String rodzajPaliwa){
        super(model, cena, waga);
        this.rodzajPaliwa = rodzajPaliwa;
        this.dataProdukcji = LocalDate.now();
    }

    public LocalDate getDataProdukcji() {return dataProdukcji;}
    public void setDataProdukcji(LocalDate dataProdukcji) {this.dataProdukcji = dataProdukcji;}

    @Override
    public String toString() {
        String temp = super.toString() + "\nSamochod\n";
        temp += String.format("[%s, %d-%s-%d]",
                this.rodzajPaliwa,
                this.dataProdukcji.getYear(),
                this.dataProdukcji.getMonth(),
                this.dataProdukcji.getDayOfMonth());
        return temp;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if ((o instanceof Samochod)) {
            if (super.equals(o)){
                if(this.dataProdukcji.equals(((Samochod) o).dataProdukcji)
                        && this.rodzajPaliwa.equals(((Samochod) o).rodzajPaliwa))
                return true;
            }
        }
        return false;
    }
}
