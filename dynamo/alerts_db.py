import boto3
import datetime
import uuid

def save_alert(alert):
	dynamodb = boto3.resource('dynamodb')
	table = dynamodb.Table('alerts')

	item = {
		"from":alert.source,
		"to":alert.destination,
		"departure_range_st":alert.departure_range[0],
		"departure_range_end":alert.departure_range[1],
		"arrival_range_st":alert.arrival_range[0],
		"arrival_range_end":alert.arrival_range[1],
		"budget":alert.flight_request.cost,
		"user_id":alert.user.email,
		"alert_id":alert.id,
		"created_at":str(datetime.datetime.now())
	}

	table.put_item(Item=item)