import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import logging

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

# Create Class for the Tour
class Tour(db.Model):
    __tablename__ = 'tours'

    TID = db.Column(db.Integer, autoincrement=True, primary_key=True)
    Title = db.Column(db.String(64), nullable=False)
    Description = db.Column(db.String(1000), nullable=False)
    Postcode = db.Column(db.String(6), nullable=False)

    def json(self):
        dto = {
            'Tour_ID': self.TID,
            'Title':self.Title,
            'Description': self.Description,
            'Postcode': self.Postcode
        }
        dto['details'] = []
        for detail in self.idv_tours:
            dto['details'].append(detail.json())

        return dto

# Create Class for the Idv_Tour
class idv_tours(db.Model):
    __tablename__ = 'idv_tours'

    startDateTime = db.Column(db.DateTime(timezone=True), primary_key=True)
    TID = db.Column(db.ForeignKey('tours.TID'), primary_key=True, nullable=False)
    endDateTime = db.Column(db.DateTime(timezone=True))
    TotalSlot = db.Column(db.Integer, nullable=False)
    TakenSlot = db.Column(db.Integer, nullable=False)

    tour = db.relationship("Tour", primaryjoin="idv_tours.TID == Tour.TID", backref="idv_tours")
    def json(self):
        return {'TID':self.TID, 'startDateTime':self.startDateTime, 'endDateTime':self.endDateTime, 'TotalSlot':self.TotalSlot, 'TakenSlot':self.TakenSlot}
    
# Basic Route for get all function
@app.route("/tour")
def get_all():
    tourlist = Tour.query.all()
    if len(tourlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "tour": [tour.json() for tour in tourlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no tours."
        }
    ), 404

@app.route("/tour/<string:TID>")
def find_by_title(TID):
    tour = Tour.query.filter_by(TID=TID).first()
    if tour:
        return jsonify(
            {
                "code": 200,
                "data": tour.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Tour not found."
        }
    ), 404


@app.route("/tour", methods=['POST'])
def create_tour():
    title = request.json.get('Title', None)
    description = request.json.get('Description', None)  # Add this line
    postcode = request.json.get('Postcode', None)
    newTour = Tour(Title=title, Description=description, Postcode=postcode)  # Modify this line

    if (Tour.query.filter_by(Title=title).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "Title": title
                },
                "message": "Tour name already exists."
            }
    ), 400

    details = request.json.get('details')
    for item in details:
        new_idv_tour = idv_tours(startDateTime=item['startDateTime'], endDateTime=item['endDateTime'], TotalSlot=item['TotalSlot'], TakenSlot=item['TakenSlot'])
        new_idv_tour.tour = newTour
        db.session.add(new_idv_tour)
    try:
        db.session.add(newTour)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "title": title
                },
                "message": "An error occurred creating the Tour." + str(e)
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": newTour.json()
        }
    ), 201


@app.route("/book/<string:isbn13>", methods=['PUT'])
def update_book(isbn13):
    book = Book.query.filter_by(isbn13=isbn13).first()
    if book:
        data = request.get_json()
        if data['title']:
            book.title = data['title']
        if data['price']:
            book.price = data['price']
        if data['availability']:
            book.availability = data['availability'] 
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": book.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "isbn13": isbn13
            },
            "message": "Book not found."
        }
    ), 404


@app.route("/book/<string:title>", methods=['DELETE'])
def delete_book(Title):
    tour = Tour.query.filter_by(Title=Title).first()
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "isbn13": isbn13
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "isbn13": isbn13
            },
            "message": "Book not found."
        }
    ), 404
app.logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
app.logger.addHandler(handler)

if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": manage orders ...")
    app.run(host='0.0.0.0', port=5002, debug=True)