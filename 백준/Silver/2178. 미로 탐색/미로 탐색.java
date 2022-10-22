import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N, M;
	static int [][] map;
	static int [][] deltas = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	static Queue<int []> q = new ArrayDeque<>();
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer tokens;
	
	static boolean isIn(int r, int c) {
		return r >= 0 && r < N && c >= 0 && c < M;
	}
	
	static void bfs() {
		while(!q.isEmpty()) {
			int [] pos = q.poll();
			int r = pos[0];
			int c = pos[1];
			for(int d = 0; d < 4; d++) {
				int nr = r + deltas[d][0];
				int nc = c + deltas[d][1];
				if(isIn(nr, nc) && (map[nr][nc] == 1)) {
					map[nr][nc] = map[r][c] + 1;
					q.offer(new int [] {nr, nc});
				}
			}
		}
	}
	
	public static void main(String[] args) throws IOException {
		tokens = new StringTokenizer(input.readLine());
		N = Integer.parseInt(tokens.nextToken());
		M = Integer.parseInt(tokens.nextToken());
		
		map = new int[N][M];
		for(int r = 0; r < N; r++) {
			String temp = input.readLine();
			for(int c = 0; c < M; c++) {
				map[r][c] = temp.charAt(c) - '0';
			}
		}
		q.offer(new int [] {0, 0});
//		map[0][0] = 0;
		bfs();
		System.out.println(map[N - 1][M - 1]);
	}

}
