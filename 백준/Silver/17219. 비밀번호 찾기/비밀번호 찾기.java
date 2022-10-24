import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
	static int N, M;
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer tokens;
	static StringBuilder output = new StringBuilder();
	static Map<String, String> map = new HashMap<>();
	
	public static void main(String[] args) throws IOException {
		tokens = new StringTokenizer(input.readLine());
		N = Integer.parseInt(tokens.nextToken());
		M = Integer.parseInt(tokens.nextToken());
		for(int i = 0; i < N; i++) {
			tokens = new StringTokenizer(input.readLine());
			map.put(tokens.nextToken(), tokens.nextToken());
		}
		for(int i = 0; i < M; i++) {
			tokens = new StringTokenizer(input.readLine());
			output.append(String.format("%s \n", map.get(tokens.nextToken())));
		}
		System.out.println(output);
	}

}