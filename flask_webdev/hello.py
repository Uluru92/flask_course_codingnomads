from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/about')
def about_us():
    return "<p>A blurb about this website</p>"

if __name__ == '__main__':
    app.run(debug=True)

