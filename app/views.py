from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home')


@app.route('/search')
def search():
    return render_template('search.html',
                           title='Search',
                           facility_title='vaelg anlaeg',
                           facility='Indtast anlaeg',
                           road_title='vaelg vejstraekning',
                           timeframe_title='vaelg tidsvindue')


@app.route('/data')
def data():
    return render_template('data.html',
                           datasoegning='*Indsaet dynamisk soegning her*')