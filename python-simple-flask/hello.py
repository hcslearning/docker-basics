from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hola Mundo'

@app.route('/')
def index():
    images = [
        "https://ichef.bbci.co.uk/news/976/cpsprodpb/12A9B/production/_111434467_gettyimages-1143489763.jpg",
        "https://api.time.com/wp-content/uploads/2015/02/cats.jpg?quality=85&w=1024&h=512&crop=1",
        "https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/article_thumbnails/other/cat_relaxing_on_patio_other/1800x1200_cat_relaxing_on_patio_other.jpg"
    ]
    catImage = random.choice( images )
    menu = {
        'Home': '/',
        'Saludo': '/hello'
    }
    return render_template('index.html', catImage=catImage, titulo="Index Page", menu=menu)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

