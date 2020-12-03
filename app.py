from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello, World!, you are adding things to test!'

app.config['DEBUG'] = True