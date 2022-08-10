import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

class Main {
	static int N, M, K, R, C, S, depth, cnt;
	static List<Integer> answer = new ArrayList<>();
	static int minVal;
	static int [][] map, command, copyMap;
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer tokens;
	
	static void rotate(int d, int y, int x) {
		int temp = map[y + cnt][x + cnt];
		int N2 = 2 * S + 1;
		int M2 = 2 * S + 1;
		// 왼쪽줄 위로 이동
		for(int r = y + d + 1; r < y + N2 - d; r++) {
			map[r - 1][x + d] = map[r][x + d];
		}
		// 아래줄 좌측으로 이동
		for(int c = x + d + 1; c < x + M2 - d; c++) {
			map[y + N2 - 1 - d][c-1] = map[y + N2 - 1 - d][c];
		}
		//오른쪽을 아래로
		for(int r = y + N2 - 1 - 1 - d; r > y - 1 + d; r--) {
			map[r+1][x + M2 -1 - d] = map[r][x + M2 -1 - d];
		}

		// 위쪽을 오른쪽으로
		for(int c = x + M2 - 1 - 1 - d; c > C - S - 1 - 1 + d; c--) {
			map[y + d][c + 1] = map[y + d][c];
		}
		map[y + cnt][x + cnt + 1] = temp;
	}
	static int [][] copyMap(int [][] map){
		int[][] arr = new int[N][M];
		for(int r = 0; r < N; r++) {
			for(int c = 0; c < M; c++) {
				arr[r][c] = map[r][c];
			}
		}
		return arr;
	}
	static void makePermutation(int nth, int[][] choosed, boolean[] visited) {
        // 기저조건 : 몇 번쨰거를 고르는데 choosed를 다 뒤져봤다면 끝
    	if(nth == K) {
    		map = copyMap(copyMap);
    		for(int i = 0; i < nth; i++) {
    			R = choosed[i][0];
    			C = choosed[i][1];
    			S = choosed[i][2];
    			depth = choosed[i][3];
    			cnt = 0;
    			for(int d = 0; d < depth; d++) {
    				rotate(d, R - S - 1, C - S - 1);
    				cnt++;
    			}
    		}
    		minVal = Integer.MAX_VALUE;
    		for(int[] row : map){
				minVal = Math.min(minVal, sum(row));
			}
    		answer.add(minVal);
			
    		return;
    	}
    	// inductive part
    	for(int i = 0; i < command.length; i++) {
    		if(!visited[i]) {
    			visited[i] = true;
    			choosed[nth] = command[i];
    			makePermutation(nth + 1, choosed, visited);
    			// 해당 녀석을 사용 안한척하기
    			visited[i] = false;
    		}
    	}
    }
	
	 static int sum(int[] map) {
		    int sum = 0;

		    for (int i = 0; i < M; i++) {
		      sum += map[i];
		    }
		    return sum;
	}
	
	public static void main(String[] args) throws IOException {
		tokens = new StringTokenizer(input.readLine());
		N = Integer.parseInt(tokens.nextToken());
		M = Integer.parseInt(tokens.nextToken());
		K = Integer.parseInt(tokens.nextToken());
		copyMap = new int [N][M];
		for(int r = 0; r < N; r++) {
			tokens = new StringTokenizer(input.readLine());
			for(int c = 0; c < M; c++) {
				copyMap[r][c] = Integer.parseInt(tokens.nextToken());
			}
		}
		command = new int[K][4];
		
		for(int tc = 0; tc < K; tc++) {
			tokens = new StringTokenizer(input.readLine());
			R = Integer.parseInt(tokens.nextToken());
			C = Integer.parseInt(tokens.nextToken());
			S = Integer.parseInt(tokens.nextToken());
			depth = (2 * S + 1) / 2;
			command[tc][0] = R;
			command[tc][1] = C;
			command[tc][2] = S;
			command[tc][3] = depth;
			cnt = 0;
		}
		makePermutation(0, new int[K][4], new boolean[K]);
		int output = Integer.MAX_VALUE;
		for(int i = 0; i < answer.size(); i++) {
			output = Math.min(output, answer.get(i));
		}
		System.out.println(output);
	}
		
	
}

