import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    static int T, N, M;
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tokens;
    static StringBuilder output = new StringBuilder();
    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(input.readLine());
        for(int tc = 1; tc <= T; tc++){
            tokens = new StringTokenizer(input.readLine());
            N = Integer.parseInt(tokens.nextToken());
            M = Integer.parseInt(tokens.nextToken());
            int EndBit = (1 << N) - 1;
            if(EndBit == (EndBit & M)){
                output.append(String.format("#%d ON\n", tc));
            }else{
                output.append(String.format("#%d OFF\n", tc));
            }
        }
        System.out.println(output);

    }
}


