# from flask import Flask, redirect, request, url_for, render_template

# app = Flask(__name__)
# #remote db
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:testpass@localhost/testdb'
# #in-memory db
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

# @app.route("/")
# def home():
#     return render_template("home.html", title="home")

# @app.route("/about")
# def about():
#     return render_template("about.html", title="about")

# # @app.route("/users/<name>/<int:id>")
# # def users(name, id):
# #     return f"hello, {name}, your ID is {id}"

# # @app.route("/account")
# # def account():
# #     if user_logged_in()==True:
# #         return "your account balance is £50000"
# #     else:
# #         return redirect(url_for("home"))

# def user_logged_in():
#     return True



# if __name__=="__main__":
#     app.run(debug=True)

from flask_sqlalchemy import SQLAlchemy 

from flask import Flask, redirect, request, url_for, render_template

app = Flask(__name__)
#remote db
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@34.89.119.214/games'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True

db= SQLAlchemy(app)

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)

all_games=Games.query.all()
print(all_games)
# first_game=Games.query.first()

games_to_update=Games(name="arsenal vs man city")
game_to_update.name="everton vs man city"
db.session.commit()

games_to_delete

if __name__=="__main__":
    app.run(debug=True)