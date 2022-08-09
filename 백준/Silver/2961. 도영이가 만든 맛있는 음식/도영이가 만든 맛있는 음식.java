import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer tokens;
	static int N;
	static int [][] materials;
	static int minVal = Integer.MAX_VALUE;
	
    static void makeFood(int check, int cnt, int sour, int bitter) {
    	if(cnt == N ) {
    		if(check != 0) {
    			minVal = Math.min(minVal, Math.abs(sour - bitter));
    		}
    		return;
    	}
    	makeFood(check, cnt + 1, sour, bitter);
    	makeFood(check + 1, cnt + 1, sour * materials[cnt][0], bitter + materials[cnt][1]);
    }
    
	public static void main(String[] args) throws NumberFormatException, IOException {
		N = Integer.parseInt(input.readLine());
		materials = new int[N][2];
		
		for(int i = 0; i < N; i++) {
			tokens = new StringTokenizer(input.readLine());
			materials[i][0] = Integer.parseInt(tokens.nextToken());
			materials[i][1] = Integer.parseInt(tokens.nextToken());
		}
		makeFood(0, 0, 1, 0);
		System.out.println(minVal);
		
	}

}
