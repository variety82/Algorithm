import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

class Solution {
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder output = new StringBuilder();
	static StringTokenizer tokens;
	static int N;
	static int cnt;
	static int [] box = new int[100];
	static int maxIdx;
	static int minIdx;
	
	static int searchIdx(int [] arr, String type) {
		int length = arr.length;
		int max = arr[0];
		int min = arr[0];
		int maxIdx = -1;
		int minIdx = -1;
		for(int i = 0; i < length; i++) {
			if(max <= arr[i]) {
				max = arr[i];
				maxIdx = i;
			}
			if(min >= arr[i]) {
				min = arr[i];
				minIdx = i;
			}
		}
		if(type.equals("max")) {
			return maxIdx;
		}
		return minIdx;
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		for(int tc = 1; tc <= 10; tc++) {
			N = Integer.parseInt(input.readLine());
			cnt = N;
			tokens = new StringTokenizer(input.readLine(), " ");
			
			for(int i = 0; i < 100; i++) {
				box[i] = Integer.parseInt(tokens.nextToken());
			}
			
			for(int i = 0; i < N; i++) {
				maxIdx = searchIdx(box, "max");
				minIdx = searchIdx(box, "min");
				
				if(box[maxIdx] - box[minIdx] <= 1) {
					output.append(String.format("#%s %d\n", tc, box[maxIdx] - box[minIdx]));
					break;
				}
				box[maxIdx] = box[maxIdx] - 1;
				box[minIdx] = box[minIdx] + 1;
			}
			maxIdx = searchIdx(box, "max");
			minIdx = searchIdx(box, "min");
			output.append(String.format("#%s %d\n", tc, box[maxIdx] - box[minIdx]));
			
	}
		System.out.println(output);

}
}