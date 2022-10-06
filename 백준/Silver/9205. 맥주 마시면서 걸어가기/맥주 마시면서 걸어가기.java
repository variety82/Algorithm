import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int T, cs, fr, fc, hr, hc;
	static int [][] map, csArr;
	static boolean [] visited;
	static Point festival;
	static List<Point> list;
	static Queue<Point> q = new ArrayDeque<>();
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer tokens;
	static StringBuilder output = new StringBuilder();
	static class Point{
		int r, c;

		public Point(int r, int c) {
			super();
			this.r = r;
			this.c = c;
		}

		@Override
		public String toString() {
			return "Point [r=" + r + ", c=" + c + "]";
		}
		
	}
	
	static int calDist(int x, int y, int x2, int y2) {
		return Math.abs(x - x2) + Math.abs(y - y2);
	}
	
	static boolean bfs() {
		q = new ArrayDeque<>();
		q.offer(new Point(hr, hc));
		while(!q.isEmpty()) {
			Point pos = q.poll();
			int nr = pos.r;
			int nc = pos.c;
			if(calDist(nr, nc, fr, fc) <= 1000) {
				return true;
			}
			for(int i = 0; i < cs; i++) {
				if(!visited[i]) {
					int cr = list.get(i).r;
					int cc = list.get(i).c;
					if(calDist(nr, nc, cr, cc) <= 1000) {
						visited[i] = true;
						q.add(new Point(cr, cc));
					}
					
				}
			}
		}
		return false;
	}
	public static void main(String[] args) throws NumberFormatException, IOException {
		T = Integer.parseInt(input.readLine());
		for(int tc = 0; tc < T; tc++) {
			list = new ArrayList<>();
			cs = Integer.parseInt(input.readLine());
			visited = new boolean[cs];
			tokens = new StringTokenizer(input.readLine());
			hr = Integer.parseInt(tokens.nextToken());
			hc = Integer.parseInt(tokens.nextToken());
//			q.offer(new Point(hr, hc));
			for(int i = 0; i < cs; i++) {
				tokens = new StringTokenizer(input.readLine());
				int csr = Integer.parseInt(tokens.nextToken());
				int csc = Integer.parseInt(tokens.nextToken());
				list.add(new Point(csr, csc));
			}
			tokens = new StringTokenizer(input.readLine());
			fr = Integer.parseInt(tokens.nextToken());
			fc = Integer.parseInt(tokens.nextToken());
			
			String ans = bfs() == true ? "happy" : "sad";
			output.append(ans);
			output.append("\n");
		}
		System.out.println(output);
		
		
		
	}

}
