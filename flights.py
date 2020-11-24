from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.common.by import By
import time
import json

GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

chrome_options = Options()  
chrome_options.add_argument("--headless")  

class Flight:
	def __init__(self, cost, duration, stops):
		self.cost = cost
		self.duration = duration
		
		if stops == 'non':
			self.stops = '0'
		else:
			self.stops = stops

	def to_string(self):
		return self.__dict__

def scan_skiplagged(alert, debug):
	if debug == True:
		driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=chrome_options)
	else:
		chrome_options.add_argument('--disable-gpu')
		chrome_options.add_argument('--no-sandbox')
		#chrome_options.binary_location = GOOGLE_CHROME_PATH
		driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=chrome_options)

	url = "https://skiplagged.com/flights/"+alert.source+"/"+alert.destination+"/"+alert.departure_range[0]+"/"+alert.arrival_range[0]
	print(url)
	driver.get(url)
	WebDriverWait(driver, 100).until(visibility_of_element_located((By.XPATH, '/html/body/section/div/div/section/div/div/div/div[2]/div/div[2]/div[3]/div[6]/div/div[2]/div[3]/p')))
	time.sleep(10)

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
			print(flight.to_string())
			flights.append(flight)

		except Exception as error:
			print("error" + str(error))
			break

	return flights

def get_valid_flights(alert, debug):
	return scan_skiplagged(alert, debug)