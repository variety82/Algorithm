import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
	static int T, n, r;
	static int [][] dp;
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer tokens;
	
	static int combination(int n, int r) {
		if(dp[n][r] > 0) {
			return dp[n][r];
		}
		if(n == r || r == 0) {
			dp[n][r] = 1;
			return 1;
		}else {
			dp[n][r] = combination(n-1, r-1) + combination(n-1, r);
			return dp[n][r];
		}
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		T = Integer.parseInt(input.readLine());
		dp = new int[31][31];
		for(int tc = 0; tc < T; tc++) {
			tokens = new StringTokenizer(input.readLine());
			r = Integer.parseInt(tokens.nextToken());
			n = Integer.parseInt(tokens.nextToken());
			
			if(r > n / 2) {
				System.out.println(combination(n, n-r));
			}else {
				System.out.println(combination(n, r));
		}
	}

}
}
