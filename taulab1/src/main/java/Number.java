public class Number {

    private int x;

    public boolean checkConcreteValue(){
        return x == 69;
    }
    public int getX() {
        return x;
    }

    public Number(int number) {
        x = number;
    }
    public void add(int y){
        if (y >= 100)
            throw new IllegalArgumentException();
        if (x + y <= 100) x = x + y;
        else {
            x = 100;
        }
    }
    public void substract(int y){
        if (y >= 100)
            throw new IllegalArgumentException();
        if (x - y >= 0) x = x - y;
        else {
            x = 0;
        }
    }

    public void multiply(int y){
        if (y >= 100)
            throw new IllegalArgumentException();
        if (x * y >= 0) x = x * y;
        else {
            x = 0;
        }
    }

    public void divide(int y){
        if (y >= 100)
            throw new IllegalArgumentException();
        if (x / y >= 0) x = x / y;
        else {
            x = 0;
        }
    }

    public void module(int y){
        if (y >= 100)
            throw new IllegalArgumentException();
        if (x % y >= 0) x = x % y;
        else {
            x = 0;
        }
    }

    public void power(int y){
        for (int i = 0; i < y;i++){
            x = x * x;
        }
    }


}
