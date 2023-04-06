from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: list[Movie] = []
        self.users_collection: list[User] = []

    def register_user(self, username: str, age: int):

        found_user = [u for u in self.users_collection if u.username == username]

        if found_user:
            raise Exception("User already exists!")

        new_user = User(username, age)

        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):

        found_user = [u for u in self.users_collection if u.username == username]

        if not found_user:
            raise Exception("This user does not exist!")

        if not movie.is_owner(username):
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        self.movies_collection.append(movie)
        found_user[0].add_movie(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if not movie.is_owner(username):
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for attribute, new_value in kwargs.items():
            setattr(movie, attribute, new_value)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if not movie.is_owner(username):
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        found_user = [u for u in self.users_collection if u.username == username][0]

        found_user.delete_movie(movie)
        self.movies_collection.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):

        if movie.is_owner(username):
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        found_user = [u for u in self.users_collection if u.username == username][0]

        if movie in found_user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        found_user.like_movie(movie)
        movie.receive_like()

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):

        found_user = [u for u in self.users_collection if u.username == username][0]

        if movie not in found_user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        found_user.dislike_movie(movie)
        movie.receive_dislike()

        return f"{username} disliked {movie.title} movie."

    def display_movies(self):

        if not self.movies_collection:
            return "No movies found."
        
        sorted_movie_list = sorted([m for m in self.movies_collection], key=lambda x: (-x.year, x.title))
        return "\n".join([m.details() for m in sorted_movie_list])

    def __str__(self):

        result = "All users: "

        if not self.users_collection:
            result += "No users."
        else:
            result += ', '.join([u.username for u in self.users_collection])

        result += "\nAll movies: "

        if not self.movies_collection:
            result += "No movies."
        else:
            result += ', '.join([u.title for u in self.movies_collection])

        return result

# https://judge.softuni.org/Contests/Practice/Index/3431#1

