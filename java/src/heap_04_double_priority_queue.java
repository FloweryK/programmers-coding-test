import java.util.Comparator;
import java.util.PriorityQueue;

public class heap_04_double_priority_queue {
    public static void main(String[] ar){
        String[] opeartions = {"I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"};
        Solution sol = new Solution();
        int[] answer = sol.solution(opeartions);
        System.out.println(answer[0]);
        System.out.println(answer[1]);
    }

    static class Solution {
        public int[] solution(String[] operations) {
            PriorityQueue<Integer> queue = new PriorityQueue<>();
            PriorityQueue<Integer> queueReverse = new PriorityQueue<>(Comparator.comparing(item->-item));

            for (String op: operations){
                String[] opParsed = op.split(" ");
                String prefix = opParsed[0];
                int value = Integer.parseInt(opParsed[1]);

                switch (prefix) {
                    case "I":
                        queue.add(value);
                        queueReverse.add(value);
                        break;
                    case "D":
                        if (queue.size() == 0) break;
                        if (value == -1){
                            int min = queue.poll();
                            queueReverse.remove(min);
                        }
                        else {
                            int max = queueReverse.poll();
                            queue.remove(max);
                        }
                        break;
                }
            }

            int[] answer = new int[2];
            if (queue.size() == 1){
                answer[0] = queue.poll();
                answer[1] = answer[0];
            }
            else if (queue.size() > 1){
                answer[1] = queue.poll();
                while (queue.size() > 1){
                    queue.poll();
                }
                answer[0] = queue.poll();
            }
            return answer;
        }
    }
}
