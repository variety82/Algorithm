import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static String input;
	static StringBuilder output = new StringBuilder();
	static char[] pw = new char[] {'a', 'e', 'i', 'o', 'u'};
	static Scanner sc = new Scanner(System.in);
	public static void main(String[] args) {
		input = sc.nextLine();
		char[] arr = input.toCharArray();

		// 주어진 암호문에서 p를 만나면 앞, 뒤 체크 후 앞 뒤가 모음이면 해당 모음으로 변경 후 p와 그 뒷자리 모음은 0으로 마킹
		for(int i = 1, length = arr.length; i < length - 1; i++) {
			if(arr[i] == 'p') {
				for(int j = 0; j < 5; j++) {
					// p를 만났을 때 p의 전자리가 0이면 이미 변경된거라 무시
					// 예를 들어 원본 apa가 암호화 되면 apapapa인데 앞에서부터 pa만 삭제하면 a가 됨
					if(arr[i + 1] == pw[j] && arr[i -1] == pw[j] && arr[i - 1] != '0') {
						arr[i] = '0';
						arr[i + 1] = '0';
						break;
					}
				}
			}
		}
		for(int i = 0; i < arr.length; i++) {
			if(arr[i] != '0') {
				output.append(arr[i]);
			}
		}
		System.out.println(output);
 	}

}
