from enum import Flag, auto


class MovieGenres(Flag):
    ACTION = auto()
    COMEDY = auto()
    DRAMA = auto()
    FANTASY = auto()
    HORROR = auto()


class Movie:
    def __init__(self, name, genres: MovieGenres) -> None:
        self.name = name
        self.genres = genres

    def in_genre(self, genres):
        return genres in self.genres

    def __str__(self) -> str:
        return self.name


# INPUT DATA:

# TEST_1:
movie = Movie("The Lord of the Rings", MovieGenres.ACTION | MovieGenres.FANTASY)

print(movie)

# TEST_2:
movie = Movie("The Lord of the Rings", MovieGenres.ACTION | MovieGenres.FANTASY)

print(movie.in_genre(MovieGenres.FANTASY))
print(movie.in_genre(MovieGenres.COMEDY))
print(movie.in_genre(MovieGenres.ACTION | MovieGenres.FANTASY))

# TEST_3:
movie = Movie("Scary movie", MovieGenres.COMEDY | MovieGenres.HORROR)

print(movie.in_genre(MovieGenres.FANTASY))
print(movie.in_genre(MovieGenres.COMEDY))
print(movie.in_genre(MovieGenres.COMEDY | MovieGenres.HORROR))

# TEST_4:
movie = Movie("Avengers", MovieGenres.FANTASY | MovieGenres.ACTION)

print(movie.in_genre(MovieGenres.DRAMA))
print(movie.in_genre(MovieGenres.ACTION))
print(movie.in_genre(MovieGenres.FANTASY | MovieGenres.ACTION))
print(movie)

# TEST_5:
movie = Movie("Любовь и голуби", MovieGenres.DRAMA | MovieGenres.COMEDY)

print(movie.in_genre(MovieGenres.DRAMA))
print(movie.in_genre(MovieGenres.ACTION))
print(movie.in_genre(MovieGenres.DRAMA | MovieGenres.COMEDY))
print(movie)
