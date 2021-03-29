import sqlite3
from flask import Flask, render_template


app = Flask(__name__)

"""Получаем данные из БД"""
def get_db_connection():
    conn = sqlite3.connect('coins.db')
    conn.row_factory = sqlite3.Row
    return conn


"""Главная страница"""
@app.route('/')
def index():
    conn = get_db_connection()
    main = conn.execute('SELECT * FROM coins').fetchall()
    conn.close()
    return render_template('index.html', main=main)
