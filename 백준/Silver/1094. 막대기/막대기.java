import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {

	static int T, X, pos, minStick, halfStick;
	static List<Integer> list;
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder output = new StringBuilder();
	
	static void makeStick() {
		if(list.get(pos) == X) {
			return;
		}
		while(true) {
			minStick = list.remove(pos);
			halfStick = minStick / 2;
			list.add(halfStick);
			if(calSize() < X) {
				list.add(halfStick);
				pos++;
			}
			if(calSize() == X) {
				return;
			}
		}
	}
	
	static int calSize() {
		int size = 0;
		for(int i = 0; i < list.size(); i++) {
			size += list.get(i);
		}
		return size;
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
//		input = new BufferedReader(new FileReader("./input.txt"));
		list = new ArrayList<>();
		X = Integer.parseInt(input.readLine());
		list.add(64);
		pos = 0;
		makeStick();
		System.out.println(list.size());
	}

}