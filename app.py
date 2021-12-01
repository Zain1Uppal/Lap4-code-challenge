from flask import Flask, render_template, request, redirect
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import random, string

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///urls.db"
db = SQLAlchemy(app)

class Shorturl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Integer, nullable=False)
    shortenUrl = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return f'{self.url}'

db.create_all()

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method == 'POST':
        received_url = request.form['input_url']
        if not received_url:
            return render_template('form.html', shortUrl= '', title='Generator')
        short_url = ''.join(random.choices(string.ascii_letters + string.digits, k = 5))
        db.session.add(Shorturl(url=received_url, shortenUrl=short_url))
        db.session.commit()
        baseUrl = request.url_root
        return render_template('form.html', shortUrl= short_url, base_url = baseUrl,title='Result')
    else:
        return render_template('form.html', shortUrl= '', title='Generator')

@app.route('/visit/<string:surl>', methods=['GET'])
def visit(surl):
    full_url = Shorturl.query.filter_by(shortenUrl=surl).first()
    if full_url:
        return redirect(f'{full_url}', code=302)   
    else:
        return redirect('/')