from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
import csv

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
        return render_template("index.html")

@app.route("/wifi")
def wifi():
        with open ('../../Wifi/Raw/SSIDs.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            data = []
            for row in reader:
                data.append(row)
            SSID1 = data[1][13].replace('" "', 'Versteckt').replace('"', '')
            ENC1 = data [1][5].replace('"', '')
            SSID2 = data[2][13].replace('" "', 'Versteckt').replace('"', '')
            ENC2 = data [2][5].replace('"', '')
            SSID3 = data[3][13].replace('" "', 'Versteckt').replace('"', '')
            ENC3 = data [3][5].replace('"', '')
            SSID4 = data[4][13].replace('" "', 'Versteckt').replace('"', '')
            ENC4 = data [4][5].replace('"', '')
        return render_template("wifi.html", SSID1=SSID1, SSID2=SSID2, SSID3=SSID3, SSID4=SSID4, Encryption1=ENC1, Encryption2=ENC2, Encryption3=ENC3, Encryption4=ENC4)

@app.route("/kontakt")
def kontakt():
        return render_template("kontakt.html")

@app.errorhandler(404)
def default(error):
        return render_template("index.html")


if __name__ == "__main__":
        app.run(debug=True)

