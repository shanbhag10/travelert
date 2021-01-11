from flask import Flask, render_template, request
import time, threading
import csv
from controller.flights import *
from controller.alerts import *
from dynamo.alerts_db import *
import logging

app = Flask(__name__)

@app.route("/")
def home():
    airports = get_airports()
    return render_template('index.html', airports=airports)

@app.route("/success", methods=['POST', 'GET'])
def create_alert():
    if request.method == 'POST':
        alert = create_alert_from_input(request.form)
        save_alert(alert)
        display_alert = get_display_alert(alert)
        return render_template('success.html', display_alert=display_alert)

# def scan_flights():
#     #for all alerts
#     #get_valid_flights()
# 	  threading.Timer(10, scan_flights).start()

def create_alert_from_input(request):
    departure_range = (request["Departure_st"], request["Departure_end"])
    arrival_range = (request["Arrival_st"], request["Arrival_end"])
    flight_request = Flight(request["Budget"], '8h', '1')
    user = User(request["Email"])
    alert = Alert(request["From"], request["To"], departure_range, arrival_range, flight_request, user)
    print(alert.to_string())
    return alert

def get_airports():
    airports = []
    with open('static/airport_data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            airports.append(row[4] +" - "+row[1])

    return sorted(airports)

if __name__ == "__main__":
    app.run(debug=True)