import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tokens;
    static int N;
    static double x, y;
    static double[][] points;

    static double determinant(double[] pre, double[] post){
        double x1 = pre[0];
        double y1 = pre[1];
        double x2 = post[0];
        double y2 = post[1];

        return x1 * y2 - x2 * y1;
    }

    static double calculateArea(double[][] points){
        double sum = 0;
        for(int i = 0; i < points.length - 1; i++){
            double[] pre = points[i];
            double[] post = points[i + 1];
            sum += determinant(pre, post);
        }
        return 0.5 * Math.abs(sum);
    }

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        points = new double[N+1][2];
        for(int i = 0; i < N; i ++){
            tokens = new StringTokenizer(input.readLine());
            x = Double.parseDouble(tokens.nextToken());
            y = Double.parseDouble(tokens.nextToken());
            points[i][0] = x;
            points[i][1] = y;
        }
        points[N][0] = points[0][0];
        points[N][1] = points[0][1];

        System.out.println(String.format("%.1f", calculateArea(points)));
    }
}
