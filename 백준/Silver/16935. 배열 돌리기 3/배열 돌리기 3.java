import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

class Main {
	static int N, M, R, cnt, C;
	static int cr, cc, pr, pc;
	static int [][] mat;
	static char direct;
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder output = new StringBuilder();
	static StringTokenizer tokens;
	static boolean isIn(int r, int c) {
		return r >= 0 && r < N && c >= 0 && c < M && mat[r][c] == 0;
	}
	static void rotate1(){
		for(int r = 0; r < N /2; r++) {
				int [] temp = mat[r];
				mat[r] = mat[N - 1 - r];
				mat[N - 1 - r] = temp;
			
		}
	}
	
	static void rotate2(){
		for(int r = 0; r < N; r++) {
			for(int c = 0; c < M / 2; c++) {
				int temp = mat[r][c];
				mat[r][c] = mat[r][M - 1 - c];
				mat[r][M - 1 - c] = temp;
			}
		}
		
	}
	
	static void rotate3(){
		int tmp = N;
		N = M;
		M = tmp;
		int [][] temp = new int [N][M];
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				temp[i][j] = mat[M - 1 - j][i];
			}
		}
		mat = temp;
		
	}
	
	static void rotate4(){
		int [][] temp = new int [M][N];
		for(int i = 0; i < M; i++) {
			for(int j = 0; j < N; j++) {
				temp[i][j] = mat[j][M - 1 - i];
			}
		}
		int tmp = N;
		N = M;
		M = tmp;
		mat = temp;
		
	}
	
	static void rotate5(){
		int [][] temp = new int [N/2][M/2];
		for(int r = 0; r < N /2; r++){
			for(int c = 0; c < M /2; c++) {
				temp[r][c] = mat[r][c];
			}
		}
//		1에서 2로 전달
		temp = swapSquare(0, M / 2, temp);
		// 2 -> 3
		temp = swapSquare(N / 2, M / 2, temp);
		// 3 -> 4
		temp = swapSquare(N / 2, 0 / 2, temp);
		// 4 -> 1
		temp = swapSquare(0, 0, temp);
		
	}
	
	static void rotate6(){
		int [][] temp = new int [N/2][M/2];
		for(int r = 0; r < N /2; r++){
			for(int c = 0; c < M /2; c++) {
				temp[r][c] = mat[r][c];
			}
		}
		temp = swapSquare(N / 2, 0, temp);
		temp = swapSquare(N / 2, M / 2, temp);
		temp = swapSquare(0, M / 2, temp);
		temp = swapSquare(0, 0, temp);
			
	}
	static int [][] swapSquare(int r, int c, int[][] temp){
		// 현재 영역 백업
		int [][] current = new int [N/2][M/2];
		//현재 영역 temp에 넣기
		for(int r2 = 0; r2 < N/2; r2++) {
			for(int c2 = 0; c2 < M/2; c2++) {
				current[r2][c2] = mat[r + r2][c + c2];
				mat[r + r2][c + c2] = temp[r2][c2];
			}
		}
		return current;
		//현재 영역 반환
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
		tokens = new StringTokenizer(input.readLine());
		for(int tc = 0; tc < R; tc++) {
			C = Integer.parseInt(tokens.nextToken());
			if(C == 1) {
				rotate1();
			}
			else if(C == 2) {
				rotate2();
			}
			else if(C == 3) {
				rotate3();
			}
			else if(C == 4) {
				rotate4();
			}
			else if(C == 5) {
				rotate5();
			}
			else if(C == 6) {
				rotate6();
			}
		}
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				output.append(String.format("%d ", mat[i][j]));
			}
			output.append("\n");
		}
		System.out.println(output);
	}
}
