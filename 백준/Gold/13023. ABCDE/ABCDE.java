import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class Main {
	static int N, M, a, b, cnt;
	static int[] parent;
	static List[] graph;
	static boolean[] visited;
	static boolean answer;
 	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer tokens;
	
	static int dfs(int v, int cnt) {
		if(cnt >= 5) {
			answer = true;
			return 99;
		}
		
		visited[v] = true;
		
		List<Integer> childs = graph[v];
		for(Integer child : childs){
			if(!visited[child]) {
				if(dfs(child, cnt + 1) == 99)
					return 99;
				visited[child] = false;
			}
		}
		return -999999999;
	}
	
	
	public static void main(String[] args) throws IOException {
		tokens = new StringTokenizer(input.readLine());
		N = Integer.parseInt(tokens.nextToken());
		M = Integer.parseInt(tokens.nextToken());
		graph = new List[N];
		visited = new boolean[N];
		
		for(int i = 0; i < N; i++) {
			graph[i] = new ArrayList<Integer>();
		}
		
		for(int i = 0; i < M; i++) {
			tokens = new StringTokenizer(input.readLine());
			a = Integer.parseInt(tokens.nextToken());
			b = Integer.parseInt(tokens.nextToken());
			graph[a].add(b);
			graph[b].add(a);
		}
		
		answer = false;
		for(int i = 0; i < N; i++) {
			visited = new boolean[N];
			dfs(i, 1);
		}
		
		if(answer == true) {
			System.out.println("1");
		}else {
			System.out.println("0");
		}
		
		
	}

}
