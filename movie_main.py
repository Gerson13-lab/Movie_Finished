from flask import Flask, render_template, request
from movie_class import movies_100
import numpy as np

app = Flask(__name__)

# Function to load movies from file and create a list of movie objects
def load_image_dict():
    file = open("C:\\Users\\gerso\\movie_finished_project\\movie_image.txt", 'r')
    image_dict = {}
    for line in file: 
        parts = line.strip().rsplit(' ', 1) #splits each line entry in file
        # Remove the extra quotes from the movie name
        movie_name = parts[0].strip("'\"")  # Ensure the movie name is stripped of quotes
        image_dict[movie_name] = parts[1]
        
    return image_dict

def load_movie_list():
    file = open("C:\\Users\gerso\\movie_finished_project\\movie.txt", 'r')
    movie_list = []
    for line in file:
        parts = line.strip().rsplit(' ', 2)  # used to split each entry
        # Remove the extra quotes from the movie name. ensures dict and m list have same movie_name type.
        # Ensure the movie name is stripped of quotes
        curr_movie = movies_100(parts[0], parts[1], parts[2])
        movie_list.append(curr_movie)
        
    return movie_list


# Function to generate a random movie
def generate_random_movie():
    random_number = np.random.randint(0, len(movie_list))
    return movie_list[random_number]

    
# Load the movie list
movie_list = load_movie_list()
#Load image_dictionary
image_dict = load_image_dict()

#used to connect to FLASK application
@app.route('/', methods=['GET', 'POST'])
def index():
    random_movie_chosen = None
    movie_image_url = None
    if request.method == 'POST':
        random_movie_chosen = generate_random_movie()
        movie_image_url = image_dict[random_movie_chosen.movie_name]
        print(f"Random Movie: {random_movie_chosen.movie_name}, {random_movie_chosen.tomato_rating}, {random_movie_chosen.release_date}, Image URL: {movie_image_url}")
    return render_template('index.html', random_movie_chosen=random_movie_chosen, movie_image_url=movie_image_url)

if __name__ == '__main__':
    app.run(debug=True)
