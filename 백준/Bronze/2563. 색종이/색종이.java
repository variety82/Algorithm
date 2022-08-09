import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
	static int N, x, y, cnt;
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer tokens;
	static boolean [][] map;
	public static void main(String[] args) throws NumberFormatException, IOException {
		N = Integer.parseInt(input.readLine());
		map = new boolean[101][101];
		for(int i = 0; i < N; i++) {
			tokens = new StringTokenizer(input.readLine());
			x = Integer.parseInt(tokens.nextToken());
			y = Integer.parseInt(tokens.nextToken());
			for(int r = y; r < y + 10; r++) {
				for(int c = x; c < x + 10;c++) {
					if(!map[r][c]) {
						map[r][c] = true;
					}
				}
			}
		}
		for(int r = 1; r < 101; r++) {
			for(int c = 1; c < 101; c++) {
				if(map[r][c] == true) {
					cnt++;
				}
			}
		}System.out.println(cnt);
	}

}
