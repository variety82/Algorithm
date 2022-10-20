import java.util.Scanner;

public class Main {
	static int D, K, coefA, coefB, A, B;
	static int [][] dp;
	static Scanner sc = new Scanner(System.in);
	public static void main(String[] args) {
		D = sc.nextInt();
		K = sc.nextInt();
		dp = new int[D + 1][2];
		dp[1][0] = 1;
		dp[2][1] = 1;
		for(int i = 3; i <= D; i++) {
			dp[i][0] = dp[i-1][0] + dp[i-2][0];
			dp[i][1] = dp[i-1][1] + dp[i-2][1];
		}
		coefA = dp[D][0];
		coefB = dp[D][1];
		A = 1;
		boolean flag = true;
		
		while(flag) {
			B = (K - coefA * A) % coefB == 0 ? (K - coefA * A) / coefB : -1;
			if(B == -1) {
				A++;
			}else {
				flag = false;
			}
		}
		System.out.println(A);
		System.out.println(B);
	}


}
