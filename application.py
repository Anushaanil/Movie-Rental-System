'''from movie import Movie_details
from user import UserDetails
movie_obj= Movie_details("DIA", "Love", "Pruthvi", False)
user_obj= UserDetails("Putta")
user_obj.movies.append(movie_obj)
# print(movie_obj.movie_name) checked to see if we can import and it works or not!
print(user_obj)
print("Newly added movies to user: ", user_obj.movies)
print("watched movie bucket_list: {}".format(user_obj.watched_movies()))'''
from movie import Movie_details
from user import UserDetails
import json
with open("myfile.txt","r") as f:
    json_data= json.load(f)
    user= UserDetails.from_json(json_data)
    print(user.json())

'''user = UserDetails("Putta")
user.add_movies("ASN", "Drama", "Rakshit Shetty")
user.add_movies("kgf","CDrama","yash")

with open("myfile.txt","w") as f:
    json.dump(user.json(),f)'''
'''user=UserDetails.load_from_file("Putta.txt")
print(user.user_name)
print(user.movies)'''
'''user_obj.add_movies("ASN","Drama","RakshitShetty")
user_obj.add_movies("kgf","CDrama", "yash")
user_obj.save_to_file()'''

