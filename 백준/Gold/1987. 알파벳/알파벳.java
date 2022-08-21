import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int R, C, maxVal;
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer tokens;
	static String str;
	static char[][] map, copy;
	static int[][] visited, deltas = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	static boolean [] check;
	
	static boolean isIn(int r, int c) {
		return r >= 0 && r < R && c >=0 && c < C;
	}
	
	static void dfs(int x, int y, int cnt) {
		if(check[map[x][y]]) {
			maxVal = Math.max(maxVal, cnt);
			return;
		}
		
		check[map[x][y]] = true;
		for(int i = 0; i < 4; i++) {
			int nx = x + deltas[i][0];
			int ny = y + deltas[i][1];
			
			if(!isIn(nx, ny)) continue;
			dfs(nx, ny, cnt + 1);
		}
			check[map[x][y]] = false;
		
	}
	public static void main(String[] args) throws IOException {
		tokens = new StringTokenizer(input.readLine());
		R = Integer.parseInt(tokens.nextToken());
		C = Integer.parseInt(tokens.nextToken());
		map = new char[R][C];
		visited = new int[R][C];
		check = new boolean[91];
		
		for(int r = 0; r < R; r++) {
			str = input.readLine();
			map[r] = str.toCharArray();
		}
		
		maxVal = Integer.MIN_VALUE;
		dfs(0, 0, 0);

		System.out.println(maxVal);
		
	}

}
