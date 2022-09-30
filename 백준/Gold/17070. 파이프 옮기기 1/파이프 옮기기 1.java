import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N, cnt;
	static int h = 0, v = 1, d = 2;
	static int [][] map;
	static int [][][] dp;
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder output = new StringBuilder();
	static StringTokenizer tokens;
	
	static boolean isIn(int r, int c) {
		return r >= 0 && r < N && c >= 0 && c < N && map[r][c] == 0;
		}
	
	static boolean isHorizion(int r, int c) {
		return isIn(r, c + 1);
	}
	
	static boolean isVertical(int r, int c) {
		return isIn(r + 1, c);
	}
	
	static boolean isDiagonal(int r, int c) {
		boolean h = isIn(r, c + 1);
		boolean v = isIn(r + 1, c);
		boolean d = isIn(r + 1, c + 1);
		return h && v && d;
	}
	
	static void dfs(int r, int c, int status) {
		if(r == N -1 && c == N - 1) {
			cnt++;
			return;
		}
		if(status == h) {
			if(isHorizion(r, c) == true) {
				dfs(r, c + 1, h);
			}if(isDiagonal(r, c) == true) {
				dfs(r + 1, c + 1, d);
			}
		}else if(status == v) {
			if(isVertical(r, c) == true) {
				dfs(r + 1, c, v);
			}if(isDiagonal(r, c) == true) {
				dfs(r + 1, c + 1, d);
			}
		}else if(status == d) {
			if(isHorizion(r, c) == true) {
				dfs(r, c + 1, h);
			}if(isVertical(r, c) == true) {
				dfs(r + 1, c, v);
			}if(isDiagonal(r, c) == true) {
				dfs(r + 1, c + 1, d);
			}
		}
		
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		N = Integer.parseInt(input.readLine());
		map = new int[N][N];
		dp = new int[N][N][1];
		for(int i = 0; i < N; i ++) {
			tokens = new StringTokenizer(input.readLine());
			for(int j = 0; j < N; j++) {
				map[i][j] = Integer.parseInt(tokens.nextToken());
			}
		}
		dfs(0, 1, h);
		System.out.println(cnt);
		
		
	}

}
