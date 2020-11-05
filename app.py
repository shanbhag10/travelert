from flask import Flask, render_template, request
import csv
app = Flask(__name__)

@app.route("/")
def home():
    airports = getAirports()
    return render_template('index.html', airports=airports)

@app.route("/success", methods=['POST', 'GET'])
def createAlert():
    if request.method == 'POST':
        result = request.form
        alert = {}
        alert["Flight"] = result["From"] +" to "+ result["To"]
        alert["Departure"] = result["Departure_st"] +" to "+result["Departure_end"]
        alert["Arrival"] = result["Arrival_st"] +" to "+result["Arrival_end"]
        alert["Budget"] = "$ " +result["Budget"]
        alert["Email"] = result["Email"]
        return render_template('success.html', alert=alert)

def getAirports():
    airports = []
    with open('static/airport_data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            airports.append(row[4] +" - "+row[1])

    return sorted(airports)

if __name__ == "__main__":
    app.run(debug=True)