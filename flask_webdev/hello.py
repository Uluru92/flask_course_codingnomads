from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about_us():
    return "<p>I am a  Motivated Python Developer / Junior Data Scientist seeking a remote position to apply skills in Python, SQL, cloud computing, and automation in data-driven projects.</p>"

@app.route('/fav_songs')
def display_my_fav_songs():
    return """
            <h3>My favorite songs are:</h3>
            <ul>
                <li>https://www.youtube.com/watch?v=elYSQkTWfTw&list=RDelYSQkTWfTw&start_radio=1</li>
                <li><strong>https://www.youtube.com/watch?v=yDOlMPzp4a8</strong></li>
                <em>https://www.youtube.com/watch?v=grsVtPvZr7A&list=RDMM&start_radio=1&rv=yDOlMPzp4a8</em>
                <li><em>https://www.youtube.com/watch?v=ymKx03NJbqk&list=RDMM&index=3</em></li>
                <h2>https://www.youtube.com/watch?v=kDz2Xk-LRN0&list=RDMM&index=4&pp=8AUB</h2>
            </ul>
            """
@app.route('/pages')
def pages():
    return """
            <h1>List of Pages</h1>
            <ul>
                <li><a href="/fav_songs">Favorite Songs</a></li>
                <li><a href="/about">About Us</a></li>
                <li><a href="/">Home</a></li>
            </ul>
           """

@app.route('/user/<username>')
def user(username):
    favorite_songs = [
    "Bohemian Rhapsody - Queen",
    "Stairway to Heaven - Led Zeppelin",
    "Hotel California - Eagles"
    ]
    bad_song = "Bad Guy - Billie Eilish"
    return render_template("user.html", username=username, favorite_songs=favorite_songs, bad_song=bad_song)

@app.route('/dictionary/<my_dict_name>')
def dictionary(my_dict_name):
    # El HTML "dictionary.html" espera my_list y my_int
    my_list = ["Ejemplo 0", "Ejemplo 1", "Ejemplo 2"]
    my_int = 1
    my_int_size = 25
    my_str = "spiders"

    return render_template("dictionary.html", 
                           my_dict=my_dict_name, 
                           my_list=my_list, 
                           my_int=my_int, 
                           my_int_size=my_int_size,
                           my_str=my_str)

# Temporary route for viewing and debugging base template
@app.route('/base')
def base_temp():
    return render_template("base.html")

# Temporary route for *recreating* the index template using blocks
@app.route('/index2')
def index2_temp():
    return render_template("index2.html")

if __name__ == '__main__':
    app.run(debug=True)
