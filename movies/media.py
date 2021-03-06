import webbrowser

class Video():
    ''' This is the parent class for movie'''
    def __init__(self, title):
        self.title = title

class Movie(Video):
    '''
    This class provide a way to store movie related information,
    inhertances from class Video
    '''

    # global variables for all movie instances
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, movie_storyline, poster_image, trailer_youtube):
        Video.__init__(self, title)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # open browser 
        webbrowser.open(self.trailer_youtube_url)
