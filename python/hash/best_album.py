import collections

def solution(genres, plays):
    genre_plays = collections.defaultdict(int)
    genre_index_plays = collections.defaultdict(list)
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_plays[g] += p
        genre_index_plays[g].append((i, p))
    
    best_genre = sorted(list(genre_plays.keys()), key=lambda x: genre_plays[x], reverse=True)
    
    answer = []
    print(genre_index_plays)
    for genre in best_genre:
        genre_best_plays = sorted(genre_index_plays[genre], key=lambda x: x[1], reverse=True)[:2]
        
        for i, p in genre_best_plays:
            answer.append(i)
    
    return answer


if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    
    print(solution(genres, plays))