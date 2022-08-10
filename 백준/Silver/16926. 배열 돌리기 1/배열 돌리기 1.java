import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

class Main {
	static int N, M, R, cnt;
	static int cr, cc, pr, pc;
	static int [][] mat, temp;
	static char direct;
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder output = new StringBuilder();
	static StringTokenizer tokens;
	static boolean isIn(int r, int c) {
		return r >= 0 && r < N && c >= 0 && c < M && mat[r][c] == 0;
	}
	
	
	public static void main(String[] args) throws IOException {

		tokens = new StringTokenizer(input.readLine());
		N = Integer.parseInt(tokens.nextToken());
		M = Integer.parseInt(tokens.nextToken());
		R = Integer.parseInt(tokens.nextToken());
		mat = new int[N][M];
		for(int r = 0; r < N; r++) {
			tokens = new StringTokenizer(input.readLine());
			for(int c = 0; c < M; c++) {
				mat[r][c] = Integer.parseInt(tokens.nextToken());
			}
		}
		
		
		for(int tc = 0; tc < R; tc++) {
			direct = 'd';
			temp = Arrays.copyOf(mat, N * M);
			mat = new int[N][M];
			cnt = 0;
			pr = 0;
			pc = 0;
			cr = 1;
			cc = 0;
			while(cnt < N * M) {
				switch(direct) {
					case 'd':
						mat[cr][cc] = temp[pr][pc];
						if(isIn(cr+1, cc)) {
							pr = cr++;
							pc = cc;
						}
						else if(isIn(cr, cc+1)) {
							pr = cr;
							pc = cc++;
							direct = 'r';
						}
						cnt++;
						break;
					case 'r':
						mat[cr][cc] = temp[pr][pc];
						if(isIn(cr, cc+1)) {
							pr = cr;
							pc = cc++;
						}
						else if(isIn(cr - 1, cc)) {
							pr = cr--;
							pc = cc;
							direct = 'u';
						}
						cnt++;
						break;
					case 'u':
						mat[cr][cc] = temp[pr][pc];
						if(isIn(cr - 1, cc)) {
							pr = cr--;
							pc = cc;
						}
						else if(isIn(cr, cc - 1)) {
							pr = cr;
							pc = cc--;
							direct = 'l';
						}
						cnt++;
						break;
					case 'l':
						mat[cr][cc] = temp[pr][pc];
						if(isIn(cr, cc - 1)) {
							pr = cr;
							pc = cc--;
						}
						else if(isIn(cr + 1, cc + 1)) {
							pr = ++cr;
							pc = ++cc;
							if(isIn(cr+1, cc)) {
								cr++;
								direct = 'd';
							}
							else if(isIn(cr, cc + 1)) {
								cr++;
								direct = 'r';
							}
						}
						cnt++;
						break;
				}
			}
		}

		for(int r = 0; r < N; r++) {
			for(int c = 0; c < M; c++) {
				output.append(String.format("%d ", mat[r][c]));
			}
			output.append("\n");
		}
		System.out.println(output);
	}

}
