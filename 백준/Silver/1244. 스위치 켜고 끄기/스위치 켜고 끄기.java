import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StringReader;
import java.lang.invoke.SwitchPoint;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.List;

public class Main {
	
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder output = new StringBuilder();
	static StringTokenizer tokens;
	static int gender;
	static int switchNum;
	static int N;
//	static String str = "8\r\n" + 
//			"0 1 0 1 0 0 0 1\r\n" + 
//			"2\r\n" + 
//			"1 3\r\n" + 
//			"2 3";
	static int changeNum(int num) {
		int change = -1;
		if(num == 0)
			change = 1;
		else if(num == 1)
			change = 0;
		return change;
	}
	
	static List<Integer> changeNumFemale(int [] switchArr, int index) {
		List<Integer> idxList = new ArrayList<>();
		idxList.add(index);
		
		int preIndex = index - 1;
		int postIndex = index + 1;
		
		boolean flag = true;
		
		while(flag) {
			if(isIn(preIndex, postIndex) && switchArr[preIndex] == switchArr[postIndex]) {
				idxList.add(preIndex--);
				idxList.add(postIndex++);
			}
			else {
				flag = false;
			}
		}
		return idxList;
	}
	
	static boolean isIn(int preIndex, int postIndex) {
		return (postIndex < N && preIndex >= 0);
	}
	
	
	public static void main(String[] args) throws NumberFormatException, IOException {		
		input = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(input.readLine());
		
		tokens = new StringTokenizer(input.readLine(), " ");
		int [] switchArr = new int [N];
		
		for(int i = 0; i < N; i++) {
			switchArr[i] = Integer.parseInt(tokens.nextToken());
		}
		
		int M = Integer.parseInt(input.readLine());
		
		for(int tc = 0; tc < M; tc++) {
			tokens = new StringTokenizer(input.readLine(), " ");
			gender = Integer.parseInt(tokens.nextToken());
			switchNum = Integer.parseInt(tokens.nextToken());
			
			if(gender == 1) {
				for(int i = 0; i < N; i++) {
					if((i + 1) % switchNum == 0) {
						switchArr[i] = changeNum(switchArr[i]);
					}
				}
			}
			else {
				List<Integer> temp = changeNumFemale(switchArr, switchNum - 1);
				for(int idx : temp) {
					switchArr[idx] = changeNum(switchArr[idx]);
				}
			}
			
		}
		
		for(int i = 0; i < switchArr.length; i++) {
			System.out.print(switchArr[i] + " ");
			if((i+1) % 20 == 0){
				System.out.println();
			}
		}
	}

}
