import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;

public class Main {
	static int N, cnt, cntAmblyopia;
	static char[][] map;
	static boolean[][] visited, visited2;
	static int[][] deltas = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	static Queue<int[]> q = new ArrayDeque<>();
	static Queue<int[]> q2 = new ArrayDeque<>();
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	
	
	static boolean isIn(int r, int c) {
		return r >=0 && r < N && c >=0 && c < N;
	}
	
	static void bfs1(int r, int c) {
		
		if(visited[r][c]) return;
		visited[r][c] = true;
		char color = map[r][c];
		q.offer(new int[] {r, c});
		
		while(!q.isEmpty()) {
			int [] cur = q.poll();
			for(int i = 0; i < 4; i++) {
				int nr = cur[0] + deltas[i][0];
				int nc = cur[1] + deltas[i][1];
				if(!isIn(nr, nc)) continue;
				if(visited[nr][nc]) continue;
				
				if(map[nr][nc] == color) {
					visited[nr][nc] = true;
					q.offer(new int[] {nr, nc});
				}
			}
		}
		cnt += 1;
	}
	
	static void bfs2(int r, int c) {
			
			if(visited2[r][c]) return;
			visited2[r][c] = true;
			char color = map[r][c];
			q2.offer(new int[] {r, c});
			
			while(!q2.isEmpty()) {
				int [] cur = q2.poll();
				for(int i = 0; i < 4; i++) {
					int nr = cur[0] + deltas[i][0];
					int nc = cur[1] + deltas[i][1];
					if(!isIn(nr, nc)) continue;
					if(visited2[nr][nc]) continue;
					
					if(color == 'R' || color == 'G') {
						
						if(map[nr][nc] == 'R' || map[nr][nc] == 'G') {
							visited2[nr][nc] = true;
							q2.offer(new int[] {nr, nc});
						}
					}else {
						if(map[nr][nc] == color) {
							visited2[nr][nc] = true;
							q2.offer(new int[] {nr, nc});
						}
					}
				}
			}
			cntAmblyopia += 1;
		}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		N = Integer.parseInt(input.readLine());
		map = new char[N][N];
		visited = new boolean[N][N];
		visited2 = new boolean[N][N];
		
		for(int i = 0; i < N; i++) {
			map[i] = input.readLine().toCharArray();
		}
		
		for(int r = 0; r < N; r++) {
			for(int c = 0; c < N; c++) {
				bfs1(r, c);
				bfs2(r, c);
			}
		}
		System.out.printf("%d %d", cnt, cntAmblyopia);
	}

}
