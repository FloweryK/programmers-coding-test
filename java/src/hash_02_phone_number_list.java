import java.util.Arrays;

public class hash_02_phone_number_list {
    public static void main(String[] ar){
        String[] phone_book = new String[] {"123", "456", "789"};
        Solution sol = new Solution();
        System.out.println(sol.solution(phone_book));
    }

    static class Solution {
        public boolean solution(String[] phone_book) {
            boolean answer = true;

            Arrays.sort(phone_book);
            for (int i=0; i<phone_book.length-1; i++){
                if (phone_book[i+1].startsWith(phone_book[i])){
                    answer = false;
                    break;
                }
            }
            return answer;
        }
    }
}
