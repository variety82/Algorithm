import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int N, M;
	static int [] nums, choosed;
	static boolean [] visited;
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder output = new StringBuilder();
	static StringTokenizer tokens;
	public static void main(String[] args) throws IOException {
		tokens = new StringTokenizer(input.readLine());
		N = Integer.parseInt(tokens.nextToken());
		M = Integer.parseInt(tokens.nextToken());
		nums = new int[N];
		choosed = new int[M];
		visited = new boolean[M];
		tokens = new StringTokenizer(input.readLine());
		for(int i = 0; i < N; i ++) {
			nums[i] = Integer.parseInt(tokens.nextToken());
		}
		Arrays.sort(nums);
		comb(0, 0);
		System.out.println(output);
	}
	
	static void comb(int nth, int startIdx) {
		if(nth == M) {
			for(int i = 0; i < M; i++) {
				output.append(String.format("%d ", choosed[i]));
			}
			output.append("\n");
			return;
		}
		for(int i = startIdx; i < N; i++) {
			choosed[nth] = nums[i];
			comb(nth + 1, i + 1);
		}
	}

}
