import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
	static int N, M;
	static Set<String> set1 = new HashSet();
	static List<String> list = new ArrayList<>();
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder output = new StringBuilder();
	static StringTokenizer tokens;
	public static void main(String[] args) throws IOException {
		tokens = new StringTokenizer(input.readLine());
		N = Integer.parseInt(tokens.nextToken());
		M = Integer.parseInt(tokens.nextToken());
		for(int i = 0; i < N; i++) {
			set1.add(input.readLine());
		}
		
		for(int i = 0; i < M; i++) {
			String temp = input.readLine();
			if(set1.contains(temp)) {
				list.add(temp);
			}
		}
		Collections.sort(list);
		output.append(list.size());
		output.append("\n");
		for(int i = 0; i < list.size(); i++) {
			output.append(String.format("%s \n", list.get(i)));
		}
		System.out.println(output);
				
	}

}