import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {
	static int N, T, S, sum, answer;
	static int[][] arr;
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer tokens;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		N = Integer.parseInt(input.readLine());
		arr = new int[N][2];
		for(int i = 0; i < N; i++) {
			tokens = new StringTokenizer(input.readLine());
			arr[i][0] = Integer.parseInt(tokens.nextToken());
			arr[i][1] = Integer.parseInt(tokens.nextToken());
		}
		Arrays.sort(arr, new Comparator<int []>(){
			@Override
			public int compare(int[] o1, int[] o2) {
				if(o1[1] == o2[1]) {
					return Integer.compare(o1[0], o2[0]);
				}
				return Integer.compare(o1[1], o2[1]);
			}
		});
		sum = 0;
		answer = arr[0][1] - arr[0][0];
		for(int i = 0; i < N; i++) {
			T = arr[i][0];
			S = arr[i][1];
			sum = sum + T;
			answer = Math.min(answer, S - sum);
			if(S < sum) {
				answer = -1;
				break;
			}
		}
		System.out.println(answer == -1 ? -1 : answer);
	}
}
