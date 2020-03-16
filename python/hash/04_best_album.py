def solution(genres, plays):
    genre_play = {}
    for i in range(len(genres)):
        genre_play[genres[i]] = plays[i] if genres[i] not in genre_play else plays[i] + genre_play[genres[i]]

    answer = []
    best_genre = sorted(genre_play.keys(), key=lambda x: genre_play[x], reverse=True)
    for genre in best_genre:
        playlist = [i for i in range(len(plays)) if genres[i] == genre]
        sorted_playlist = sorted(playlist, key=lambda i: plays[i], reverse=True)
        answer += sorted_playlist[:2]
    return answer


if __name__ == '__main__':
    genres = ['classic', 'pop', 'classic', 'classic', 'pop']
    plays = [500, 600, 150, 800, 2500]
    print(solution(genres, plays))
