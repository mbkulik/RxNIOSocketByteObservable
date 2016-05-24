import rx.Observable;
import rx.Scheduler;
import rx.schedulers.Schedulers;

/**
 * Created by mbk on 5/24/16.
 */
public class SimpleTest {

    public static void main(String[] args) throws Exception {
        Observable<byte[]> observable = new RxNIOSocketByteObservable().toObservable();

        observable
                .subscribeOn(Schedulers.computation())
                .map(bytes -> new String(bytes))
                .toBlocking()
                .subscribe(System.out::println);

    }
}
