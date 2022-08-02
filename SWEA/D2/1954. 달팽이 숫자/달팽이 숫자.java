import java.util.Arrays;
import java.util.Scanner;

class Solution {
	static Scanner sc = new Scanner(System.in);
	static StringBuilder output = new StringBuilder();
	static int T;
	static int N;
	static int [][] dal;
	static int row;
	static int col;
	static String dir;
	
	static boolean isIn(int r, int c) {
		return r >= 0 && r < N && c >= 0 && c < N;
	}
	
	static boolean isLeft(int[][] dal, int row, int col) {
		return isIn(row, col-1) && (dal[row][col - 1] == 0);
	}
	
	static boolean isRight(int[][] dal, int row, int col) {
		return isIn(row, col+1) && (dal[row][col + 1] == 0);
	}
	
	static boolean isUp(int[][] dal, int row, int col) {
		return (isIn(row-1, col) && dal[row - 1][col] == 0);
	}
	
	static boolean isDown(int[][] dal, int row, int col) {
		return (isIn(row+1, col) && dal[row + 1][col] == 0);
	}
	
	
	
	public static void main(String[] args) {
		T = sc.nextInt();
		for(int tc = 1; tc <= T; tc++) {
			N = sc.nextInt();
			dal = new int[N][N];
			int num = 1;
			row = 0;
			col = 0;
			dir = "우";
			while(num <= N * N) {
				dal[row][col] = num++;
				
				switch(dir) {
					case "우":
						if(isRight(dal, row, col) == true) {
							col++;
							break;
						}
						else {
							dir = "하";
							row++;
							break;
						}
					case "하":
						if(isDown(dal, row, col) == true) {
							row++;
							break;
						}
						else {
							dir = "좌";
							col--;
							break;
						}
					case "좌":
						if(isLeft(dal, row, col) == true) {
							col--;
							break;
						}
						else {
							dir = "상";
							row--;
							break;
						}
					case "상":
						if(isUp(dal, row, col) == true) {
							row--;
							break;
						}
						else {
							dir = "우";
							col++;
							break;
						}
				}
			}

	
			output.append(String.format("#%s\n", tc));
			for(int i = 0; i < N; i++) {
				for(int j = 0; j < N; j++) {
					output.append(String.format("%d ", dal[i][j]));
				}
				output.append("\n");
			}
			
		}
		System.out.println(output);
}
}