import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Solution {
	static int T, N, minVal;
	static int [] pos;
	static int [][][] map;
	static boolean [][] visited;
	static int [][] deltas = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder output = new StringBuilder();
	static StringTokenizer tokens;
	static Deque<int []> q = new ArrayDeque<>();
	static void bfs() {
		while(!q.isEmpty()) {
			pos = q.poll();
			int r = pos[0];
			int c = pos[1];
			
			if(r == N -1 && c == N - 1) {
				minVal = Math.min(minVal, map[1][N-1][N-1]);
			}
			if(minVal <= map[1][r][c]) {
				continue;
			}
			for(int i = 0; i < 4; i++) {
				int nr = r + deltas[i][0];
				int nc = c + deltas[i][1];
				if(!isIn(nr, nc)) {
					continue;
				}
				if(map[1][nr][nc] > map[0][nr][nc] + map[1][r][c]) {
					visited[nr][nc] = true;
					map[1][nr][nc] = map[0][nr][nc] + map[1][r][c];
					q.offer(new int[] {nr, nc});
				}
				
			}
		}
	}
	static boolean isIn(int r, int c) {
		return r >= 0 && r < N && c >= 0 && c < N;
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		T = Integer.parseInt(input.readLine());
		for(int tc = 1; tc <= T; tc++) {
			minVal = Integer.MAX_VALUE;
			N = Integer.parseInt(input.readLine());
			map = new int [2][N][N];
			visited = new boolean[N][N];
			for(int i = 0; i < N; i++) {
				String temp = input.readLine();
				for(int j = 0; j < N; j++) {
					map[0][i][j] = temp.charAt(j) - '0';
					map[1][i][j] = Integer.MAX_VALUE;
				}
			}
			map[1][0][0] = 0;
			q.offer(new int[] {0, 0});
			bfs();
			output.append(String.format("#%d %d\n", tc, map[1][N-1][N-1]));
		}
		System.out.println(output);
	}

}
