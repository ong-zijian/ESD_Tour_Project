#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script

import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

from datetime import datetime
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("tourdbKey")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)  

class Booking(db.Model):
    __tablename__ = 'bookings'

    booking_id = db.Column(db.Integer, primary_key=True)
    startDateTime = db.Column(db.datetime, primary_key=True nullable=False)
    Tour_ID = db.Column(db.Integer, nullable=False)
    cName = db.Column(db.String(256), nullable=False)
    Postcode = db.Column(db.String(6), nullable=False)

    def json(self):
        dto = {
            'booking_id': self.booking_id,
            'startDateTime': self.startDateTime,
            'Tour_ID': self.Tour_ID,
            'cName': self.cName,
            'Postcode': self.Postcode
        }

        # dto['order_item'] = []
        # for oi in self.order_item:
        #     dto['order_item'].append(oi.json())

        return dto



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
    booking = Booking.query.filter_by(booking_id=booking_id).first()
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
    cName = request.json.get('cName', None)
    booking = Booking(cName=cName, status='NEW')

    booking_item = request.json.get('booking_item')
    ################################ !!! figure this one out###################################
    # for item in booking_item:
    #     booking.booking_item.append(Order_Item(
    #         book_id=item['book_id'], quantity=item['quantity']))

    try:
        db.session.add(booking)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the order. " + str(e)
            }
        ), 500
    
    print(json.dumps(booking.json(), default=str)) # convert a JSON object to a string and print
    print()

    return jsonify(
        {
            "code": 201,
            "data": booking.json()
        }
    ), 201


@app.route("/booking/<string:order_id>", methods=['PUT'])
def update_booking(booking_id):
    try:
        booking = Booking.query.filter_by(booking_id=booking_id).first()
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
        if data['status']:
            booking.status = data['status']
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
