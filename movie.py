class Movie_details:
    def __init__(self, movie_name, movie_genre, movie_hero,watched):
        self.movie_name = movie_name
        self.movie_genre = movie_genre
        self.movie_hero = movie_hero
        self.watched=watched
    def __repr__(self):
        return "<Movie: {}>".format(self.movie_name)

    def json(self):
        return{
            'name': self.movie_name,
            'genre': self.movie_genre,
            'hero': self.movie_hero,
            'watched': self.watched

        }
    @classmethod
    def from_json(cls,json_data):
        return Movie_details(json_data['name'],json_data['genre'],json_data['hero'],json_data['watched'])