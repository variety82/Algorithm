import java.math.BigInteger;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int N, R;
	static Scanner sc = new Scanner(System.in);
	static BigInteger [] factorial;
	public static void main(String[] args) {
		N = sc.nextInt();
		R = sc.nextInt();
		factorial = new BigInteger[N + 1];
		factorial[0] = new BigInteger("1");
		factorial[1] = new BigInteger("1");
		for(int i = 2; i <= N; i++) {
			factorial[i] = factorial[i - 1].multiply(new BigInteger(i + ""));
		}
		if(R > N / 2) {
			R = N - R;
		}
		System.out.println(factorial[N].divide(factorial[R].multiply(factorial[N-R])));
	}
	
	
	

}
