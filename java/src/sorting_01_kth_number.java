import java.util.Arrays;

public class sorting_01_kth_number {
    public static void main(String[] ar){
        int[] array = {1, 5, 2, 6, 3, 7, 4};
        int[][] commands = {{2, 5, 3}, {4, 4, 1}, {1, 7, 3}};

        Solution sol = new Solution();
        for (int a: sol.solution(array, commands)) System.out.println(a);
    }


    static class Solution {
        public int[] solution(int[] array, int[][] commands) {
            int[] answer = new int[commands.length];

            for (int i=0; i<commands.length; i++){
                int[] cmd = commands[i];
                int[] subArray = Arrays.copyOfRange(array, cmd[0]-1, cmd[1]);
                Arrays.sort(subArray);
                answer[i] = subArray[cmd[2]-1];
            }

            return answer;
        }
    }
}
