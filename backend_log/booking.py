#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script

import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
from werkzeug.routing import BaseConverter

# To load the environment variable
load_dotenv()

from datetime import datetime
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("tourdbKey")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)  

# Create Class for the Booking
class Booking(db.Model):
    __tablename__ = 'bookings'

    BID = db.Column(db.Integer, autoincrement=True, primary_key=True)
    startDateTime = db.Column(db.DateTime(timezone=True), primary_key=True)
    TID = db.Column(db.ForeignKey('tours.TID', ondelete='CASCADE'),primary_key=True)
    cName = db.Column(db.String(256), nullable=False)
    Email = db.Column(db.String(256), nullable=False)
    Price = db.Column(db.Float, nullable=False)

    def json(self):
        dto = {
            'booking_id': self.BID,
            'startDateTime': self.startDateTime,
            'Tour_ID': self.TID,
            'cName': self.cName,
            'Email': self.Email,
            "Price": self.Price
        }
        return dto
    

# Create Class for the Tour
class Tour(db.Model):
    __tablename__ = 'tours'

    TID = db.Column(db.Integer, autoincrement=True, primary_key=True)
    Title = db.Column(db.String(64), nullable=False)
    Description = db.Column(db.String(1000), nullable=False)
    Postcode = db.Column(db.String(6), nullable=False)
    Price = db.Column(db.Float, nullable=False)

    def json(self):
        dto = {
            'Tour_ID': self.TID,
            'Title':self.Title,
            'Description': self.Description,
            'Postcode': self.Postcode,
            "Price": self.Price
        }
        dto['details'] = []
        for detail in self.idv_tours:
            dto['details'].append(detail.json())

        return dto

# Create Class for the Idv_Tour
class idv_tours(db.Model):
    __tablename__ = 'idv_tours'

    startDateTime = db.Column(db.DateTime(timezone=True), primary_key=True)
    TID = db.Column(db.ForeignKey('tours.TID', ondelete='CASCADE'), primary_key=True, nullable=False)
    endDateTime = db.Column(db.DateTime(timezone=True))
    TotalSlot = db.Column(db.Integer, nullable=False)
    TakenSlot = db.Column(db.Integer, nullable=False)

    tour = db.relationship("Tour", primaryjoin="idv_tours.TID == Tour.TID", backref="idv_tours")
    def json(self):
        return {'TID':self.TID, 'startDateTime':self.startDateTime, 'endDateTime':self.endDateTime, 'TotalSlot':self.TotalSlot, 'TakenSlot':self.TakenSlot}
    
class DateTimeConverter(BaseConverter):
    """Custom converter for datetime objects."""

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')

    def to_url(self, value):
        return value.strftime('%Y-%m-%dT%H:%M:%S')
    
app.url_map.converters['datetime'] = lambda pattern: DateTimeConverter(pattern)



@app.route("/booking")
def get_all():
    bookinglist = Booking.query.all()
    if len(bookinglist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "bookings": [booking.json() for booking in bookinglist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no booking."
        }
    ), 404


@app.route("/booking/<string:booking_id>")
def find_by_booking_id(booking_id):
    booking = Booking.query.filter_by(BID=booking_id).first()
    if booking:
        return jsonify(
            {
                "code": 200,
                "data": booking.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "booking_id": booking_id
            },
            "message": "Booking not found."
        }
    ), 404


@app.route("/booking", methods=['POST'])
def create_booking():
    cName = request.json.get("cName", None)
    TourID = request.json.get("TID", None)
    startDateTime = request.json.get("startDateTime", None)
    Email = request.json.get("Email", None)
    Price = request.json.get("Price", None)


    booking = Booking(cName=cName, TID=TourID, startDateTime=startDateTime, Email=Email, Price=Price)

    try:
        with db.session.begin():
            db.session.add(booking)
            db.session.flush()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the order. " + str(e)
            }
        ), 500

    print(json.dumps(booking.json(), default=str))
    print()

    return jsonify(
        {
            "code": 201,
            "data": booking.json()
        }
    ), 201


@app.route("/booking/<string:booking_id>", methods=['PUT'])
def update_booking(booking_id):
    try:
        booking = Booking.query.filter_by(BID=booking_id).first()
        if not booking:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "booking_id": booking_id
                    },
                    "message": "Order not found."
                }
            ), 404

        # update status
        data = request.get_json()
        if data['cName']:
            booking.cName = data['cName']
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "data": booking.json()
                }
            ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "booking_id": booking_id
                },
                "message": "An error occurred while updating the order. " + str(e)
            }
        ), 500


if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": manage orders ...")
    app.run(host='0.0.0.0', port=5001, debug=True)
