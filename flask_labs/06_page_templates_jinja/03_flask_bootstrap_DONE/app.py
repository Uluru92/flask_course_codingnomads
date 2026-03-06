from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def welcome():
    # Emily made an html file for this route she wants to show
    # for now she put this placeholder
    return render_template("index.html")
    
    #"Welcome to Emily's Dog Costumes! See my <a href=\"/services\">"\
    #"services</a> and current line of <a href=\"/costumes\">costumes</a>"

@app.route('/services')
def services():
    # Emily made an html file for this route she wants to show
    # for now she put this placeholder
    return render_template("services.html")
    
    #"I offer custom made costumes for your precious canine companion, "\
    #"and a free in-home consultation, to get the measurements."

@app.route('/costumes')
def costumes():
    costumes_list = [
        {
            'header': 'Skeleton',
            'body': "This style is great if you are feeling something extra "\
                    "spooky for your pooch.",
            'image': '/static/skeleton.jpg',
        },
        {
            'header': 'Dracula',
            'body': "My friend Judy got a new puppy, and I just had to dress "\
                    "him up for Halloween! Super cute, and no coffins required.",
            'image': '/static/dracula.jpg',
        },
        {
            'header': 'Punk Rocker',
            'image': '/static/punk-rocker.jpg',
            'body': "I thought I was a huge Misfits fan, until I dressed "\
                    "my bff's dog Frank. I think he pulls off the punk "\
                    "rocker look better than me!",
        },
        {
            'header': 'Witch',
            'body': "Our dog Rose went with the husband out fishing, so I had "\
            "to dress the cat up in this bewitching costume.",
            'image': '/static/witch.jpg',
        },
    ]

    # Emily wants to list her costumes above (listed above)
    # for now she put this placeholder

    return render_template('costumes.html', costumes_list=costumes_list)
    
    #f"Check out my costumes!"

if __name__ == '__main__':
    app.run(debug=True)