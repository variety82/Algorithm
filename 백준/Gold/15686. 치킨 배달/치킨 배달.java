import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

class Main {
	static int N, M, minVal, sumDist, answer;
	static int [][] map;
	static Integer [][] candidate;
	static List<Integer []> store, home;
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer tokens;
	
	 static int calDistance(Integer [][] candidate) {
		 sumDist = 0;
		 for(int i = 0; i < home.size(); i++) {
			 minVal = Integer.MAX_VALUE;
			 for(int j = 0; j < candidate.length; j++) {
				 int temp = Math.abs(home.get(i)[0] - candidate[j][0]) + Math.abs(home.get(i)[1] - candidate[j][1]);
				 minVal = Math.min(minVal, temp);
			 }
			 sumDist += minVal;
		 }
		 return sumDist;
	 }
	
	static void comb(int cnt, int start) {
		if(cnt == M) {
			answer = Math.min(answer, calDistance(candidate));
			return;
		}
		for(int i = start; i < store.size(); i++) {
			candidate[cnt] = store.get(i);
			comb(cnt + 1, i + 1);
		}
	}
	
	public static void main(String[] args) throws IOException {
		tokens = new StringTokenizer(input.readLine());
		N = Integer.parseInt(tokens.nextToken());
		M = Integer.parseInt(tokens.nextToken());
		map = new int[N][N];
		store = new ArrayList<>();
		home = new ArrayList<>();
		for(int r = 0; r < N; r++) {
			tokens = new StringTokenizer(input.readLine());
			for(int c = 0; c < N; c++) {
				map[r][c] = Integer.parseInt(tokens.nextToken());
				if(map[r][c] == 2) {
					store.add(new Integer []{r, c});
				}
				if(map[r][c] == 1) {
					home.add(new Integer []{r, c});
				}
			}
		}
		candidate = new Integer[M][2];
		answer = Integer.MAX_VALUE;
		
		comb(0, 0);
		System.out.println(answer);
		
	}

}
