from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class Flight:
	def __init__(self, cost, duration, stops):
		self.cost = cost
		self.duration = duration
		
		if stops == 'non':
			self.stops = 0
		else:
			self.stops = stops

chrome_options = Options()  
chrome_options.add_argument("--headless")  
driver = webdriver.Chrome('/app/.chromedriver/bin/chromedriver', options=chrome_options)
#driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=chrome_options)

def scan_skiplagged(alert):
	url = "https://skiplagged.com/flights/"+alert.source+"/"+alert.destination+"/"+alert.departure_range[0]+"/"+alert.arrival_range[0]
	driver.get(url)
	time.sleep(2)

	flights = []
	for i in range (2,20):
		try:
			cost_text = driver.find_element_by_xpath('/html/body/section/div/div/section/div/div/div/div[2]/div/div[2]/div[3]/div[6]/div/div['+str(i)+']/div[3]/p')
			duration = driver.find_element_by_xpath('/html/body/section/div/div/section/div/div/div/div[2]/div/div[2]/div[3]/div[6]/div/div['+str(i)+']/div[1]')

			#button = driver.find_element_by_xpath('/html/body/section/div/div/section/div/div/div/div[2]/div/div[2]/div[4]/div[7]/div/div[2]/div[3]/button[1]').click()

			cost = int(cost_text.text[1:])
			details = duration.text.split()
			if len(details) > 3:
				details = details[2:]

			flight = Flight(cost, details[0], details[1])
			flights.append(flight)

		except Exception as error:
			break

	return flights

def get_valid_flights(alert):
	return scan_skiplagged(alert)