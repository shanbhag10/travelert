from flask import Flask, render_template
import csv
app = Flask(__name__)

@app.route("/")
def home():
    airports = getAirports()
    return render_template('index.html', airports=airports)

def getAirports():
    airports = []
    with open('static/airport_data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            airports.append(row[4] +" - "+row[1])

    return sorted(airports)

if __name__ == "__main__":
    app.run(debug=True)