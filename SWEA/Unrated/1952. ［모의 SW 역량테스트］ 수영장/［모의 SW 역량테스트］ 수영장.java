import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
	static int T, day, month, threeMonth, year, minVal;
	static int [] plan;
	static BufferedReader input = new BufferedReader(new BufferedReader(new InputStreamReader(System.in)));
	static StringBuilder output = new StringBuilder();
	static StringTokenizer tokens;
	
	static void dfs(int nth, int cost) {
		if(nth >= 12) {
			minVal = Math.min(minVal, cost);
			return;
		}
		dfs(nth + 1, cost + (day * plan[nth]));
		dfs(nth + 1, cost + month);
		dfs(nth + 3, cost + threeMonth);
		dfs(nth + 12, cost + year);
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		T = Integer.parseInt(input.readLine());
		plan = new int[12];
		for(int tc = 1; tc <= T; tc++) {
			minVal = Integer.MAX_VALUE;
			tokens = new StringTokenizer(input.readLine());
			day = Integer.parseInt(tokens.nextToken());
			month = Integer.parseInt(tokens.nextToken());
			threeMonth = Integer.parseInt(tokens.nextToken());
			year = Integer.parseInt(tokens.nextToken());
			
			tokens = new StringTokenizer(input.readLine());
			for(int i = 0; i < 12; i++) {
				plan[i] = Integer.parseInt(tokens.nextToken());
			}
			dfs(0, 0);
			output.append(String.format("#%d %d \n", tc, minVal));
			
		}
		System.out.println(output);
	}
}
