from flask import Flask, render_template, session, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = "keep it secret, keep it safe bbi" # This is just an example, this is not a proper secret!
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data-dev.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

bootstrap = Bootstrap(app)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return f"<Role {self.name}>"

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return f"<User {self.username}>"


class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/', methods=['GET', 'POST'])
def home():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        flash('Great! We hope you enjoy the community')
        return redirect(url_for('home'))
    return render_template('index.html', form=form, name=session.get('name'))


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

# ERROR HANDLERS

@app.errorhandler(403)
def forbidden(e):
    error_title = "Forbidden"
    error_msg = "You shouldn't be here!"
    return render_template('error.html',
                           error_title=error_title,error_msg=error_msg), 403

@app.errorhandler(404)
def page_not_found(e):
    error_title = "Not Found"
    error_msg = "That page doesn't exist"
    return render_template('error.html',
                           error_title=error_title,error_msg=error_msg), 404

@app.errorhandler(500)
def internal_server_error(e):
    error_title = "Internal Server Error"
    error_msg = "Sorry, we seem to be experiencing some technical difficulties"
    return render_template("error.html",
                           error_title=error_title,
                           error_msg=error_msg), 500

# ERROR EXCEPTIONS -> ABORT
@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort()(404)
    return f"<h1>Hello, {user}!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
