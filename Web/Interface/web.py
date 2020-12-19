from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
import csv
import requests

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

            i=1
            render_str=''
            #renderstr+=('"wifi.html"')
            for i in range(0,15):
                exec("global SSID%d; global ENC%d; global MAC%d; global ls%d; SSID%d='';ENC%d=''; MAC%d='';ls%d='';"% (i+1, i+1, i+1, i+1,i+1,i+1,i+1,i+1));
            for i in range(1,len(data)):
                exec("""global SSID%d; SSID%d = data[%d][13].replace('" "', 'Versteckt').replace('"', '');""" % (i,i,i));
                exec("""global ENC%d; ENC%d = data[%d][5].replace('"', '');""" % (i,i,i)); 
                exec("""global MAC%d; MAC%d = data[%d][0].replace('"', '');""" % (i,i,i));
                exec("""global ls%d; ls%d = data[%d][2].replace('"', '');""" % (i,i,i));

        return render_template("wifi.html", SSID1=SSID1, SSID2=SSID2, SSID3=SSID3, SSID4=SSID4, SSID5=SSID5, SSID6=SSID6, SSID7=SSID7, SSID8=SSID8, SSID9=SSID9, SSID10=SSID10, SSID11=SSID11, SSID12=SSID12, SSID13=SSID13, SSID14=SSID14, SSID15=SSID15, Encryption1=ENC1, Encryption2=ENC2, Encryption3=ENC3, Encryption4=ENC4, Encryption5=ENC5, Encryption6=ENC6, Encryption7=ENC7, Encryption8=ENC8, Encryption9=ENC9, Encryption10=ENC10, Encryption11=ENC11, Encryption12=ENC12, Encryption13=ENC13, Encryption14=ENC14, Encryption15=ENC15, MAC1=MAC1, MAC2=MAC2, MAC3=MAC3, MAC4=MAC4, MAC5=MAC5, MAC6=MAC6, MAC7=MAC7,MAC8=MAC8,MAC9=MAC9,MAC10=MAC10,MAC11=MAC11,MAC12=MAC12,MAC13=MAC13,MAC14=MAC14,MAC15=MAC15,ls1=ls1,ls2=ls2,ls3=ls3,ls4=ls4,ls5=ls5,ls6=ls6,ls7=ls7,ls8=ls8,ls9=ls9,ls10=ls10,ls11=ls11,ls12=ls12,ls13=ls13,ls14=ls14,ls15=ls15 )

@app.route("/ble")
def ble():
        with open ('../../BLE/Raw/Devs.csv', newline='') as BLEcsvfile:
            BLEreader = csv.reader(BLEcsvfile, delimiter=',', quotechar='|')
            BLEdata = []
            for i in range(0,15):
                exec("global Name%d; global MAC%d; global connect%d; global vendor%d; Name%d='';MAC%d=''; connect%d=''; vendor%d='';"% (i+1, i+1, i+1, i+1,i+1,i+1,i+1,i+1));

            for row in BLEreader:
                BLEdata.append(row)
            
            for i in range(1,len(BLEdata)):
                exec("""global Name%d; Name%d = BLEdata[%d][0].replace('"', '');""" % (i,i,i)); 
                exec("""global MAC%d; MAC%d = BLEdata[%d][1].replace('"', '');""" % (i,i,i)); 
                exec("""global vendor%d; vendor%d = BLEdata[%d][3].replace('"', '');""" % (i,i,i)); 
                exec("""global connect%d; connect%d = BLEdata[%d][2].replace('"', '').replace('True', 'Ja').replace('False','Nein');""" % (i,i,i)); 
        return render_template("ble.html", Name1=Name1, Name2=Name2, Name3=Name3, Name4=Name4, Name5=Name5, Name6=Name6, Name7= Name7, Name8=Name8,Name9=Name9,Name10=Name10,Name11=Name11,Name12=Name12,Name13=Name13,Name14=Name14,Name15=Name15, MAC1=MAC1, MAC2=MAC2, MAC3=MAC3, MAC4=MAC4, MAC5=MAC5, MAC6=MAC6, MAC7=MAC7,MAC8=MAC8,MAC9=MAC9,MAC10=MAC10,MAC11=MAC11,MAC12=MAC12,MAC13=MAC13,MAC14=MAC14,MAC15=MAC15, connect1=connect1, connect2=connect2, connect3=connect3, connect4=connect4, connect5=connect5, connect6=connect6, connect7=connect7,connect8=connect8,connect9=connect9,connect10=connect10,connect11=connect11,connect12=connect12,connect13=connect13,connect14=connect14,connect15=connect15, vendor1=vendor1, vendor2=vendor2, vendor3=vendor3, vendor4=vendor4, vendor5=vendor5, vendor6=vendor6, vendor7=vendor7,vendor8=vendor8,vendor9=vendor9,vendor10=vendor10,vendor11=vendor11,vendor12=vendor12,vendor13=vendor13,vendor14=vendor14,vendor15=vendor15)
    

@app.errorhandler(404)
def default(error):
       return render_template("index.html")


if __name__ == "__main__":
        app.run(debug=True)

