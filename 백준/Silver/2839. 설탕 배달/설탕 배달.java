import java.util.Scanner;

public class Main {
	static int N;
	static boolean flag;
	static Scanner sc = new Scanner(System.in);
	public static void main(String[] args) {
		N = sc.nextInt();
		flag = false;
		for(int three = 0; three < 1667; three++) {
			for(int five = 0; five < 1001; five++) {
				if((3 * three + 5 * five) == N) {
					flag = true;
					System.out.println(three + five);
				}
			}
			if(flag == true) {
				break;
			}
		}if(flag == false) {
			System.out.println(-1);
		}
	}
	
	
}
