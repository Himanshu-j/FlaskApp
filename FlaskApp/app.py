from flask import Flask, render_template
from datagen import article

app = Flask(__name__)


Article = article()


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/articles")
def arcticle():
    return render_template('article.html', article=Article)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
