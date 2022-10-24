import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
	static int M;
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer tokens;
	static StringBuilder output = new StringBuilder();
	static Set<Integer> set = new HashSet<>();
	
	static void oper(String command, int num) {
		switch(command) {
			case "add":
				set.add(num);
				break;
			case "remove":
				set.remove(num);
				break;
			case "check":
				if(set.contains(num)) {
					output.append("1\n");
				}else {
					output.append("0\n");
				}
				break;
			case "toggle":
				if(set.contains(num)) {
					set.remove(num);
				}else {
					set.add(num);
				}
				break;
			case "all":
				set = new HashSet<>();
				for(int i = 1; i <= 20; i++) {
					set.add(i);
				}
				break;
			case "empty":
				set = new HashSet<>();
				break;
		}
	}
	
	public static void main(String[] args) throws IOException {
		M = Integer.parseInt(input.readLine());
		for(int i = 0; i < M; i++) {
			tokens = new StringTokenizer(input.readLine());
			String command = tokens.nextToken();
			if(command.equals("all") || command.equals("empty")) oper(command, 0);
			else{
				int num = Integer.parseInt(tokens.nextToken());
				oper(command, num);
			}
		}
		System.out.println(output);
	}

}