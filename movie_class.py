class movies_100:
    def __init__(self, movie_name, tomato_rating, release_date):
        self.movie_name = movie_name.strip("'\"")  # Ensure the movie name is stripped of quotes
        self.tomato_rating = tomato_rating
        self.release_date = release_date
        
    def print_info(self):
        print('Movie name: ' + self.movie_name + ' \n')
        print('Movie rating: ' + str(self.tomato_rating) + ' \n')
        print('Year released: ' + str(self.release_date) + ' \n')



