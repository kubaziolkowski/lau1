import static org.junit.Assert.*;
import org.junit.*;

public class NumberTest {

    @Test
    public void rightCheckOf69() {
        Number counter = new Number(69);
        Assert.assertTrue(counter.checkConcreteValue());
    }
    @Test
    public void wrongCheckOf69() {
        Number counter = new Number(12);
        Assert.assertFalse(counter.checkConcreteValue());
    }

    @Test
    public void addCorrectly() {
        Number counter = new Number(13);
        counter.add(27);
        Assert.assertEquals(40,counter.getX());
    }

    @Test
    public void addWrongly() {
        Number counter = new Number(70);
        counter.add(49);
        Assert.assertEquals(100,counter.getX());
    }
    @Test
    public void substractCorrectly() {
        Number counter = new Number(98);
        counter.substract(28);
        Assert.assertEquals(70, counter.getX());
    }

    @Test
    public void substractWrongly() {
        Number counter = new Number(45);
        counter.substract(46);
        Assert.assertEquals(0, counter.getX());
    }

    @Test
    public void multiplyCorrectly() {
        Number counter = new Number(33);
        counter.multiply(3);
        Assert.assertEquals(99, counter.getX());
    }

    @Test
    public void divideCorrectly() {
        Number counter = new Number(99);
        counter.divide(9);
        Assert.assertEquals(11, counter.getX());
    }

    @Test
    public void moduleCorrectly() {
        Number counter = new Number(98);
        counter.module(9);
        Assert.assertEquals(8, counter.getX());
    }

}