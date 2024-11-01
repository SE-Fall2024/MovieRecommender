1. Clone the project onto your system.

2. Include an api_key.txt file with the api key for the movie API - Take a look at this link: (https://developer.themoviedb.org/reference/intro/getting-started).

3 .Install the following packages:

a. pip install flask-sqlalchemy

b. pip install flask-bcrypt

c. pip install flask-login

d. pip install flask-wtf

e. pip install email-validator

f. pip install flask-migrate

4. Follow these steps to create the database -> Execute in python terminal:

a. from movierecommender import db

b. from movierecommender.models import User,Post, WishlistItem, Watched, MovieLikes

c. db.create_all()

5. Run cd Code/recommenderapp and python3 app.py
