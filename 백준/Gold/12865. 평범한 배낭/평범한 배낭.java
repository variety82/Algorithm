import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N, K;
	static int [] V, W;
	static int [][] dp;
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer tokens;
	public static void main(String[] args) throws IOException {
		tokens = new StringTokenizer(input.readLine());
		N = Integer.parseInt(tokens.nextToken());
		K = Integer.parseInt(tokens.nextToken());
		W = new int[K + 1];
		V = new int[K + 1];
		dp = new int[N + 1][K + 1];
		for(int i = 1; i < N + 1; i++) {
			tokens = new StringTokenizer(input.readLine());
			W[i] = Integer.parseInt(tokens.nextToken());
			V[i] = Integer.parseInt(tokens.nextToken());
		}
		for(int i = 1; i < N + 1; i++) {
			for(int w = 1; w < K + 1; w++) {
				if(W[i] == 0) {
					dp[i][w] = 0;
				}if(W[i] > w) {
					dp[i][w] = dp[i - 1][w];
				}else if(W[i] <= w) {
					dp[i][w] = Math.max(V[i] + dp[i - 1][w - W[i]], dp[i - 1][w]);
				}
			}
		}
		System.out.println(dp[N][K]);
	}	

}
