import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int [] W, V;
	static int [][] dp;
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer tokens;
	public static void main(String[] args) throws NumberFormatException, IOException {
		N = Integer.parseInt(input.readLine());
		W = new int[N + 1];
		V = new int[N + 1];
		dp = new int[N + 1][101];
		tokens = new StringTokenizer(input.readLine());
		for(int i = 1; i < N + 1; i++) {
			W[i] = Integer.parseInt(tokens.nextToken());
		}
		
		tokens = new StringTokenizer(input.readLine());
		for(int i = 1; i < N + 1; i++) {
			V[i] = Integer.parseInt(tokens.nextToken());
		}
		
		for(int i = 1; i < N + 1; i++) {
			for(int w = 0; w < 100; w++) {
				if(W[i] == 0) {
					dp[i][w] = 0;
				}
				if(W[i] > w) {
					dp[i][w] = dp[i - 1][w];
				}else if(W[i] <= w){
					dp[i][w] = Math.max(V[i] + dp[i - 1][w - W[i]], dp[i - 1][w]);
				}
			}
		}
		System.out.println(dp[N][99]);
	}
}

