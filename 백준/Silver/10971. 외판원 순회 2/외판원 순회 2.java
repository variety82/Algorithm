import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N, minVal, cost, start;
	static int[][] graph;
	static boolean[] visited;
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer tokens;
	
	static void dfs(int v, int nth, int cost) {
		if(cost >= minVal) {
			return;
		}
		
		if(nth == N - 1) {
			if(graph[v][0] != 0) {
				minVal = Math.min(minVal, cost + graph[v][0]);
			}
			return;
		}
		
		for(int i = 1; i < N; i++) {
			if(!visited[i] && graph[v][i] != 0) {
				
				visited[i] = true;
				dfs(i, nth + 1, cost + graph[v][i]);
				visited[i] = false;
			}
		}
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		N = Integer.parseInt(input.readLine());
		graph = new int[N][N];
		for(int r = 0; r < N; r++) {
			tokens = new StringTokenizer(input.readLine());
			for(int c = 0; c < N; c++) {
				graph[r][c] = Integer.parseInt(tokens.nextToken());
			}
		}
		
		minVal = Integer.MAX_VALUE;

		visited = new boolean[N];
		visited[0] = true;
		dfs(0, 0, 0);
	
		System.out.println(minVal);
	}

}
