from flights import *

class Alert:
	def __init__(self, source, destination, departure_range, arrival_range, flight_request, user):
		self.source = source
		self.destination = destination
		self.departure_range = departure_range
		self.arrival_range = arrival_range
		self.flight_request = flight_request
		self.user = user

class User:
	def __init__(self, email):
		self.email = email