import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {
	static int [] nums, choosed;
	static int sum;
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder output;
	
	static void comb(int cnt, int start) {
		if(cnt == choosed.length) {
			sum = 0;
			for(int i = 0; i < choosed.length; i++) {
				sum += choosed[i];
			}
			if(sum == 100) {
				for(int i = 0; i < choosed.length; i++) {
					System.out.println(choosed[i]);
				}
				return;
			}
			return;
		}
		for(int i = start; i < nums.length; i++) {
			choosed[cnt] = nums[i];
			comb(cnt + 1, i + 1);
		}
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		nums = new int[9];
		choosed = new int[7];
		for(int i = 0; i < 9; i++) {
			nums[i] = Integer.parseInt(input.readLine());
		}
		comb(0, 0);
	}	

}
