import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
	static int N, M;
	static int [] nums, choosed;
	static boolean [] visited;
	static Scanner sc = new Scanner(System.in);
	static StringBuilder output = new StringBuilder();
	static StringTokenizer tokens;
	
	static void perm(int cnt) {
		if(cnt == M) {
			for(int i = 0; i < choosed.length; i++) {
				output.append(String.format("%d ", choosed[i]));
			}
			output.append("\n");
			return ;
		}
		
		for(int i = 0; i < nums.length; i++) {
			
			if(visited[i]) continue;
			visited[i] = true;
			choosed[cnt] = nums[i];
			perm(cnt + 1);
			visited[i] = false;
		}
	}
	
	public static void main(String[] args) {
		N = sc.nextInt();
		M = sc.nextInt();
		nums = new int[N];
		visited = new boolean[N];
		choosed = new int[M];
		for(int i = 0; i < N; i++) {
			nums[i] = i + 1;
		}
		perm(0);
		System.out.println(output);
	}

}
