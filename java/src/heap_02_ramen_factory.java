import java.util.Arrays;
import java.util.Comparator;

public class heap_02_ramen_factory {
    public static void main(String[] ar) {
        int stock = 4;
        int[] dates = {4, 10, 15};
        int[] supplies = {20, 5, 10};
        int k = 30;
        Solution sol = new Solution();
        System.out.println(sol.solution(stock, dates, supplies, k));
    }


    static class Solution {
        public int solution(int stock, int[] dates, int[] supplies, int k) {
            int[][] schedule = new int[dates.length][2];
            int[] used = new int[dates.length];
            for(int i=0; i<dates.length; i++){
                schedule[i][0] = dates[i];
                schedule[i][1] = supplies[i];
            }
            Arrays.sort(schedule, Comparator.comparing(item->-item[1]));

            int answer = 0;
            int day = stock;
            while (day < k){
                for (int i=0; i<schedule.length; i++){
                    if (schedule[i][0] <= day && used[i] == 0){
                        answer += 1;
                        day += schedule[i][1];
                        used[i] = 1;
                        break;
                    }
                }
            }

            return answer;
        }
    }
}
