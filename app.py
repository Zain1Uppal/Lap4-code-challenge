from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random, string

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)

class Shorturl(db.model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Integer, nullable=False)
    shortenUrl = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return f"<Shorturl id: {self.id}, url: {self.url}, shortenUrl = {self.shortenUrl}>"

db.create_all()

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    received_url = request.form['input_url']
    short_url = ''.join(random.choices(string.ascii_letters + string.digits, k = 16))
    # query adding
    return('')