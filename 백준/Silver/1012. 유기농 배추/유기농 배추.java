import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
	static int T, M, N, K, cnt;
	static int[][] map;
	static boolean [][] visited;
	static int[][] deltas = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder output = new StringBuilder();
	static StringTokenizer tokens;
	static Deque<int []> q = new ArrayDeque<>();
	static Deque<int []> q2;
	
	static boolean isIn(int r, int c) {
		return r >=0 && r < N && c >= 0 && c < M;
	}
	
	static boolean bfs(int x, int y) {
		if(visited[x][y]) {
			return false;
		}
		q2 = new ArrayDeque<>();
		q2.offer(new int[] {x, y});
		visited[x][y] = true;
		
		while(!q2.isEmpty()) {
			int pos [] = q2.poll();
			int r = pos[0];
			int c = pos[1];
			
			for(int d = 0; d < 4; d++) {
				int nr = r + deltas[d][0];
				int nc = c + deltas[d][1];
				if(isIn(nr, nc) && !visited[nr][nc] && map[nr][nc] == 1) {
					visited[nr][nc] = true;
					q2.offer(new int [] {nr, nc});
				}
				
			}
		}
		return true;
		
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		T = Integer.parseInt(input.readLine());
		for(int tc = 0; tc < T; tc++) {
			tokens = new StringTokenizer(input.readLine());
			M = Integer.parseInt(tokens.nextToken());
			N = Integer.parseInt(tokens.nextToken());
			K = Integer.parseInt(tokens.nextToken());
			map = new int[N][M];
			visited = new boolean[N][M];
			cnt = 0;
			for(int c = 0; c < K; c++) {
				tokens = new StringTokenizer(input.readLine());
				int x = Integer.parseInt(tokens.nextToken());
				int y = Integer.parseInt(tokens.nextToken());
				map[y][x] = 1;
				q.offer(new int []{y, x});
			}
			while(!q.isEmpty()) {
				int [] temp = q.poll();
				if(bfs(temp[0], temp[1])) {
					cnt++;
				}
			}
			System.out.println(cnt);
		}
		
	}

}