import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N, minVal;
	static int [][] cost;
	static int R = 0, G = 1, B = 2;
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer tokens;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
//		input = new BufferedReader(new FileReader("./input.txt"));
		N = Integer.parseInt(input.readLine());
		cost = new int[N][3];
		for(int i = 0; i < N; i++) {
			tokens = new StringTokenizer(input.readLine());
			for(int j = 0; j < 3; j++) {
				cost[i][j] = Integer.parseInt(tokens.nextToken());
			}
		}
		
		System.out.println(makeHome());
	}
	
	static int makeHome() {
		for(int i = 1; i < N; i++) {
			cost[i][R] += Math.min(cost[i-1][G], cost[i-1][B]);
			cost[i][G] += Math.min(cost[i-1][R], cost[i-1][B]);
			cost[i][B] += Math.min(cost[i-1][R], cost[i-1][G]);
			
		}
		return Math.min(Math.min(cost[N-1][R], cost[N-1][G]), cost[N-1][B]);
		
	}
	

}
