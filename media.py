#webbrowser module imported
import webbrowser
#Class Movie Initialized with self and 4 parts: Title, Storyline, Poster, and trailer.
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
#Show trailer function initialized to open a youtube video in a browser window
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
