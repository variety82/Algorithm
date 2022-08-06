import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;


class Main{
	static int N;
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		N = Integer.parseInt(input.readLine());
		
		Deque<Integer> q = new ArrayDeque<>();
		for(int i = 1; i < N + 1; i++) {
			q.add(i);
		}
		
		boolean flag = true;
		
        if(q.size() == 1){
            System.out.println(q.peekFirst());
            flag = false;
        }
        
		while(flag) {
			q.removeFirst();
			int temp = q.pollFirst();
			q.add(temp);
			if(q.size() == 1) {
				System.out.println(q.peekFirst());
				flag = false;
				
			}
		}
	}

}