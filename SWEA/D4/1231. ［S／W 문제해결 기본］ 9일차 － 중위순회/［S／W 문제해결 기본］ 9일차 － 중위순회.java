import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {

    static int N, nodeNum, left, right;
    static String node;
    static ArrayList<String> tree;
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tokens;
    static StringBuilder output = new StringBuilder();


    static void inOrder(int index){
        if(index > N){
            return;
        }
        inOrder(index * 2);
        output.append(tree.get(index));
        inOrder(index * 2 + 1);
    }

    public static void main(String[] args) throws IOException {
        for(int tc = 1; tc <= 10; tc++){
            N = Integer.parseInt(input.readLine());
            tree = new ArrayList<>();
            tree.add(null);
            for(int i = 0; i < N; i++){
                tokens = new StringTokenizer(input.readLine());
                nodeNum = Integer.parseInt(tokens.nextToken());
                node = tokens.nextToken();
                if(tokens.hasMoreTokens()){
                    left = Integer.parseInt(tokens.nextToken());
                    if(tokens.hasMoreTokens()){
                        right = Integer.parseInt(tokens.nextToken());
                    }
                }
                tree.add(node);
            }
            output.append(String.format("#%d ", tc));
            inOrder(1);
            output.append("\n");
        }
        System.out.println(output);
    }
}
