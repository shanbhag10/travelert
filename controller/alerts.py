from controller.flights import *
import json
import uuid

class Alert:
	def __init__(self, source, destination, departure_range, arrival_range, flight_request, user):
		self.id = str(uuid.uuid4())
		self.source = source
		self.destination = destination
		self.departure_range = departure_range
		self.arrival_range = arrival_range
		self.flight_request = flight_request
		self.user = user

	def to_string(self):
		return self.__dict__

class User:
	def __init__(self, email):
		self.id = str(uuid.uuid4())
		self.email = email

def get_display_alert(alert):
    display_alert = {}
    display_alert["Flight"] = alert.source +" to "+ alert.destination
    display_alert["Departure"] = alert.departure_range[0] +" to "+alert.departure_range[1]
    display_alert["Arrival"] = alert.arrival_range[0] +" to "+alert.arrival_range[1]
    display_alert["Budget"] = "$ " +alert.flight_request.cost
    display_alert["Email"] = alert.user.email
    
    # flights = get_valid_flights(alert, app.debug)
    # if (len(flights) > 0):
    #     display_alert["flight_info_test"] = str(flights[0].cost)
    return display_alert