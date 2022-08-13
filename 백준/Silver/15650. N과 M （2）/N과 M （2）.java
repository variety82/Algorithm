import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int N, M;
	static int [] nums, choosed;
	static boolean [] visited;
	static StringBuilder output = new StringBuilder();
	static Scanner sc = new Scanner(System.in);
	
	static void comb(int nth, int start) {
		if(nth == M) {
			for(int i = 0; i < M; i++) {
				output.append(choosed[i] + " ");
			}
			output.append("\n");
			return;
		}
		for(int i = start; i < N; i++) {
			choosed[nth] = nums[i];
			comb(nth + 1, i + 1);
		}
	}
	


	
	public static void main(String[] args) {
		N = sc.nextInt();
		M = sc.nextInt();
		nums = new int [N];
		choosed = new int[M];
		
		for(int i = 0; i < N; i++) {
			nums[i] = i + 1;
		}
		comb(0, 0);
		System.out.println(output);
	}

}
