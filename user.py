from movie import Movie_details

class UserDetails:
    def __init__(self, user_name):
        self.user_name = user_name
        self.movies = []

    def __repr__(self):
        return "<User is: {} >".format(self.user_name)

    def watched_movies(self):
        return list(filter(lambda movie: movie.watched, self.movies))

    def add_movies(self, movie_name, movie_genre, movie_hero):
        new_movie= Movie_details(movie_name, movie_genre, movie_hero, False)
        self.movies.append(new_movie)

    def delete_movie(self,name):
        return list(filter(lambda movie:movie!=name,self.movies))

    '''using csv save and load the data,
    def save_to_file(self):
        with open("{}.txt" .format(self.user_name),"w") as f:
            f.write(f"{self.user_name} \n")
            for movie in self.movies:
                f.write(f"{movie.movie_name},{movie.movie_genre},{movie.movie_hero},{str(movie.watched)}\n")
    @classmethod
    def load_from_file(cls, filename):
        with open(filename, "r") as f:
            content = f.readlines()
            uname = content[0]
            movies = []
            for line in content[1:]:
                movie_data = line.split(',')
                movies.append(Movie_details(movie_data[0], movie_data[1], movie_data[2],movie_data[3] =='True'))
        user = cls(uname)
        user.movies = movies
        return user'''

    def json(self):
        return{
            'username':self.user_name,
            'movies':[
                movie.json() for movie in self.movies
            ]
        }
    @classmethod
    def from_json(cls,json_data):
        user=UserDetails(json_data['username'])
        movies=[]
        for movie in json_data['movies']:
            movies.append(Movie_details.from_json(movie))
        user.movies=movies
        return user


