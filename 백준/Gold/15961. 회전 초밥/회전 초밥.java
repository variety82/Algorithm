import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
	static int N, d, k, c, cnt, ans;
	static int [] dishs, ate;
	static HashSet<Integer> set = new HashSet<Integer>();
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer tokens;
	
	static void choiceSushi() {
		boolean flag = true;
		int start = k;
		while(flag) {
			ate[dishs[(start - k) % N]]--;
			if(ate[dishs[(start - k) % N]] == 0) {
				cnt--;
			}
			
			if(ate[dishs[start % N]] == 0) {
				cnt++;
			}
			ate[dishs[start % N]]++;
			
			ans = Math.max(ans, ate[c] == 0 ? cnt + 1 : cnt);
			
			start++;
			if(start == (N - 1 + k)) {
				flag = false;
			}
		}
	}
	
	public static void main(String[] args) throws IOException {
		tokens = new StringTokenizer(input.readLine());
		N = Integer.parseInt(tokens.nextToken());
		d = Integer.parseInt(tokens.nextToken());
		k = Integer.parseInt(tokens.nextToken());
		c = Integer.parseInt(tokens.nextToken());
		cnt = 0;
		
		dishs = new int[N];
		ate = new int[d + 1];
		
		for(int i = 0; i < N; i++) {
			dishs[i] = Integer.parseInt(input.readLine());
		}
		for(int i = 0; i < k; i++) {
			if(ate[dishs[i]] == 0) {
				cnt++;
			}
			ate[dishs[i]]++;
		}
		
		ans = ate[c] == 0 ? cnt + 1 : cnt;
		choiceSushi();
		System.out.println(ans);
		
		
	}

}
