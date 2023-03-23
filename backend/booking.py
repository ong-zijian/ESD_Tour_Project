#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script

import os
#import logging for log
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv

# To load the environment variable
load_dotenv()

from datetime import datetime
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("tourdbKey")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

# Create a logger object
logger = logging.getLogger(__name__)

db = SQLAlchemy(app)

CORS(app)  

# Create Class for the Booking
class Booking(db.Model):
    __tablename__ = 'bookings'

    BID = db.Column(db.Integer, autoincrement=True, primary_key=True)
    startDateTime = db.Column(db.DateTime(timezone=True), primary_key=True)
    TID = db.Column(db.Integer, nullable=False)
    cName = db.Column(db.String(256), nullable=False)
    Postcode = db.Column(db.String(6), nullable=False)

    def json(self):
        dto = {
            'booking_id': self.BID,
            'startDateTime': self.startDateTime,
            'Tour_ID': self.TID,
            'cName': self.cName,
            'Postcode': self.Postcode
        }
        return dto



@app.route("/booking")
def get_all():
    try:
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
    except Exception as e:
        logger.exception("An error occurred while getting all bookings")
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while getting all bookings"
            }
        ), 500



@app.route("/booking/<string:booking_id>")
def find_by_booking_id(booking_id):
    try:
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
    except Exception as e:
        logger.exception(f"An error occurred while finding booking by id {booking_id}")
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while finding booking by id"
            }
        ), 500


def create_booking():
    cName = request.json.get("cName", None)
    TourID = request.json.get("TID", None)
    startDateTime = request.json.get("startDateTime", None)
    Postcode = request.json.get("Postcode", None)

    booking = Booking(cName=cName, TID=TourID, startDateTime=startDateTime, Postcode=Postcode)

    try:
        with db.session.begin():
            db.session.add(booking)
            db.session.flush()
    except Exception as e:
        logger.error("An error occurred while creating the order. " + str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the order. " + str(e)
            }
        ), 500

    logger.info("Booking created: %s", booking.json())

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
            logger.warning("Order not found. Booking ID: %s", booking_id)
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
            logger.info("Booking updated. Booking ID: %s", booking_id)
            return jsonify(
                {
                    "code": 200,
                    "data": booking.json()
                }
            ), 200
    except Exception as e:
        logger.error("An error occurred while updating the order. Booking ID: %s Error: %s", booking_id, str(e))
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
