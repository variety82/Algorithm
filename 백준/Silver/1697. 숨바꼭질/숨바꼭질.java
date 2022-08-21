import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N, K, cur;
	static int[] answer;
	static Queue<Integer> q = new ArrayDeque<>();
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer tokens;
	
	static boolean isIn(int x) {
		return x >= 0 && x <= 100000;
	}
	
	static void bfs() {
		if(N == K) {
			System.out.println(0);
			return;
		}
		q.offer(N);
		
		while(!q.isEmpty()) {
			cur = q.poll();
			
			if(answer[K] != 0) {
				System.out.println(answer[K]);
				return;
			}
			
			if(isIn(cur + 1) && answer[cur + 1] == 0) {
				q.offer(cur + 1);
				answer[cur + 1] = answer[cur] + 1;
			}
			if(isIn(cur - 1) && answer[cur - 1] == 0){
				q.offer(cur - 1);
				answer[cur - 1] = answer[cur] + 1;
				
			}
			if(isIn(cur * 2) && answer[cur * 2] == 0) {
				q.offer(cur * 2);
				answer[cur * 2] = answer[cur] + 1;
			}
			
		}
	}
	
	public static void main(String[] args) throws IOException {
		tokens = new StringTokenizer(input.readLine());
		N = Integer.parseInt(tokens.nextToken());
		K= Integer.parseInt(tokens.nextToken());
		answer = new int[100001];
		bfs();
	}

}
