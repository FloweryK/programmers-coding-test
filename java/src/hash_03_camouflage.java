import java.util.HashMap;

public class hash_03_camouflage {
    public static void main(String[] ar){
        String[][] clothes = new String[][] {
                {"yellow_hat", "headgear"},
                {"blue_sunglasses", "eyewear"},
                {"green_turban", "headgear"}
        };

        Solution sol = new Solution();
        System.out.println(sol.solution(clothes));
    }

    static class Solution {
        public int solution(String[][] clothes) {
            int answer = 1;
            HashMap<String, Integer> clothCount = new HashMap<>();
            for (String[] cloth: clothes) clothCount.put(cloth[1], clothCount.getOrDefault(cloth[1], 0)+1);
            for (int count: clothCount.values()) answer *= count+1;

            return answer - 1;
        }
    }
}
