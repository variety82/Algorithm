import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static char[][] map;
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder output = new StringBuilder();
	static StringTokenizer tokens;
	
	static boolean check(int row, int col, int size) {
		char type = map[row][col];
		for(int r = row; r < row + size; r++) {
			for(int c = col; c< col + size; c++) {
				if(map[r][c] != type) {
					output.append("(");
					return false;
				}
			}
		}
		output.append(String.format("%s", type));
		return true;
	}
	
	static void makeTree(int row, int col, int size) {
		if(check(row, col, size)) {
			return;
		}
		int newSize = size / 2;
		makeTree(row, col, newSize);
		makeTree(row, col + newSize, newSize);
		makeTree(row + newSize, col, newSize);
		makeTree(row + newSize, col + newSize, newSize);
		output.append(")");
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		N = Integer.parseInt(input.readLine());
		map = new char[N][N];
		for(int r = 0; r < N; r++) {
			String str = input.readLine();
			for(int c = 0; c < N; c++) {
				map[r][c] = str.charAt(c);
			}
		}
		makeTree(0, 0, N);
		System.out.println(output);
	}

}
