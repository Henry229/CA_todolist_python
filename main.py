import os
from flask import Flask
from db import db, ma
from controllers.todo_controller import todo_bp


# def create_app():

app = Flask(__name__)
# app.secret_key = 'this is super key'

app.config['SECRET_KEY'] = 'This is super key'
# app.config['SESSION_TYPE'] = 'filesystem'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

db.init_app(app)

app.register_blueprint(todo_bp)

@app.cli.command('create')
def create_db():
    db.create_all()
    print("Tables created")    

@app.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")    
    
    # return app

