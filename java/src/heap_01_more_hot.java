import java.util.PriorityQueue;

public class heap_01_more_hot {
    public static void main(String[] ar){
        int[] scoville = {1, 2, 3, 9, 10, 12};
        int K = 7;
        Solution sol = new Solution();
        System.out.println(sol.solution(scoville, K));
    }

    static class Solution {
        public int solution(int[] scoville, int K) {
            PriorityQueue<Integer> q = new PriorityQueue<>();

            for (int s: scoville){
                q.add(s);
            }

            int answer = 0;
            while (true){
                if (q.peek() >= K) return answer;
                if (q.size() < 2){
                    return -1;
                }
                else {
                    answer += 1;
                    int c1 = q.poll();
                    int c2 = q.poll();
                    q.add(c1 + c2*2);
                }
            }
        }
    }
}
