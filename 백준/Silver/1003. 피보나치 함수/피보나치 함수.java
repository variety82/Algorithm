import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int T, N;
	static int [][] dp;
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder output = new StringBuilder();
	static StringTokenizer tokens;
	public static void main(String[] args) throws NumberFormatException, IOException {
		T = Integer.parseInt(input.readLine());
		dp = new int[41][2];
		dp[0][0] = 1;
		dp[1][1] = 1;
		
		for(int i = 2; i < 41; i++) {
			dp[i][0] = dp[i-2][0] + dp[i-1][0];
			dp[i][1] = dp[i-2][1] + dp[i-1][1];
		}
		
		for(int i = 0; i < T; i++) {
			N = Integer.parseInt(input.readLine());
			output.append(String.format("%d %d\n", dp[N][0], dp[N][1]));
		}
		System.out.println(output);
	}

}
