import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StringReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder output = new StringBuilder();
	static StringTokenizer tokens;
	static int N;
	static int M;
	static int [] arr;
	static int [] preFixSum;
	static int start;
	static int end;
	static int sum;
//	static String str = "5 3\r\n" + 
//			"5 4 3 2 1\r\n" + 
//			"1 3\r\n" + 
//			"2 4\r\n" + 
//			"5 5";
	
public static void main(String[] args) throws NumberFormatException, IOException {
//		input = new BufferedReader(new StringReader(str));
		tokens = new StringTokenizer(input.readLine());
		N = Integer.parseInt(tokens.nextToken());
		M = Integer.parseInt(tokens.nextToken());
		arr = new int[N];
		
		tokens = new StringTokenizer(input.readLine());
		for(int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(tokens.nextToken());
		}
		
		preFixSum = new int[N+1];
		for(int i = 1; i < N + 1; i++) {
			preFixSum[i] += preFixSum[i-1] + arr[i-1];
		}
		for(int tc = 0; tc < M; tc++) {
			tokens = new StringTokenizer(input.readLine());
			start = Integer.parseInt(tokens.nextToken()) - 1;
			end = Integer.parseInt(tokens.nextToken());
			sum = preFixSum[end] - preFixSum[start];
			
			output.append(String.format("%d\n", sum));
		}
		System.out.println(output);
}

}
