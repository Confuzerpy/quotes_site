from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Coins, Base


app = Flask(__name__)

engine = create_engine('sqlite:///coins.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

"""Главная страница"""


@app.route('/')
def index():
    main = session.query(Coins).all()
    return render_template('index.html', main=main)
