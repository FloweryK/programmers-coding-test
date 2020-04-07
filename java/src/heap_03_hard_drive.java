import java.util.Comparator;
import java.util.PriorityQueue;

public class heap_03_hard_drive {
    public static void main(String[] ar){
        int[][] jobs = {{1, 9}, {0, 3}, {2, 6}};

        Solution sol = new Solution();
        System.out.println(sol.solution(jobs));
    }

    static class Solution {
        public int solution(int[][] jobs) {
            PriorityQueue<int[]> queue = new PriorityQueue<int[]>(Comparator.comparing(item->item[1]));
            PriorityQueue<int[]> jobq = new PriorityQueue<int[]>(Comparator.comparing(item->item[0]));
            for (int[] job: jobs) jobq.add(job);

            int t = 0;
            int sum = 0;

            while (jobq.size() > 0 || queue.size() > 0){
                while (jobq.size() > 0 && jobq.peek()[0] <= t){
                    queue.add(jobq.poll());
                }
                if (queue.size() > 0){
                    int[] job = queue.poll();
                    t += job[1];
                    sum += t - job[0];
                }
                else{
                    t = jobq.peek()[0];
                }
            }
            return sum / jobs.length;
        }
    }
}
