import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution {
	static int T, N, M, K;
	static int flySum;
	static int maxSum;
	static int [][] map;
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder output = new StringBuilder();
	static StringTokenizer tokens;
	public static void main(String[] args) throws NumberFormatException, IOException {
//		input = new BufferedReader(new FileReader("./input.txt"));
		T = Integer.parseInt(input.readLine());
		
		for(int tc = 1; tc <= T; tc++) {
			tokens = new StringTokenizer(input.readLine(), " ");
			N = Integer.parseInt(tokens.nextToken());
			M = Integer.parseInt(tokens.nextToken());
			// K : 파리채 이동가능 횟수 
			K = N - M + 1;
			map = new int[N][N];
			for(int r = 0; r < N; r++) {
				tokens = new StringTokenizer(input.readLine(), " ");
				for(int c = 0; c < N; c++) {
					map[r][c] = Integer.parseInt(tokens.nextToken());
				}
			}
			
			maxSum = 0;
			// 오른쪽으로 K번, 아래로 K번, M : 파리채 크기
			for(int r = 0; r < K; r++) {
				for(int c = 0; c < K; c++) {
					flySum = 0;
					for(int i = 0; i < M; i++) {
						for(int j = 0; j < M; j++) {
							flySum += map[r + i][c + j];
						maxSum = Math.max(maxSum, flySum);
					}
				}
			}
			
		}
			output.append(String.format("#%s %d\n", tc, maxSum));
			
	}
		System.out.println(output);
}
}

