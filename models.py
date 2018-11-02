import os
from app import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, index=True)
    password = db.Column(db.String(255))
    created_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_date = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    devices = db.relationship('Device', backref='user', lazy=True)
    profiles = db.relationship('Profile', backref='user', lazy=True)


class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mac_id = db.Column(db.String(255), unique=True, nullable=False)
    secret_key = db.Column(db.String(255), default=os.urandom(4).hex(), nullable=False)
    created_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    sold_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_name = db.Column(db.String(255), nullable=False)
    preheat_cycle = db.Column(db.Float)
    shower_cycle = db.Column(db.Float)
    shower_temp = db.Column(db.Float)
    old_shower_habits = db.Column(db.Float)
    water_used = db.Column(db.Float)
    water_saved = db.Column(db.Float)
    challenge_level = db.Column(db.Float)
    created_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    last_shower_date = db.Column(db.DateTime)
    showering_data = db.relationship('ShoweringData', backref='profile', lazy=True)


class ShoweringData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'))
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))
    created_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    # 0: norma1: challenge
    shower_mode = db.Column(db.Integer, default=0)
    preheat_cycle = db.Column(db.Float)
    shower_cycle = db.Column(db.Float)
    old_shower_habits = db.Column(db.Float)
    water_used = db.Column(db.Float)
    water_saved = db.Column(db.Float)
    shower_temp = db.Column(db.Float)
    mixing_temp = db.Column(db.Float)
    challenge_level = db.Column(db.Float)
    aggregate_water_used = db.Column(db.Float)
    average_water_used = db.Column(db.Float)
