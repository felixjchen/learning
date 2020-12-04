userMap = {  
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
}
genreMap = {  
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}

songMap = {}
for genre, songs in genreMap.items():
    for song in songs:
        songMap[song] = genre


def favoriteGenres(userMap):
    userGenreMap = {}

    for user, songs in userMap.items():
        genreCount = {}

        for song in songs:
            genre = songMap[song]

            if genre not in genreCount:
                genreCount[genre] = 0

            genreCount[genre] += 1

        favGenres = []
        maxCount = -float('inf')
        for genre, count in genreCount.items():
            if count > maxCount:
                favGenres = []
                maxCount = count
            if count == maxCount:
                favGenres.append(genre)
        
        userGenreMap[user] = favGenres

    return userGenreMap

print(favoriteGenres(userMap))