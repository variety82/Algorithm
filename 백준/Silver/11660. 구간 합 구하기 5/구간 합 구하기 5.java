import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StringReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder output = new StringBuilder();
	static StringTokenizer tokens;

	static int N;
	static int M;
	static int [][] accums;
	static int x1;
	static int x2;
	static int y1;
	static int y2;

	public static void main(String[] args) throws IOException {
		tokens = new StringTokenizer(input.readLine());
		N = Integer.parseInt(tokens.nextToken());
		M = Integer.parseInt(tokens.nextToken());
		accums = new int[N][N + 1];
		
		for(int r = 0; r < N; r++) {
			int cnt = 1;
			tokens = new StringTokenizer(input.readLine());
			for(int c = 0; c < N; c++) {

				accums[r][cnt] += accums[r][cnt - 1] + Integer.parseInt(tokens.nextToken());
				cnt ++;
			}
		}
		
		for(int tc = 0; tc < M; tc++) {
			tokens = new StringTokenizer(input.readLine());
			x1 = Integer.parseInt(tokens.nextToken());
			y1 = Integer.parseInt(tokens.nextToken());
			x2 = Integer.parseInt(tokens.nextToken());
			y2 = Integer.parseInt(tokens.nextToken());

			int start = y1-1;
			int end = y2;
			int sum = 0;
			for(int i = x1 - 1; i <= x2 - 1; i++) {
				sum += (accums[i][end] - accums[i][start]);
			}
			
			output.append(sum + "\n");

		}
		System.out.println(output);
}
}
