import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class hash_04_best_album {
    public static void main(String[] ar) {
        String[] genres = {"a", "a", "b", "b", "c", "c"};
        int[] plays = {1, 2, 3, 4, 0, 1};
        Solution sol = new Solution();
        for (int i: sol.solution(genres, plays)) System.out.println(i);
    }


    static class Solution {
        public int[] solution(String[] genres, int[] plays) {
            ArrayList<String> genreTypes = new ArrayList<>();
            for (String g : genres) if (!genreTypes.contains(g)) genreTypes.add(g);

            ArrayList<Integer> genrePlays = new ArrayList<>();
            for (int i = 0; i < genreTypes.size(); i++) {
                genrePlays.add(0);
            }
            for (int i = 0; i < plays.length; i++) {
                int genreIndex = genreTypes.indexOf(genres[i]);
                genrePlays.set(genreIndex, genrePlays.get(genreIndex) + plays[i]);
            }

            Collections.sort(genreTypes, Comparator.comparing(item -> genrePlays.get(genreTypes.indexOf(item))));
            Collections.reverse(genreTypes);
            Collections.sort(genrePlays);
            Collections.reverse(genrePlays);

            ArrayList<Integer> bestAlbum = new ArrayList<>();
            for (String genre: genreTypes){
                ArrayList<Integer> playlist = new ArrayList<>();
                for (int i = 0; i < plays.length; i++) {
                    if (genres[i].equals(genre)) playlist.add(i);
                }
                Collections.sort(playlist, Comparator.comparing(i -> -plays[i]));

                for (int i=0; i<playlist.size(); i++){
                    if (i==2) break;
                    bestAlbum.add(playlist.get(i));
                }
            }

            int[] answer = new int[bestAlbum.size()];
            for (int i = 0; i<bestAlbum.size(); i++){
                answer[i] = bestAlbum.get(i);
            }
            return answer;
        }
    }

}

