import java.util.*;

class Solution {
    static int[][] deltas = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    
    static boolean isIn(int r, int c, int N, int M, int[][] maps, int new_d){
        return r >= 0 && r < N && c >= 0 && c < M && maps[r][c] > new_d;
    }

    static void bfs(int N, int M, int[][] maps){
        Deque<int[]> q = new ArrayDeque<>();
        q.offer(new int[] {0, 0});
        while(!q.isEmpty()){
            int pos[] = q.poll();
            int r = pos[0];
            int c = pos[1];
            if(r == N -1 && c == M - 1){
                break;
            }
            int new_d = maps[r][c] + 1;
            for(int[] delta : deltas){
                int nr = r + delta[0];
                int nc = c + delta[1];
                if(!isIn(nr, nc, N, M, maps, new_d)){
                    continue;
                }
                maps[nr][nc] = new_d;
                q.offer(new int[] {nr, nc});
            }
        }
    }

    static int solution(int[][] maps) {
        int N = maps.length;
        int M = maps[0].length;
        for(int r = 0; r < N; r++){
            for(int c = 0; c < M; c++){
                if(maps[r][c] == 1){
                    maps[r][c] = 10001;
                }
            }
        }
        maps[0][0] = 1;
        bfs(N, M, maps);
        if(maps[N-1][M-1] == 10001){
            return -1;
        }else{
            return maps[N-1][M-1];
        }
    }
}