# import sys
# # from sqlalchemy import Column, ForeignKey, Integer, String
# # from sqlalchemy.ext.declarative import declarative_base
# # from sqlalchemy.orm import relationship
# # from sqlalchemy import create_engine
# # from flask_sqlalchemy import SQLAlchemy
# from . import appe


# # Base = declarative_base()
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coins.db'
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # db = SQLAlchemy(app)
# db = appe.db


# class Coins(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     symbol = db.Column(db.String(100))
#     name = db.Column(db.String(100))
#     price = db.Column(db.String(100))
#     market_cap = db.Column(db.String(100))
#     volume_24h = db.Column(db.String(100))
#     delta_24h = db.Column(db.String(100))
