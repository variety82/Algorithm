import java.util.*;

class Solution {
    
    static Map<Integer, Integer> init(int [] tangerine){
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < tangerine.length; i++){
            int key = tangerine[i];
            if(map.containsKey(key)){
                map.put(key, map.get(key) + 1);
            }else{
                map.put(key, 1);
            }
        }
        return map;
    }
    
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        Map<Integer, Integer> map = init(tangerine);

        List<Map.Entry<Integer, Integer>> entryList = new LinkedList<>(map.entrySet());
        entryList.sort((o1, o2) -> (o2.getValue() - o1.getValue()));

        int idx = 0;
        while(k != 0){
            int value = entryList.get(idx).getValue();
            if(k >= value){
                k -= value;
                answer += 1;
                idx++;
            }else{
                k = 0;
                answer += 1;
            }
        }
        return answer;
    }
}