import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;
import java.util.Scanner;

class Main {
	static int N, K, temp;
	static Scanner sc = new Scanner(System.in);
	static Deque<Integer> q = new ArrayDeque<>();
	static List<Integer> answer = new ArrayList<>();
	
	static StringBuilder output = new StringBuilder();
	public static void main(String[] args) {
		String[] input = sc.nextLine().split(" ");
		N = Integer.parseInt(input[0]);
		K = Integer.parseInt(input[1]);
		for(int i = 1; i <= N; i++) {
			q.add(i);
		}
		int cnt = 1;
		output.append("<");
		while(q.size() != 0) {
			if(cnt == K) {
				temp = q.remove();
				answer.add(temp);
				cnt = 1;
				continue;
			}
			temp = q.remove();
			q.addLast(temp);
			cnt++;
		}
		for(int i = 0; i < N; i++) {
			if(i == N-1) {
				output.append(String.format("%d>", answer.get(i)));
				break;
			}
			output.append(String.format("%d, ", answer.get(i)));
			
		}
		System.out.println(output);
	}

}
