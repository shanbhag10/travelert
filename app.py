from flask import Flask, render_template, request
import time, threading
import csv
from flights import *
from alerts import *
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
        #save_alert(alert)
        display_alert = get_display_alert(alert)
        return render_template('success.html', display_alert=display_alert)

# def save_alert():
#     print('alert')

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

def get_display_alert(alert):
    display_alert = {}
    display_alert["Flight"] = alert.source +" to "+ alert.destination
    display_alert["Departure"] = alert.departure_range[0] +" to "+alert.departure_range[1]
    display_alert["Arrival"] = alert.arrival_range[0] +" to "+alert.arrival_range[1]
    display_alert["Budget"] = "$ " +alert.flight_request.cost
    display_alert["Email"] = alert.user.email
    flights = get_valid_flights(alert)
    if (len(flights) > 0):
        display_alert["flight_info_test"] = str(flights[0].cost)
    return display_alert

if __name__ == "__main__":
    app.run(debug=True)