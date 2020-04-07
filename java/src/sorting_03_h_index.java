import java.util.Arrays;

public class sorting_03_h_index {
    public static void main(String[] ar){
        int[] citations = {3, 0, 6, 1, 5};
        Solution sol = new Solution();
        System.out.println(sol.solution(citations));
    }

    static class Solution {
        public int solution(int[] citations) {
            Arrays.sort(citations);
            int h = citations.length;
            for (int citation: citations) if (h<=citation) break; else h+=-1;
            return h;
        }
    }
}

