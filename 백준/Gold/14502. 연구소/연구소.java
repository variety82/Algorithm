import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N, M, maxVal, cnt;
	static int [][] map, lab;
	static boolean [][] visited;
	static int [][] deltas = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	static Queue<int []> q = new ArrayDeque<>();
	static Queue<int []> virus = new ArrayDeque<>();
	static int [] pos;
	static int [][] choosed;
	static List<int []> nums = new ArrayList<int []>();
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder ouput = new StringBuilder();
	static StringTokenizer tokens;
	
	static int countVirus(int [][] arr) {
		int cnt = 0;
		for(int r = 0; r < N; r++) {
			for(int c = 0; c < M; c++) {
				if(arr[r][c] == 0) {
					cnt++;
				}
			}
		}
		return cnt;
	}
	
	static int [][] copyMap(){
		int [][] copyMap = new int[N][M];
		for(int r = 0; r < N; r++) {
			for(int c = 0; c < M; c++) {
				copyMap[r][c] = map[r][c];
			}
		}
		return copyMap;
	}
	
	static void comb(int nth, int idx) {
		if(nth == 3) {
			lab = copyMap();
			for(int i = 0; i < 3; i++) {
				lab[choosed[i][0]][choosed[i][1]] = 1;
			}
			bfs();
			maxVal = Math.max(maxVal, countVirus(lab));
			return;
		}
		for(int i = idx; i < nums.size(); i++) {
			choosed[nth] = nums.get(i);
			comb(nth + 1, i + 1);
		}
	}
	
	
	static boolean isIn(int r, int c) {
		return r >= 0 && r < N && c >=0 && c < M;
	}
	
	static void bfs() {
		for(int r = 0; r < N; r++) {
			for(int c = 0; c < M; c++) {
				if(map[r][c] == 2) {
					q.offer(new int [] {r, c});
				}
			}
		}
		while(!q.isEmpty()) {
			pos = q.poll();
			int r = pos[0];
			int c = pos[1];
			for(int i = 0; i < 4; i++) {
				int nr = r + deltas[i][0];
				int nc = c + deltas[i][1];
				if(isIn(nr, nc) && lab[nr][nc] == 0) {
					lab[nr][nc] = 2;
					q.offer(new int [] {nr, nc});
				}
			}
		}
	}
	
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		tokens = new StringTokenizer(input.readLine());
		N = Integer.parseInt(tokens.nextToken());
		M = Integer.parseInt(tokens.nextToken());
		map = new int[N][M];
		visited = new boolean[N][M];
		maxVal = Integer.MIN_VALUE;
		
		choosed = new int [3][2];
		for(int r = 0; r < N; r++) {
			tokens = new StringTokenizer(input.readLine());
			for(int c = 0; c < M; c++) {
				map[r][c] = Integer.parseInt(tokens.nextToken());
				if(map[r][c] == 0) {
					nums.add(new int [] {r, c});
				}
			}
		}
		comb(0, 0);
		System.out.println(maxVal);
		

	}

}
