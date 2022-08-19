import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer tokens;
	static int a, b, c, maxVal, temp;
	
	public static void main(String[] args) throws IOException {
		tokens = new StringTokenizer(input.readLine());
		a = Integer.parseInt(tokens.nextToken());
		b = Integer.parseInt(tokens.nextToken());
		c = Integer.parseInt(tokens.nextToken());
		if(a == b && b == c) {
			System.out.println(10000 + a * 1000);
		}
		else if(a == b) {
			System.out.println(1000 + a * 100);
		}
		else if(b == c) {
			System.out.println(1000 + b * 100);
		}
		else if(a == c) {
			System.out.println(1000 + a * 100);
		}
		else {
			maxVal = Math.max(a, b);
			maxVal = Math.max(maxVal, c);
			System.out.println(maxVal * 100);
		}
		
	}

}
