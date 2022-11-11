import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
 
public class Solution {
    static int T, N, B, minHeight;
    static int[] deployee;
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder output = new StringBuilder();
    static StringTokenizer tokens;
     
    static void findHeight(int topHeight, int index) {
        if(topHeight >= B) {
            minHeight = Math.min(minHeight, topHeight);
            return;
        }
        if(index == deployee.length) {
            return;
        }
        findHeight(topHeight + deployee[index], index + 1);
        findHeight(topHeight, index + 1);
         
    }
     
    public static void main(String[] args) throws NumberFormatException, IOException {
        T = Integer.parseInt(input.readLine());
        for(int tc = 1; tc <= T; tc++) {
            tokens = new StringTokenizer(input.readLine());
            N = Integer.parseInt(tokens.nextToken());
            B = Integer.parseInt(tokens.nextToken());
            deployee = new int[N];
            minHeight = Integer.MAX_VALUE;
             
            tokens = new StringTokenizer(input.readLine());
            for(int i = 0; i < N; i++) {
                deployee[i] = Integer.parseInt(tokens.nextToken());
            }
            findHeight(0, 0);
            output.append(String.format("#%d %d\n", tc, minHeight - B));
        }
        System.out.println(output);
 
    }
 
}