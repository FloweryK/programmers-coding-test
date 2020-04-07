import java.util.HashMap;

public class hash_01_runner_who_couldnt_complete {
    public static void main(String[] ar){
        String[] participant = new String[] {"leo", "kiki", "eden"};
        String[] completion = new String[] {"eden", "kiki"};
        Solution sol = new Solution();
        System.out.println(sol.solution(participant, completion));
    }

    static class Solution {
        public String solution(String[] participant, String[] completion) {
            String answer = "";
            HashMap<String, Integer> nameCount = new HashMap<>();
            for (String name: participant) nameCount.put(name, nameCount.getOrDefault(name, 0) + 1);
            for (String name: completion) nameCount.put(name, nameCount.get(name)-1);

            for (String name: nameCount.keySet()){
                if (nameCount.get(name) != 0){
                    answer = name;
                }
            }
            return answer;
        }
    }
}
