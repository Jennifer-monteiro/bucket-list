from flask import Flask
from config import Config
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy


load_dotenv()



app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)


@app.route('/')
def home():
    return "ghjhgjhgj"

app.static_folder = 'static'
