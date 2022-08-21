import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;


public class Main {
	static int N, M, V, num;
	static List [] graph;
	static Queue<Integer> q = new ArrayDeque<>();
	static boolean [] visited;
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder output = new StringBuilder();
	static StringTokenizer tokens;
	
	static void dfs(int n) {
		output.append(n).append(" ");
		
		visited[n] = true;
		List<Integer> childs = graph[n];
		for(Integer child : childs) {
			if(!visited[child]) {
				dfs(child);
			}
		}
	}
	
	static void bfs(int n) {
		visited[n] = true;
		while(!q.isEmpty()) {
			int size = q.size();
			
			while(size --> 0) {
				int cur = q.poll();
				visited[cur] = true;
				output.append(cur).append(" ");
				
				List<Integer> childs = graph[cur];
				for(Integer child : childs) {
					if(!visited[child]) {
						q.offer(child);
						visited[child] = true;
					}
				}
			}
		}
	}
	
	
	public static void main(String[] args) throws IOException {
		tokens = new StringTokenizer(input.readLine());
		N = Integer.parseInt(tokens.nextToken());
		M = Integer.parseInt(tokens.nextToken());
		V = Integer.parseInt(tokens.nextToken());
		visited = new boolean[N + 1];
		graph =  new List[N + 1];
		
		num = Integer.MAX_VALUE;
		for(int i = 1; i <= N; i++) {
			graph[i] = new ArrayList<>();
		}
		
		for(int i = 1; i < M + 1; i++) {
			tokens = new StringTokenizer(input.readLine());
			int start = Integer.parseInt(tokens.nextToken());
			int end = Integer.parseInt(tokens.nextToken());
			graph[start].add(end);
			graph[end].add(start);
			num = Math.min(num, start);
		}
		for(int i = 1; i <= N; i++) {
			Collections.sort(graph[i]);
		}
		dfs(V);
		output.append("\n");
		
		visited = new boolean[N + 1];
		q.offer(V);
		bfs(V);
		System.out.println(output);
		

	}

}
