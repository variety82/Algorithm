import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.StringTokenizer;


public class Main {
	static int N, K, cnt;
	static int[] coin;
	static BufferedReader input = new BufferedReader(new java.io.InputStreamReader(System.in));
	static StringTokenizer tokens;
	
	static int changeMonye(int money) {
		for(int i = 0; i < N; i++) {
			if(money - coin[i] >= 0) {
				cnt += (money / coin[i]);
				money -= coin[i] *  (money / coin[i]);
			}
		}
		
		return cnt;
	}
	
	public static void main(String[] args) throws IOException {
		tokens = new StringTokenizer(input.readLine());
		N = Integer.parseInt(tokens.nextToken());
		K = Integer.parseInt(tokens.nextToken());
		coin = new int[N];
		for(int i = N - 1; i >= 0; i--) {
			coin[i] = Integer.parseInt(input.readLine());
		}
		System.out.println(changeMonye(K));
	}

}
