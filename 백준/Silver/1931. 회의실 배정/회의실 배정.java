import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main{
	static int N, cnt, max;
	static int [][] arr;
	static boolean [] visited;
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer tokens;
	
	static void checkTrue(int start, int end) {
		for(int i = start; i <= end; i++) {
			visited[i] = true;
		}
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		N = Integer.parseInt(input.readLine());
		arr = new int[N][2];
		max = Integer.MIN_VALUE;
		for(int i = 0; i < N; i++) {
			tokens = new StringTokenizer(input.readLine());
			arr[i][0] = Integer.parseInt(tokens.nextToken());
			arr[i][1] = Integer.parseInt(tokens.nextToken());
			max = Math.max(max, arr[i][1]);
		}
		
		Arrays.sort(arr, new Comparator<int []>(){
			@Override
			public int compare(int [] o1, int [] o2) {
				if(o1[1] == o2[1])
					return Integer.compare(o1[0], o2[0]);
				return Integer.compare(o1[1], o2[1]);
			}
		});
		
		visited = new boolean[max + 1];
		cnt = 0;
		for(int i = 0; i < N; i++) {
			int start = arr[i][0];
			int end = arr[i][1];
			if(visited[start] == false && start != end) {
				checkTrue(0, end - 1);
				cnt++;
			}
			else if(start == end) {
                checkTrue(0, end - 1);
				cnt++;
			}
			
		}
		System.out.println(cnt);
	}
}
