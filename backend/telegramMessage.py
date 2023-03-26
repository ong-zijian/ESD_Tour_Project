import os
import json
import requests
from dotenv import load_dotenv

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


load_dotenv()
API_TOKEN = os.getenv("telegramAPItoken")

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

        return dto


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
            'startDateTime': str(self.startDateTime),
            'Tour_ID': self.TID,
            'cName': self.cName,
            'Postcode': self.Postcode
        }
        return dto
    

# Route to get the individual tour
@app.route("/tour/<string:TID>")
def find_by_title(TID):
    tour = Tour.query.filter_by(TID=TID).first()
    if tour:
        tour1 = tour.json()
        return json.dumps(tour1)
    return jsonify(
        {
            "code": 404,
            "message": "Tour not found."
        }
    ), 404

@app.route("/booking/<string:booking_id>")
def find_by_booking_id(booking_id):
    booking = Booking.query.filter_by(BID=booking_id).first()
    if booking:
        booking1 = booking.json()
        return json.dumps(booking1)
    return jsonify(
        {
            "code": 404,
            "data": {
                "booking_id": booking_id
            },
            "message": "Booking not found."
        }
    ), 404

@app.route('/receive_chat_id', methods=['POST'])
def receive_chat_id():
    #Get the data from the request and pull out the `Chat ID` and `BID`
    data = request.json
    chat_id = data['chat_id']
    bid = data["bid"]
    
    # Send a message to the booking get route
    response = requests.get(f'http://127.0.0.1:5010/booking/{bid}')
    if response.status_code == 200:
        data2 = json.loads(response.content)
        # Split the datetime into date and time
        datetime1 = data2["startDateTime"]
        datetime1 = datetime1.split(" ")

        # Get the tour information with the tour get route
        tour = requests.get(f'http://127.0.0.1:5010/tour/{data2["Tour_ID"]}')
        if tour.status_code == 200:
            tourDetails = json.loads(tour.content)
            string = f'Dear {data2["cName"]}, \n\nYour booking of ID {data2["Tour_ID"]} is confirmed. Here are the details: \n- Title: {tourDetails["Title"]}\n- Description: {tourDetails["Description"]}\n- Date: {datetime1[0]} \n- Time: {datetime1[1]} \n- Location: {data2["Postcode"]} \n\nEnjoy your tour!'
            send_message(string, chat_id)
    else:
        send_message(f"Booking with ID {bid} not found.", chat_id)
    print(chat_id)
    return 'OK'


def send_message(text, chat_id):
    # Define the API endpoint for sending messages
    api_url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    # Define the payload for the API request
    payload = {
        "text": text,
        "chat_id": chat_id
    }
    # Send the API request
    response = requests.post(api_url, json=payload)
    # Parse the response and check for errors
    if response.status_code != 200:
        print(f"Error sending message: {response.text}")
    else:
        pass

if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": manage orders ...")
    app.run(host='0.0.0.0', port=5010, debug=True)