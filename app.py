from flask import Flask, render_template, request, redirect, url_for, flash
from tmdbv3api import TMDb
from tmdbv3api import Movie

app = Flask(__name__)
app.secret_key = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMTBjNzM5MjYwZmJkODA4ZmE4ZGViNDFmZWZmYThjMiIsInN1YiI6IjY1MWQwYjllNzQ1MDdkMDBjNTc5OTFhMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.FZOdElCYd4tHoZBCG4IqHBgr4Z_cxE0LdBBIcO_MN5'  # Replace with your secret key

# Initialize the TMDb API client
tmdb = TMDb()
tmdb.api_key = '210c739260fbd808fa8deb41feffa8c2'  # Replace with your TMDb API key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    try:
        movie_name = request.form['movie_name']

        # Search for the movie by name
        movie = Movie()
        search_results = movie.search(movie_name)

        if not search_results:
            flash('Movie not found.')
            return redirect(url_for('index'))

        # Get details of the first search result (you can handle multiple results as needed)
        movie_details = movie.details(search_results[0]['id'])

        return render_template('movie_details.html', movie_details=movie_details)
    except Exception as e:
        flash('An error occurred while fetching movie details.')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
