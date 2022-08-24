import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int M, N, answer;
	static int[][] map;
	static int[][] deltas = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	static Queue<int[]> q = new ArrayDeque<>();
//	static boolean[][] visited;
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer tokens;
	
	static boolean isEnd() {
		for(int r = 0; r < N; r++) {
			for(int c = 0; c < M; c++) {
				if(map[r][c] != 1 || map[r][c] != -1) {
					if(map[r][c] == 0) {
						return false;
					}
				}
			}
		}
		return true;
	}
	
	
	static boolean isIn(int r, int c) {
		return r >= 0 && r < N && c >= 0 && c < M;
	}
	
	static void bfs() {
		while(!q.isEmpty()) {
			int size = q.size();
			while(size -->0) {
				int[] cur = q.poll();
				
				int r = cur[0];
				int c = cur[1];
				
//				if(map[r][c] == 0) {
//					map[r][c] = 1;
//				}
				
				for(int i = 0; i < 4; i++) {
					int nr = r + deltas[i][0];
					int nc = c + deltas[i][1];
					if(!isIn(nr, nc)) continue;
					if(map[nr][nc] == -1 || map[nr][nc] == 1) continue;
//					if(visited[nr][nc]) continue;
					q.offer(new int[] {nr, nc});
					map[nr][nc] = 1;
				}
			}
			answer++;
		}
		
	}
	
	public static void main(String[] args) throws IOException {
		tokens = new StringTokenizer(input.readLine());
		M = Integer.parseInt(tokens.nextToken());
		N = Integer.parseInt(tokens.nextToken());
//		visited = new boolean[N][M];
		map = new int[N][M];
		
		for(int r = 0; r < N; r++) {
			tokens = new StringTokenizer(input.readLine());
			for(int c = 0; c < M; c++) {
				map[r][c] = Integer.parseInt(tokens.nextToken());
				if(map[r][c] == 1) {
					q.offer(new int[] {r, c});
				}
			}
		}
		answer = 0;
		bfs();
		if(isEnd()) {
			System.out.println(answer - 1);
		}else {
			System.out.println(-1);
		}
	}

}
