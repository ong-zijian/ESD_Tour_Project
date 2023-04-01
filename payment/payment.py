#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script

import os
#import pika for the log
import pika
#import logging for payment log
import logging
import traceback
from dotenv import load_dotenv
import stripe
from flask import Flask,jsonify,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
now = datetime.now()


load_dotenv()
dbURL=os.getenv('dbURL')

# logger = logging.getLogger(__name__)
# configure logger
# logging.basicConfig(level=logging.DEBUG, filename='app.log', format='%(asctime)s %(levelname)s %(message)s')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = dbURL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)


# @app.route('/log')
# def show_log():
#     # Read the logged messages from the logger object
#     log_messages = []
#     for handler in logging.getLogger().handlers:
#         if isinstance(handler, logging.FileHandler):
#             with open(handler.baseFilename, 'r') as log_file:
#                 log_messages = log_file.readlines()

    # # Create an HTML table to display the logged messages
    # table_html = '<table><thead><tr><th>Time</th><th>Level</th><th>Message</th></tr></thead><tbody>'
    # for message in log_messages:
    #     time, level, message = message.strip().split(' ', 2)
    #     table_html += f'<tr><td>{time}</td><td>{level}</td><td>{message}</td></tr>'
    # table_html += '</tbody></table>'

    # return table_html

class Booking(db.Model):
    __tablename__="bookings"

    BID=db.Column(db.Integer, primary_key=True)
    startDateTime=db.Column(db.DateTime(timezone=True),primary_key=True)
    TID=db.Column(db.ForeignKey('tours.TID', ondelete='CASCADE'), nullable=False)
    cName=db.Column(db.String(256),nullable=False)
    Postcode=db.Column(db.String(6),nullable=False)

    def json(self):
        return {
            "BID" : self.BID,
            "startDateTime" : self.startDateTime,
            "TID":self.TID,
            "cName" : self.cName,
            "Postcode" : self.Postcode
        }



class Payments(db.Model):
    __tablename__ = 'payments'

    PID = db.Column(db.Integer,autoincrement=True,primary_key=True)
    PdateTime = db.Column(db.DateTime(timezone=True), nullable=False)
    BID = db.Column(db.ForeignKey('bookings.BID',ondelete='CASCADE'),primary_key=True, nullable=False)

    booking = db.relationship("Booking", primaryjoin="Payments.BID == Booking.BID", backref="Payments")

    def json(self):
        return {"PID": self.PID, 
                "PdateTime": self.PdateTime, 
                "BID": self.BID}



stripe_keys = {
    "secret_key":os.getenv('STRIPE_SECRET_KEY'),
    "publishable_key":os.getenv('STRIPE_PUBLISHABLE_KEY'),
    "endpoint_secret":os.getenv('STRIPE_ENDPOINT_SECRET')
}

stripe.api_key = stripe_keys["secret_key"]


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/config")
def get_publishable_key():
    stripe_config={"publicKey":stripe_keys["publishable_key"]}
    return jsonify(stripe_config)



@app.route("/checkout-session")
def create_checkout_session():
    domain_url="http://127.0.0.1:5200/"
    stripe.api_key=stripe_keys["secret_key"]
    # Assigned the Stripe secret key to stripe.api_key (so it will be sent automatically when we make a request to create a new Checkout Session)

    try:
        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url+"success?session_id{CHECKOUT_SESSION_ID}",
            cancel_url=domain_url+"cancelled",
            payment_method_types=['card'],
            mode="payment",
            line_items=[
            {
                "price":'price_1MluLTA7CL0wKMv1WzcFON50',
                "quantity":1
            },
            ]
        )
        # Activity log
        message = f"Checkout session created successfully with session ID {checkout_session['id']}"
        send_to_queue(message)
        return jsonify({"sessionId":checkout_session["id"]})
    
    except Exception as e:
        # Error log
        message = f"Failed to create checkout session: {str(e)}"
        send_to_queue(message)
        return jsonify(error=str(e)),403
    
def send_to_queue(message):
    # Connect to AMQP server
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Declare queue
    channel.queue_declare(queue='logs')

    # Send message to queue
    channel.basic_publish(exchange='', routing_key='logs', body=message)

    # Close connection
    connection.close()

@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/cancelled")
def cancelled():
    return render_template("cancelled.html")


@app.route('/webhook',methods=['POST'])
def stripe_webhook():
    payload=request.get_data(as_text=True)
    sig_header=request.headers.get('Stripe-Signature')

    try:
        event=stripe.Webhook.construct_event(payload,sig_header,stripe_keys['endpoint_secret'])

    except ValueError as e:
        #error log
        # logger.error(f'Invalid payload: {e}')
        return {
                'code':400,
                'message':'Invalid payload, sent for error handling'
                }
        
    except stripe.error.SignatureVerificationError as e:
        #error log
        # logger.error(f'Invalid signature: {e}')
        return {
                'code':400,
                'message':'Invalid signature, sent for error handling'
                }
        
    
    if event['type']=='checkout.session.completed':
        #activity log
        # logger.info('Payment successful')
        print ('Payment successful')
        create_payment()

        
    return "Success", 200


def create_payment():
    # logger.info('Creating payment')
    print('in creating payment function')

    payment = Payments(PdateTime=now,BID=1)

    try:
        print('Creating now...')
        # logger.info('Adding payment to database')
        db.session.add(payment)
        db.session.commit()
        print('Done creating')
        # logger.info('Payment added successfully')
    except:
        #error log
        # logger.error('An error occurred while adding payment to the database', exc_info=True)
        print('error!!')
        print(traceback.format_exc())
        return jsonify(
            {
                "code": 500,
                "data": {
                    "BID": 1
                },
                "message": "An error occurred creating the payment record and is sent for error handling"
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": payment.json()
        }
    ), 201



if __name__ == "__main__":
    app.run(port=5200,debug=True)