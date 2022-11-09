from flask import Flask, request, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "farts"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.debug = True
debug = DebugToolbarExtension(app)


@app.route('/')
def main_page():
    return render_template('home.html')

@app.route('/new')
def show_new():
    return render_template('new.html')

@app.route('/old')
def what_is_happening():
    return redirect('/new')



# movie post/get redirect demo
MOVIES = ['forest gump', 'top gun', 'contact', 'gone girl']

@app.route('/movies')
def show_all_movies():
    '''show list of all movies in fake db'''
    return render_template('movies.html', movies=MOVIES)

@app.route('/movies/new', methods=['POST'])
def add_movie():
    title = request.form['title']
    #pretend db
    MOVIES.append(title)
    flash('movie created')
    return redirect('/movies')

@app.route('/movies/json')
def get_movies_json():
    raise
    return jsonify(list(MOVIES))





if __name__ == '__main__':
    app.run(debug=True)