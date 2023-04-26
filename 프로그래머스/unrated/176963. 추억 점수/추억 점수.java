import java.util.HashMap;
import java.util.Map;
class Solution {
    public int [] solution(String[] name, int[] yearning, String[][] photo){
        int[] answer = new int[photo.length];
        Map<String, Integer> map = new HashMap<String, Integer>();
        for(int i = 0; i < name.length; i++){
            map.put(name[i], yearning[i]);
        }

        for(int i = 0; i < photo.length; i++){
            int cnt = 0;
            for(int j = 0; j < photo[i].length; j++){
                if(!map.containsKey(photo[i][j])) {
                    continue;
                }
                cnt += map.get(photo[i][j]);
            }
            answer[i] = cnt;
        }
        return answer;
    }
}