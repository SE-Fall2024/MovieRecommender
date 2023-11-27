from flask import Flask, jsonify, render_template, request, url_for,redirect
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

import json
import sys
import csv
import time

sys.path.append("../../")
from Code.prediction_scripts.item_based import recommendForNewUser
from search import Search

import requests

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
print(app.config["SQLALCHEMY_DATABASE_URI"] )
app.config['SECRET_KEY'] = 'thisisasecretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/logout', methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(80), nullable=False)

class LoginForm(FlaskForm):
    userid = StringField(validators=[
                           InputRequired()], render_kw={"placeholder": "UserID"})

    password = PasswordField(validators=[
                             InputRequired()], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')

app.secret_key = "secret key"
CORS(app, resources={r"/*": {"origins": "*"}})



# Replace 'YOUR_API_KEY' with your actual OMDB API key
OMDB_API_KEY = 'b726fa05'

with open('api_key.txt', 'r') as file: # Trailer API
    api_key = file.read().strip()


def get_movie_info(title):
    index=len(title)-6
    url = f"http://www.omdbapi.com/?t={title[0:index]}&apikey={OMDB_API_KEY}"
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        res=response.json()
        if(res['Response'] == "True"):
            return res
        else:  
            return { 'Title': title, 'imdbRating':"N/A", 'Genre':'N/A',"Poster":"https://www.creativefabrica.com/wp-content/uploads/2020/12/29/Line-Corrupted-File-Icon-Office-Graphics-7428407-1.jpg"}
    else:
        return  { 'Title': title, 'imdbRating':"N/A",'Genre':'N/A', "Poster":"https://www.creativefabrica.com/wp-content/uploads/2020/12/29/Line-Corrupted-File-Icon-Office-Graphics-7428407-1.jpg"}

@app.route("/landing_page", methods =['GET', 'POST'])
@login_required
def landing_page():
    return render_template("landing_page.html")

# @app.route("/")#~
# def home():
#    return  render_template("home.html")

@app.route("/", methods =['GET', 'POST'])#~
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(id = form.userid.data).first()
        #print(user.id)
        if user:
            #print("user.id, user.password" ,user.id, user.password)
            #print("form.password", form.password.data)
            if user.password.__eq__(form.password.data):
                print('equal')
                login_user(user)
                return redirect(url_for('landing_page'))    
            else:
                print('not equal')
    return  render_template("login.html", form = form)

# @app.route("/register")#~
# def register():
#     return  render_template("register.html")


@app.route("/predict", methods=["POST"])
# def predict():
#     data = json.loads(request.data)  # contains movies
#     data1 = data["movie_list"]
#     training_data = []
#     for movie in data1:
#         movie_with_rating = {"title": movie, "rating": 5.0}
#         training_data.append(movie_with_rating)
#     recommendations = recommendForNewUser(movie_with_rating)
    
#     for movie in data1:    
#         movie_info = get_movie_info(movie)
#         if movie_info:
#             movie_with_rating["title"]=movie
#             movie_with_rating["rating"]=movie_info["imdbRating"]
    
#     recommendations = recommendations[:10]
#     resp = {"recommendations": recommendations}
#     return resp
def predict():
    data = json.loads(request.data)  # contains movies inputted by the user
    print("data ",data) #~
    data1 = data["movie_list"]
    training_data = []
    for movie in data1:
        movie_with_rating = {"title": movie, "rating": 5.0}
        training_data.append(movie_with_rating)
    recommendations = recommendForNewUser(training_data)
    recommendations = recommendations[:10] # Top 10 recommended
    print("recommendations Top 10", recommendations) #~
    for movie in recommendations:
        movie_info = get_movie_info(movie)
        #print("movie_info", movie_info) #~

        if(movie_info.get('imdbID')): # IMDB ID
            imdb_id = movie_info['imdbID'] #~
            #print("IMDB id = ", imdb_id)
            url = f'https://api.themoviedb.org/3/find/{imdb_id}?external_source=imdb_id&api_key={api_key}'
            resp = requests.get(url)
            if resp.status_code == 200:
                res1=resp.json()
                #print('res1', res1)

                if(res1["movie_results"]):
                    movie_id = res1["movie_results"][0]['id']
                    print('movie id', movie_id)
                    url2 = f'https://api.themoviedb.org/3/movie/{movie_id}/videos?language=en-US&api_key={api_key}'
                    res_vid = requests.get(url2)
                    if res_vid.status_code == 200:
                        res_vid=res_vid.json()
                        #print("res_vid",res_vid)
                        if(res_vid['results']):
                            url_vid = f"https://www.youtube.com/watch?v={res_vid['results'][0]['key']}"
                            #print('url_vid_________________',url_vid)
                        else:
                            #print('empty video')
                            url_vid = None
                    else:
                        url_vid = None
                else:
                    movie_id = None
                    print('Empty list')
                    url_vid=None
            else:
                url_vid = None
                
        else:
            imdb_id = None #~
            url_vid = None
        #print(movie_info['imdbRating']) 
        if movie_info:
            movie_with_rating[movie+"-r"]=movie_info['imdbRating']
            movie_with_rating[movie+"-g"]=movie_info['Genre']
            movie_with_rating[movie+"-p"]=movie_info['Poster']
            movie_with_rating[movie+"-u"]=url_vid

    resp = {"recommendations": recommendations, "rating":movie_with_rating}
    return resp

@app.route("/search", methods=["POST"])
def search():
    term = request.form["q"]
    print("term= ", term) #~
    search = Search()
    filtered_dict = search.resultsTop10(term)
    resp = jsonify(filtered_dict)
    resp.status_code = 200
    return resp

@app.route("/feedback", methods=["POST"])
def feedback():
    data = json.loads(request.data)
    with open(f"experiment_results/feedback_{int(time.time())}.csv", "w") as f:
        for key in data.keys():
            f.write(f"{key} - {data[key]}\n")
    return data

@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
