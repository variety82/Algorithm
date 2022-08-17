import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer tokens;
	static char[] arr;
	static boolean check;
	static int sum, temp;
	static String sign;
	static Deque<String> q = new ArrayDeque<>();
	public static void main(String[] args) throws IOException {
		String str = input.readLine();
		arr = str.toCharArray();
		for(int i = 0, lenght = arr.length;i < lenght; i++) {
			if(arr[i] == '+' && check) {
				arr[i] = '-';
			}else if(arr[i] == '-'){
				q.add("-");
				check = true;
			}else if(arr[i] == '+') {
				q.add("+");
				check = false;
			}
		}
		str = String.copyValueOf(arr);
		tokens = new StringTokenizer(str, "+|-");
		sum = Integer.parseInt(tokens.nextToken());
		while(tokens.hasMoreTokens()) {
			sign = q.poll();
			temp = Integer.parseInt(tokens.nextToken());
			if(sign == "+") {
				sum = sum + temp;
			}else {
				sum = sum - temp;
			}
			
		}
		System.out.println(sum);
	}

}
