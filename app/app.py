from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:Mydatabase123@database-1.cfug2sa2wjus.eu-north-1.rds.amazonaws.com/recipe_sharing'
db = SQLAlchemy(app)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return 'Welcome to the Recipe Sharing Platform!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
