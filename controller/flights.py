from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time
import json
import os

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


def scan_skiplagged(alert, debug, driver):
	url = "https://skiplagged.com/flights/"+alert.source+"/"+alert.destination+"/"+alert.departure_range[0]+"/"+alert.arrival_range[0]
	print(url)
	driver.get(url)
	#time.sleep(10)
	print(driver.title)

	flights = []
	try:
		#costs = driver.find_elements_by_class_name('trip-cost')
		#durations = driver.find_elements_by_class_name('trip-duration')
		#cost = driver.find_element_by_xpath('/html/body/section/div/div/section/div/div/div/div[2]/div/div[2]/div[3]/div[6]/div/div[2]/div[3]/p')

		wait = WebDriverWait(driver, 100)
		infinite_list = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="trip-list-sections"]/div[2]/div[3]/div[starts-with(@class, "infinite-trip-list")]')))

		#static_header = driver.find_element_by_xpath('/html/body/section/div/div/section/div/div/div/div[2]/div/div[2]/div[3]/div[3]')
		#infinite_list = driver.find_elements_by_class_name('infinite-trip-list')

	except Exception as error:
		print("Error: " + str(error))
		return flights

	#print(len(costs))
	#print(len(durations))
	#print(cost.text)
	#print(static_header.text)
	print(infinite_list.text)

	# for i in range(len(costs)):
	# 	#cost_text = driver.find_element_by_xpath('/html/body/section/div/div/section/div/div/div/div[2]/div/div[2]/div[3]/div[6]/div/div['+str(i)+']/div[3]/p')
	# 	#duration = driver.find_element_by_xpath('/html/body/section/div/div/section/div/div/div/div[2]/div/div[2]/div[3]/div[6]/div/div['+str(i)+']/div[1]')
	# 	#button = driver.find_element_by_xpath('/html/body/section/div/div/section/div/div/div/div[2]/div/div[2]/div[4]/div[7]/div/div[2]/div[3]/button[1]').click()

	# 	cost = int(costs[i].text[1:])
	# 	details = durations[i].text.split()
	# 	if len(details) > 3:
	# 		details = details[2:]

	# 	flight = Flight(cost, details[0], details[1])
	# 	print(flight.to_string())
	# 	flights.append(flight)

	return flights

def get_valid_flights(alert, debug):
	chrome_options = webdriver.ChromeOptions()  
	
	chrome_options.add_argument("--headless") 
	chrome_options.add_argument('--disable-gpu')
	chrome_options.add_argument('--disable-dev-shm-usage')
	chrome_options.add_argument('--no-sandbox')
	
	if debug == True:
		driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=chrome_options)
		#driver = swebdriver.PhantomJS()
	else:
		chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
		driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

	# options = FirefoxOptions()
	# options.add_argument("--headless")
	# driver = webdriver.Firefox(options=options)
	return scan_skiplagged(alert, debug, driver)