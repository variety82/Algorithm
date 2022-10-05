import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int N, M, cheese, ans, time;
    static int[][] map;
    static boolean[][] visited;
    static int [][] deltas = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    
    static boolean isIn(int r, int c) {
    	return r >= 0 && r < N && c >= 0 && c < M;
    }
    
    public static void main(String[] args) throws IOException {
        StringTokenizer stringTokenizer = new StringTokenizer(input.readLine());

        N = Integer.parseInt(stringTokenizer.nextToken());
        M = Integer.parseInt(stringTokenizer.nextToken());

        cheese = 0;
        time = 0; 
        ans = 0;

        map = new int[N][M];
        for(int i = 0 ; i < N ; i++){
            stringTokenizer = new StringTokenizer(input.readLine());
            for(int j = 0 ; j < M ; j++){
            	map[i][j] = Integer.parseInt(stringTokenizer.nextToken());
                if(map[i][j] == 1)
                    cheese++;
            }
        }

        while(cheese != 0){
            time++;
            ans = cheese;
            bfs();
        }

        System.out.println(time);
        System.out.println(ans);
    }

    private static void bfs() {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{0,0});
        visited = new boolean[N][M];

        visited[0][0] = true;
        while(!q.isEmpty()){
            int[] cur = q.poll();
            for(int i = 0 ; i < 4 ; i++){
                int nr = cur[0] + deltas[i][0];
                int nc = cur[1] + deltas[i][1];
                if(nr < 0 || nc < 0 || N <= nr || M <= nc || visited[nr][nc])  continue;
                if(map[nr][nc] == 1){
                    cheese--;
                    map[nr][nc] = 0;
                }
                else if(map[nr][nc] == 0){
                    q.offer(new int[]{nr,nc});
                }

                visited[nr][nc] = true;
            }
        }
    }
}