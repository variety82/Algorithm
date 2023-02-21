import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {

    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder output = new StringBuilder();
    static int T, N;
    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(input.readLine());
        int total = (1 << 10) - 1;
        for(int tc = 1; tc <= T; tc++){
            N = Integer.parseInt(input.readLine());
            int cnt = 1;
            int visited = 0;
            for(cnt = 1;; cnt++){
                char[] arr = String.valueOf(N * cnt).toCharArray();
                for(char c : arr){
                    int num = c - '0';
                    visited = visited | (1 << num);
                }
                if(visited == total){
                    break;
                }
            }
            output.append(String.format("#%d %d\n" , tc, N * cnt));
        }
        System.out.println(output);
    }
}
