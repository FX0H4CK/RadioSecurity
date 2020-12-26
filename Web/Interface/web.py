#!/usr/bin/python3

from flask import Flask, redirect, url_for, render_template, request, session, flash

from datetime import timedelta
import csv
import requests
import mariadb

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
        try:
            conn = mariadb.connect(
                    user="reader",
                    password="PW4readonly",
                    host="127.0.0.1",
                    port=3306,
                    database="radio_mon"
            )
        except mariadb.Error as e:
            print(f"[x] Error while Connecting: {e}")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM ssids where status IS NULL;")
            unknown = cursor.fetchall()
            cursor.execute("SELECT * FROM ssids;")
            allssids = cursor.fetchall()
            percent=len(unknown)/len(allssids)*100;
            percent=100-int(percent)
            if percent<70:
                color='orange'
            else:
                color='green'
           
            cursor.execute("SELECT * FROM ssids where privacy LIKE '%WPA2%';")
            encrypted = cursor.fetchall()
            percent_enc=len(encrypted)/len(allssids)*100;
            percent_enc=int(percent_enc)
            if percent_enc>70:
                color_enc='green'
            else:
                color_enc='orange'
            
            cursor.execute("SELECT * FROM ble;")
            allble = cursor.fetchall()
            cursor.execute("SELECT * FROM ble WHERE status IS NULL;")
            unkownble = cursor.fetchall()
            ble_known=len(unkownble)/len(allble)*100;
            ble_known=100-int(ble_known)
            if ble_known<70:
                color_ble_known='orange'
            else:
                color_ble_known='green'
        except mariadb.Error as e:
            print(f"[x] Error while Reading Data: {e}")
        return render_template("index.html",ble_known=ble_known,color_ble_known=color_ble_known, percent=percent, color=color, percent_enc=percent_enc,color_enc=color_enc)


@app.route("/wifi", methods=["POST", "GET"])
def wifi():
    if request.method == "POST":
        accept = request.form["accept"] # returned mac from button
        if accept.split(',',1)[0]=="ignore": #If Button ignore
            mac = accept.split(',',1)[1].split(',',1)[0].strip()
            ssid = accept.split(',',1)[1].split(',',1)[1].strip()
            query="UPDATE ssids SET status=2 WHERE bssid='"+mac+"' AND essid=' "+ssid+"';"
        elif accept.split(',',1)[0]=="accept": #If Button Bekannt
            mac = accept.split(',',1)[1].split(',',1)[0].strip()
            ssid = accept.split(',',1)[1].split(',',1)[1].strip()
            query="UPDATE ssids SET status=1 WHERE bssid='"+mac+"' AND essid=' "+ssid+"';"
        
        #Connect to Database
        try:
            conn = mariadb.connect(
                    user="writer",
                    password="PW4Writer!",
                    host="127.0.0.1",
                    port=3306,
                    database="radio_mon"
            )
        except mariadb.Error as e:
            print(f"[x] Error while connecting: {e}")
        cursor = conn.cursor()
        # Update Status of Entry
        try:
            cursor.execute(query)
            conn.commit()
            conn.close()
        except mariadb.Error as e:
            print(f"[x] Error while executing update: {e}")

        return redirect(url_for("wifi"))
    else:
        for i in range(0,15):
            exec("global SSID%d; global ENC%d; global MAC%d; global ls%d; global vendor%d; SSID%d='';ENC%d=''; MAC%d='';ls%d='';vendor%d='';"% (i+1, i+1, i+1, i+1,i+1,i+1,i+1,i+1,i+1,i+1));
        try:
            conn = mariadb.connect(
                    user="reader",
                    password="PW4readonly",
                    host="127.0.0.1",
                    port=3306,
                    database="radio_mon"
            )
        except mariadb.Error as e:
            print(f"[x] Error while Connecting: {e}")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM ssids;")
            ssids = cursor.fetchall()
        except mariadb.Error as e:
            print(f"[x] Error while Reading Data: {e}")
        
        for i in range(0,len(ssids)):
                exec("""global SSID%d; SSID%d = ssids[%d][13].replace('" "', 'Versteckt').replace('"', '');""" % (i+1,i+1,i));
                exec("""global ENC%d; ENC%d = ssids[%d][5].replace('"', '');""" % (i+1,i+1,i)); 
                exec("""global MAC%d; MAC%d = ssids[%d][0].replace('"', '');""" % (i+1,i+1,i));
                exec("""global ls%d; ls%d = ssids[%d][2];""" % (i+1,i+1,i));
                exec("""global vendor%d; vendor%d = ssids[%d][14];"""% (i+1,i+1,i));
        conn.close()

        return render_template("wifi.html",button='Bekannt', SSID1=SSID1, SSID2=SSID2, SSID3=SSID3, SSID4=SSID4, SSID5=SSID5, SSID6=SSID6, SSID7=SSID7, SSID8=SSID8, SSID9=SSID9, SSID10=SSID10, SSID11=SSID11, SSID12=SSID12, SSID13=SSID13, SSID14=SSID14, SSID15=SSID15, Encryption1=ENC1, Encryption2=ENC2, Encryption3=ENC3, Encryption4=ENC4, Encryption5=ENC5, Encryption6=ENC6, Encryption7=ENC7, Encryption8=ENC8, Encryption9=ENC9, Encryption10=ENC10, Encryption11=ENC11, Encryption12=ENC12, Encryption13=ENC13, Encryption14=ENC14, Encryption15=ENC15, MAC1=MAC1, MAC2=MAC2, MAC3=MAC3, MAC4=MAC4, MAC5=MAC5, MAC6=MAC6, MAC7=MAC7,MAC8=MAC8,MAC9=MAC9,MAC10=MAC10,MAC11=MAC11,MAC12=MAC12,MAC13=MAC13,MAC14=MAC14,MAC15=MAC15,ls1=ls1,ls2=ls2,ls3=ls3,ls4=ls4,ls5=ls5,ls6=ls6,ls7=ls7,ls8=ls8,ls9=ls9,ls10=ls10,ls11=ls11,ls12=ls12,ls13=ls13,ls14=ls14,ls15=ls15, vendor1=vendor1, vendor2=vendor2, vendor3=vendor2,vendor4=vendor4,vendor5=vendor5,vendor6=vendor6,vendor7=vendor7,vendor8=vendor8,vendor9=vendor9,vendor10=vendor10,vendor11=vendor11,vendor12=vendor12,vendor13=vendor13,vendor14=vendor14,vendor15=vendor15)

@app.route("/wifi/ignored", methods=["POST", "GET"])
def ignoredwifi():
    if request.method == "POST":
        accept = request.form["accept"] # returned mac from button
        if accept.split(',',1)[0]=="ignore": #If Button ignore
            mac = accept.split(',',1)[1].split(',',1)[0].strip()
            ssid = accept.split(',',1)[1].split(',',1)[1].strip()
            query="UPDATE ssids SET status=2 WHERE bssid='"+mac+"' AND essid=' "+ssid+"';"
        elif accept.split(',',1)[0]=="accept": #If Button Bekannt
            mac = accept.split(',',1)[1].split(',',1)[0].strip()
            ssid = accept.split(',',1)[1].split(',',1)[1].strip()
            query="UPDATE ssids SET status=1 WHERE bssid='"+mac+"' AND essid=' "+ssid+"';"
        
        #Connect to Database
        try:
            conn = mariadb.connect(
                    user="writer",
                    password="PW4Writer!",
                    host="127.0.0.1",
                    port=3306,
                    database="radio_mon"
            )
        except mariadb.Error as e:
            print(f"[x] Error while connecting: {e}")
        cursor = conn.cursor()
        # Update Status of Entry
        try:
            cursor.execute(query)
            conn.commit()
            conn.close()
        except mariadb.Error as e:
            print(f"[x] Error while executing update: {e}")

        return redirect(url_for("wifi"))
    else:
        for i in range(0,15):
            exec("global SSID%d; global ENC%d; global MAC%d; global ls%d; global vendor%d; SSID%d='';ENC%d=''; MAC%d='';ls%d='';vendor%d='';"% (i+1, i+1, i+1, i+1,i+1,i+1,i+1,i+1,i+1,i+1));
        try:
            conn = mariadb.connect(
                    user="reader",
                    password="PW4readonly",
                    host="127.0.0.1",
                    port=3306,
                    database="radio_mon"
            )
        except mariadb.Error as e:
            print(f"[x] Error while Connecting: {e}")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM ssids where status=2;")
            ssids = cursor.fetchall()
        except mariadb.Error as e:
            print(f"[x] Error while Reading Data: {e}")
        
        for i in range(0,len(ssids)):
                exec("""global SSID%d; SSID%d = ssids[%d][13].replace('" "', 'Versteckt').replace('"', '');""" % (i+1,i+1,i));
                exec("""global ENC%d; ENC%d = ssids[%d][5].replace('"', '');""" % (i+1,i+1,i)); 
                exec("""global MAC%d; MAC%d = ssids[%d][0].replace('"', '');""" % (i+1,i+1,i));
                exec("""global ls%d; ls%d = ssids[%d][2];""" % (i+1,i+1,i));
                exec("""global vendor%d; vendor%d = ssids[%d][14];"""% (i+1,i+1,i));
        conn.close()

        return render_template("wifi.html",button='Bekannt', SSID1=SSID1, SSID2=SSID2, SSID3=SSID3, SSID4=SSID4, SSID5=SSID5, SSID6=SSID6, SSID7=SSID7, SSID8=SSID8, SSID9=SSID9, SSID10=SSID10, SSID11=SSID11, SSID12=SSID12, SSID13=SSID13, SSID14=SSID14, SSID15=SSID15, Encryption1=ENC1, Encryption2=ENC2, Encryption3=ENC3, Encryption4=ENC4, Encryption5=ENC5, Encryption6=ENC6, Encryption7=ENC7, Encryption8=ENC8, Encryption9=ENC9, Encryption10=ENC10, Encryption11=ENC11, Encryption12=ENC12, Encryption13=ENC13, Encryption14=ENC14, Encryption15=ENC15, MAC1=MAC1, MAC2=MAC2, MAC3=MAC3, MAC4=MAC4, MAC5=MAC5, MAC6=MAC6, MAC7=MAC7,MAC8=MAC8,MAC9=MAC9,MAC10=MAC10,MAC11=MAC11,MAC12=MAC12,MAC13=MAC13,MAC14=MAC14,MAC15=MAC15,ls1=ls1,ls2=ls2,ls3=ls3,ls4=ls4,ls5=ls5,ls6=ls6,ls7=ls7,ls8=ls8,ls9=ls9,ls10=ls10,ls11=ls11,ls12=ls12,ls13=ls13,ls14=ls14,ls15=ls15, vendor1=vendor1, vendor2=vendor2, vendor3=vendor2,vendor4=vendor4,vendor5=vendor5,vendor6=vendor6,vendor7=vendor7,vendor8=vendor8,vendor9=vendor9,vendor10=vendor10,vendor11=vendor11,vendor12=vendor12,vendor13=vendor13,vendor14=vendor14,vendor15=vendor15)


@app.route("/wifi/unknown", methods=["POST", "GET"])
def unknownwifi():
    if request.method == "POST":
        accept = request.form["accept"] # returned mac from button
        if accept.split(',',1)[0]=="ignore": #If Button ignore
            mac = accept.split(',',1)[1].split(',',1)[0].strip()
            ssid = accept.split(',',1)[1].split(',',1)[1].strip()
            query="UPDATE ssids SET status=2 WHERE bssid='"+mac+"' AND essid=' "+ssid+"';"
        elif accept.split(',',1)[0]=="accept": #If Button Bekannt
            mac = accept.split(',',1)[1].split(',',1)[0].strip()
            ssid = accept.split(',',1)[1].split(',',1)[1].strip()
            query="UPDATE ssids SET status=1 WHERE bssid='"+mac+"' AND essid=' "+ssid+"';"
        
        #Connect to Database
        try:
            conn = mariadb.connect(
                    user="writer",
                    password="PW4Writer!",
                    host="127.0.0.1",
                    port=3306,
                    database="radio_mon"
            )
        except mariadb.Error as e:
            print(f"[x] Error while connecting: {e}")
        cursor = conn.cursor()
        # Update Status of Entry
        try:
            cursor.execute(query)
            conn.commit()
            conn.close()
        except mariadb.Error as e:
            print(f"[x] Error while executing update: {e}")

        return redirect(url_for("unknownwifi"))
    else:
        for i in range(0,15):
            exec("global SSID%d; global ENC%d; global MAC%d; global ls%d; global vendor%d; SSID%d='';ENC%d=''; MAC%d='';ls%d='';vendor%d='';"% (i+1, i+1, i+1, i+1,i+1,i+1,i+1,i+1,i+1,i+1));
        try:
            conn = mariadb.connect(
                    user="reader",
                    password="PW4readonly",
                    host="127.0.0.1",
                    port=3306,
                    database="radio_mon"
            )
        except mariadb.Error as e:
            print(f"[x] Error while Connecting: {e}")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM ssids where status IS NULL;")
            ssids = cursor.fetchall()
        except mariadb.Error as e:
            print(f"[x] Error while Reading Data: {e}")
        
        for i in range(0,len(ssids)):
                exec("""global SSID%d; SSID%d = ssids[%d][13].replace('" "', 'Versteckt').replace('"', '');""" % (i+1,i+1,i));
                exec("""global ENC%d; ENC%d = ssids[%d][5].replace('"', '');""" % (i+1,i+1,i)); 
                exec("""global MAC%d; MAC%d = ssids[%d][0].replace('"', '');""" % (i+1,i+1,i));
                exec("""global ls%d; ls%d = ssids[%d][2];""" % (i+1,i+1,i));
                exec("""global vendor%d; vendor%d = ssids[%d][14];"""% (i+1,i+1,i));
        conn.close()

        return render_template("wifi.html",button='Bekannt', SSID1=SSID1, SSID2=SSID2, SSID3=SSID3, SSID4=SSID4, SSID5=SSID5, SSID6=SSID6, SSID7=SSID7, SSID8=SSID8, SSID9=SSID9, SSID10=SSID10, SSID11=SSID11, SSID12=SSID12, SSID13=SSID13, SSID14=SSID14, SSID15=SSID15, Encryption1=ENC1, Encryption2=ENC2, Encryption3=ENC3, Encryption4=ENC4, Encryption5=ENC5, Encryption6=ENC6, Encryption7=ENC7, Encryption8=ENC8, Encryption9=ENC9, Encryption10=ENC10, Encryption11=ENC11, Encryption12=ENC12, Encryption13=ENC13, Encryption14=ENC14, Encryption15=ENC15, MAC1=MAC1, MAC2=MAC2, MAC3=MAC3, MAC4=MAC4, MAC5=MAC5, MAC6=MAC6, MAC7=MAC7,MAC8=MAC8,MAC9=MAC9,MAC10=MAC10,MAC11=MAC11,MAC12=MAC12,MAC13=MAC13,MAC14=MAC14,MAC15=MAC15,ls1=ls1,ls2=ls2,ls3=ls3,ls4=ls4,ls5=ls5,ls6=ls6,ls7=ls7,ls8=ls8,ls9=ls9,ls10=ls10,ls11=ls11,ls12=ls12,ls13=ls13,ls14=ls14,ls15=ls15, vendor1=vendor1, vendor2=vendor2, vendor3=vendor2,vendor4=vendor4,vendor5=vendor5,vendor6=vendor6,vendor7=vendor7,vendor8=vendor8,vendor9=vendor9,vendor10=vendor10,vendor11=vendor11,vendor12=vendor12,vendor13=vendor13,vendor14=vendor14,vendor15=vendor15)

@app.route("/wifi/known", methods=["POST", "GET"])
def knownwifi():
    if request.method == "POST":
        accept = request.form["accept"] # returned mac from button
        if accept.split(',',1)[0]=="ignore": #If Button ignore
            mac = accept.split(',',1)[1].split(',',1)[0].strip()
            ssid = accept.split(',',1)[1].split(',',1)[1].strip()
            query="UPDATE ssids SET status=2 WHERE bssid='"+mac+"' AND essid=' "+ssid+"';"
        elif accept.split(',',1)[0]=="accept": #If Button Bekannt
            mac = accept.split(',',1)[1].split(',',1)[0].strip()
            ssid = accept.split(',',1)[1].split(',',1)[1].strip()
            query="UPDATE ssids SET status=1 WHERE bssid='"+mac+"' AND essid=' "+ssid+"';"
        
        #Connect to Database
        try:
            conn = mariadb.connect(
                    user="writer",
                    password="PW4Writer!",
                    host="127.0.0.1",
                    port=3306,
                    database="radio_mon"
            )
        except mariadb.Error as e:
            print(f"[x] Error while connecting: {e}")
        cursor = conn.cursor()
        # Update Status of Entry
        try:
            cursor.execute(query)
            conn.commit()
            conn.close()
        except mariadb.Error as e:
            print(f"[x] Error while executing update: {e}")

        return redirect(url_for("knownwifi"))
    else:
        for i in range(0,15):
            exec("global SSID%d; global ENC%d; global MAC%d; global ls%d; global vendor%d; SSID%d='';ENC%d=''; MAC%d='';ls%d='';vendor%d='';"% (i+1, i+1, i+1, i+1,i+1,i+1,i+1,i+1,i+1,i+1));
        try:
            conn = mariadb.connect(
                    user="reader",
                    password="PW4readonly",
                    host="127.0.0.1",
                    port=3306,
                    database="radio_mon"
            )
        except mariadb.Error as e:
            print(f"[x] Error while Connecting: {e}")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM ssids where status=1;")
            ssids = cursor.fetchall()
        except mariadb.Error as e:
            print(f"[x] Error while Reading Data: {e}")
        
        for i in range(0,len(ssids)):
                exec("""global SSID%d; SSID%d = ssids[%d][13].replace('" "', 'Versteckt').replace('"', '');""" % (i+1,i+1,i));
                exec("""global ENC%d; ENC%d = ssids[%d][5].replace('"', '');""" % (i+1,i+1,i)); 
                exec("""global MAC%d; MAC%d = ssids[%d][0].replace('"', '');""" % (i+1,i+1,i));
                exec("""global ls%d; ls%d = ssids[%d][2];""" % (i+1,i+1,i));
                exec("""global vendor%d; vendor%d = ssids[%d][14];"""% (i+1,i+1,i));
        conn.close()

        return render_template("wifi.html",button="unbekannt", SSID1=SSID1, SSID2=SSID2, SSID3=SSID3, SSID4=SSID4, SSID5=SSID5, SSID6=SSID6, SSID7=SSID7, SSID8=SSID8, SSID9=SSID9, SSID10=SSID10, SSID11=SSID11, SSID12=SSID12, SSID13=SSID13, SSID14=SSID14, SSID15=SSID15, Encryption1=ENC1, Encryption2=ENC2, Encryption3=ENC3, Encryption4=ENC4, Encryption5=ENC5, Encryption6=ENC6, Encryption7=ENC7, Encryption8=ENC8, Encryption9=ENC9, Encryption10=ENC10, Encryption11=ENC11, Encryption12=ENC12, Encryption13=ENC13, Encryption14=ENC14, Encryption15=ENC15, MAC1=MAC1, MAC2=MAC2, MAC3=MAC3, MAC4=MAC4, MAC5=MAC5, MAC6=MAC6, MAC7=MAC7,MAC8=MAC8,MAC9=MAC9,MAC10=MAC10,MAC11=MAC11,MAC12=MAC12,MAC13=MAC13,MAC14=MAC14,MAC15=MAC15,ls1=ls1,ls2=ls2,ls3=ls3,ls4=ls4,ls5=ls5,ls6=ls6,ls7=ls7,ls8=ls8,ls9=ls9,ls10=ls10,ls11=ls11,ls12=ls12,ls13=ls13,ls14=ls14,ls15=ls15, vendor1=vendor1, vendor2=vendor2, vendor3=vendor2,vendor4=vendor4,vendor5=vendor5,vendor6=vendor6,vendor7=vendor7,vendor8=vendor8,vendor9=vendor9,vendor10=vendor10,vendor11=vendor11,vendor12=vendor12,vendor13=vendor13,vendor14=vendor14,vendor15=vendor15)

@app.route("/ble", methods=["POST", "GET"])
def ble():
    if request.method == "POST":
        accept = request.form["accept"] # returned mac from button
        if accept.split(',',1)[0]=="ignore": #If Button ignore
            query="UPDATE ble SET status=2 WHERE mac='"+accept.split(',',1)[1]+"';"
        elif accept.split(',',1)[0]=="accept": #If Button Bekannt
            query="UPDATE ble SET status=1 WHERE mac='"+accept.split(',',1)[1]+"';"
        
        #Connect to Database
        try:
            conn = mariadb.connect(
                    user="writer",
                    password="PW4Writer!",
                    host="127.0.0.1",
                    port=3306,
                    database="radio_mon"
            )
        except mariadb.Error as e:
            print(f"[x] Error while connecting: {e}")
        cursor = conn.cursor()
        # Update Status of Entry
        try:
            cursor.execute(query)
            conn.commit()
            conn.close()
        except mariadb.Error as e:
            print(f"[x] Error while executing update: {e}")

        return redirect(url_for("ble")) # Redirect to BLE Site
    else:
        for i in range(0,15):
            exec("global Name%d; global MAC%d; global connect%d; global vendor%d; global ls%d; Name%d='';MAC%d=''; connect%d=''; vendor%d=''; ls%d='';"% (i+1,i+1,i+1, i+1, i+1, i+1,i+1,i+1,i+1,i+1));
        try:
            conn = mariadb.connect(
                    user="reader",
                    password="PW4readonly",
                    host="127.0.0.1",
                    port=3306,
                    database="radio_mon"
            )
        except mariadb.Error as e:
            print(f"[x] Error while Connecting: {e}")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * from ble;")
            BLEdata = cursor.fetchall()
        except mariadb.error as e:
            print(f"[x] Error while Reading Data: {e}")

        for i in range(0,len(BLEdata)):
            exec("""global Name%d; Name%d = BLEdata[%d][0].replace('"', '');""" % (i+1,i+1,i)); 
            exec("""global MAC%d; MAC%d = BLEdata[%d][1].replace('"', '');""" % (i+1,i+1,i)); 
            exec("""global vendor%d; vendor%d = BLEdata[%d][3].replace('"', '');""" % (i+1,i+1,i)); 
            exec("""global connect%d; connect%d = BLEdata[%d][2].replace('"', '').replace('True', 'Ja').replace('False','Nein');""" % (i+1,i+1,i)); 
            exec("""global ls%d; ls%d = BLEdata[%d][4];"""% (i+1,i+1,i));
        return render_template("ble.html",button='Bekannt', Name1=Name1, Name2=Name2, Name3=Name3, Name4=Name4, Name5=Name5, Name6=Name6, Name7= Name7, Name8=Name8,Name9=Name9,Name10=Name10,Name11=Name11,Name12=Name12,Name13=Name13,Name14=Name14,Name15=Name15, MAC1=MAC1, MAC2=MAC2, MAC3=MAC3, MAC4=MAC4, MAC5=MAC5, MAC6=MAC6, MAC7=MAC7,MAC8=MAC8,MAC9=MAC9,MAC10=MAC10,MAC11=MAC11,MAC12=MAC12,MAC13=MAC13,MAC14=MAC14,MAC15=MAC15, connect1=connect1, connect2=connect2, connect3=connect3, connect4=connect4, connect5=connect5, connect6=connect6, connect7=connect7,connect8=connect8,connect9=connect9,connect10=connect10,connect11=connect11,connect12=connect12,connect13=connect13,connect14=connect14,connect15=connect15, vendor1=vendor1, vendor2=vendor2, vendor3=vendor3, vendor4=vendor4, vendor5=vendor5, vendor6=vendor6, vendor7=vendor7,vendor8=vendor8,vendor9=vendor9,vendor10=vendor10,vendor11=vendor11,vendor12=vendor12,vendor13=vendor13,vendor14=vendor14,vendor15=vendor15, ls1=ls1,ls2=ls2,ls3=ls3,ls4=ls4,ls5=ls5,ls6=ls6,ls7=ls7,ls8=ls8,ls9=ls9,ls10=ls10,ls11=ls11,ls12=ls12,ls13=ls13,ls14=ls14,ls15=ls15)


@app.route("/ble/ignored", methods=["POST", "GET"])
def ignoredble():
    if request.method == "POST":
        accept = request.form["accept"] # returned mac from button
        if accept.split(',',1)[0]=="ignore": #If Button ignore
            query="UPDATE ble SET status=NULL WHERE mac='"+accept.split(',',1)[1]+"';"
        elif accept.split(',',1)[0]=="accept": #If Button Bekannt
            query="UPDATE ble SET status=1 WHERE mac='"+accept.split(',',1)[1]+"';"
        
        #Connect to Database
        try:
            conn = mariadb.connect(
                    user="writer",
                    password="PW4Writer!",
                    host="127.0.0.1",
                    port=3306,
                    database="radio_mon"
            )
        except mariadb.Error as e:
            print(f"[x] Error while connecting: {e}")
        cursor = conn.cursor()
        # Update Status of Entry
        try:
            cursor.execute(query)
            conn.commit()
            conn.close()
        except mariadb.Error as e:
            print(f"[x] Error while executing update: {e}")

        return redirect(url_for("ignoredble")) # Redirect to BLE Site
    else:
        for i in range(0,15):
            exec("global Name%d; global MAC%d; global connect%d; global vendor%d; global ls%d; Name%d='';MAC%d=''; connect%d=''; vendor%d=''; ls%d='';"% (i+1,i+1,i+1, i+1, i+1, i+1,i+1,i+1,i+1,i+1));
        try:
            conn = mariadb.connect(
                    user="reader",
                    password="PW4readonly",
                    host="127.0.0.1",
                    port=3306,
                    database="radio_mon"
            )
        except mariadb.Error as e:
            print(f"[x] Error while Connecting: {e}")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * from ble where status=2;")
            BLEdata = cursor.fetchall()
        except mariadb.error as e:
            print(f"[x] Error while Reading Data: {e}")

        for i in range(0,len(BLEdata)):
            exec("""global Name%d; Name%d = BLEdata[%d][0].replace('"', '');""" % (i+1,i+1,i)); 
            exec("""global MAC%d; MAC%d = BLEdata[%d][1].replace('"', '');""" % (i+1,i+1,i)); 
            exec("""global vendor%d; vendor%d = BLEdata[%d][3].replace('"', '');""" % (i+1,i+1,i)); 
            exec("""global connect%d; connect%d = BLEdata[%d][2].replace('"', '').replace('True', 'Ja').replace('False','Nein');""" % (i+1,i+1,i)); 
            exec("""global ls%d; ls%d = BLEdata[%d][4];"""% (i+1,i+1,i));
        return render_template("ble.html",button='Bekannt', Name1=Name1, Name2=Name2, Name3=Name3, Name4=Name4, Name5=Name5, Name6=Name6, Name7= Name7, Name8=Name8,Name9=Name9,Name10=Name10,Name11=Name11,Name12=Name12,Name13=Name13,Name14=Name14,Name15=Name15, MAC1=MAC1, MAC2=MAC2, MAC3=MAC3, MAC4=MAC4, MAC5=MAC5, MAC6=MAC6, MAC7=MAC7,MAC8=MAC8,MAC9=MAC9,MAC10=MAC10,MAC11=MAC11,MAC12=MAC12,MAC13=MAC13,MAC14=MAC14,MAC15=MAC15, connect1=connect1, connect2=connect2, connect3=connect3, connect4=connect4, connect5=connect5, connect6=connect6, connect7=connect7,connect8=connect8,connect9=connect9,connect10=connect10,connect11=connect11,connect12=connect12,connect13=connect13,connect14=connect14,connect15=connect15, vendor1=vendor1, vendor2=vendor2, vendor3=vendor3, vendor4=vendor4, vendor5=vendor5, vendor6=vendor6, vendor7=vendor7,vendor8=vendor8,vendor9=vendor9,vendor10=vendor10,vendor11=vendor11,vendor12=vendor12,vendor13=vendor13,vendor14=vendor14,vendor15=vendor15, ls1=ls1,ls2=ls2,ls3=ls3,ls4=ls4,ls5=ls5,ls6=ls6,ls7=ls7,ls8=ls8,ls9=ls9,ls10=ls10,ls11=ls11,ls12=ls12,ls13=ls13,ls14=ls14,ls15=ls15)


@app.route("/ble/known", methods=["POST", "GET"])
def knownble():
    if request.method == "POST":
        accept = request.form["accept"] # returned mac from button
        if accept.split(',',1)[0]=="ignore": #If Button ignore
            query="UPDATE ble SET status=2 WHERE mac='"+accept.split(',',1)[1]+"';"
        elif accept.split(',',1)[0]=="accept": #If Button Bekannt
            query="UPDATE ble SET status=1 WHERE mac='"+accept.split(',',1)[1]+"';"
        
        #Connect to Database
        try:
            conn = mariadb.connect(
                    user="writer",
                    password="PW4Writer!",
                    host="127.0.0.1",
                    port=3306,
                    database="radio_mon"
            )
        except mariadb.Error as e:
            print(f"[x] Error while connecting: {e}")
        cursor = conn.cursor()
        # Update Status of Entry
        try:
            cursor.execute(query)
            conn.commit()
            conn.close()
        except mariadb.Error as e:
            print(f"[x] Error while executing update: {e}")
        return redirect(url_for("knownble")) # Redirect to BLE Site
    else:
        for i in range(0,15):
            exec("global Name%d; global MAC%d; global connect%d; global vendor%d; global ls%d; Name%d='';MAC%d=''; connect%d=''; vendor%d=''; ls%d='';"% (i+1,i+1,i+1, i+1, i+1, i+1,i+1,i+1,i+1,i+1));
        try:
            conn = mariadb.connect(
                    user="reader",
                    password="PW4readonly",
                    host="127.0.0.1",
                    port=3306,
                    database="radio_mon"
            )
        except mariadb.Error as e:
            print(f"[x] Error while Connecting: {e}")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * from ble where status=1;")
            BLEdata = cursor.fetchall()
        except mariadb.Error as e:
            print(f"[x] Error while Reading Data: {e}")

        for i in range(0,len(BLEdata)):
            exec("""global Name%d; Name%d = BLEdata[%d][0].replace('"', '');""" % (i+1,i+1,i)); 
            exec("""global MAC%d; MAC%d = BLEdata[%d][1].replace('"', '');""" % (i+1,i+1,i)); 
            exec("""global vendor%d; vendor%d = BLEdata[%d][3].replace('"', '');""" % (i+1,i+1,i)); 
            exec("""global connect%d; connect%d = BLEdata[%d][2].replace('"', '').replace('True', 'Ja').replace('False','Nein');""" % (i+1,i+1,i)); 
            exec("""global ls%d; ls%d = BLEdata[%d][4];"""% (i+1,i+1,i));
        return render_template("ble.html",button='Unbekannt', Name1=Name1, Name2=Name2, Name3=Name3, Name4=Name4, Name5=Name5, Name6=Name6, Name7= Name7, Name8=Name8,Name9=Name9,Name10=Name10,Name11=Name11,Name12=Name12,Name13=Name13,Name14=Name14,Name15=Name15, MAC1=MAC1, MAC2=MAC2, MAC3=MAC3, MAC4=MAC4, MAC5=MAC5, MAC6=MAC6, MAC7=MAC7,MAC8=MAC8,MAC9=MAC9,MAC10=MAC10,MAC11=MAC11,MAC12=MAC12,MAC13=MAC13,MAC14=MAC14,MAC15=MAC15, connect1=connect1, connect2=connect2, connect3=connect3, connect4=connect4, connect5=connect5, connect6=connect6, connect7=connect7,connect8=connect8,connect9=connect9,connect10=connect10,connect11=connect11,connect12=connect12,connect13=connect13,connect14=connect14,connect15=connect15, vendor1=vendor1, vendor2=vendor2, vendor3=vendor3, vendor4=vendor4, vendor5=vendor5, vendor6=vendor6, vendor7=vendor7,vendor8=vendor8,vendor9=vendor9,vendor10=vendor10,vendor11=vendor11,vendor12=vendor12,vendor13=vendor13,vendor14=vendor14,vendor15=vendor15, ls1=ls1,ls2=ls2,ls3=ls3,ls4=ls4,ls5=ls5,ls6=ls6,ls7=ls7,ls8=ls8,ls9=ls9,ls10=ls10,ls11=ls11,ls12=ls12,ls13=ls13,ls14=ls14,ls15=ls15)
    

@app.route("/ble/unknown", methods=["POST", "GET"])
def unknownble():

    if request.method == "POST":
        accept = request.form["accept"] # returned mac from button
        if accept.split(',',1)[0]=="ignore": #If Button ignore
            query="UPDATE ble SET status=2 WHERE mac='"+accept.split(',',1)[1]+"';"
        elif accept.split(',',1)[0]=="accept": #If Button Bekannt
            query="UPDATE ble SET status=1 WHERE mac='"+accept.split(',',1)[1]+"';"
        
        #Connect to Database
        try:
            conn = mariadb.connect(
                    user="writer",
                    password="PW4Writer!",
                    host="127.0.0.1",
                    port=3306,
                    database="radio_mon"
            )
        except mariadb.Error as e:
            print(f"[x] Error while connecting: {e}")
        cursor = conn.cursor()
        # Update Status of Entry
        try:
            cursor.execute(query)
            conn.commit()
            conn.close()
        except mariadb.Error as e:
            print(f"[x] Error while executing update: {e}")


        return redirect(url_for("unknownble")) # Redirect to BLE Site
    else:
        for i in range(0,15):
            exec("global Name%d; global MAC%d; global connect%d; global vendor%d; global ls%d; Name%d='';MAC%d=''; connect%d=''; vendor%d=''; ls%d='';"% (i+1,i+1,i+1, i+1, i+1, i+1,i+1,i+1,i+1,i+1));
        try:
            conn = mariadb.connect(
                    user="reader",
                    password="PW4readonly",
                    host="127.0.0.1",
                    port=3306,
                    database="radio_mon"
            )
        except mariadb.Error as e:
            print(f"[x] Error while Connecting: {e}")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * from ble where status IS NULL;")
            BLEdata = cursor.fetchall()
        except mariadb.Error as e:
            print(f"[x] Error while Reading Data: {e}")


        for i in range(0,len(BLEdata)):
            exec("""global Name%d; Name%d = BLEdata[%d][0].replace('"', '');""" % (i+1,i+1,i)); 
            exec("""global MAC%d; MAC%d = BLEdata[%d][1].replace('"', '');""" % (i+1,i+1,i)); 
            exec("""global vendor%d; vendor%d = BLEdata[%d][3].replace('"', '');""" % (i+1,i+1,i)); 
            exec("""global connect%d; connect%d = BLEdata[%d][2].replace('"', '').replace('True', 'Ja').replace('False','Nein');""" % (i+1,i+1,i)); 
            exec("""global ls%d; ls%d = BLEdata[%d][4];"""% (i+1,i+1,i));
            print(MAC1)
        return render_template("ble.html",button='Bekannt', Name1=Name1, Name2=Name2, Name3=Name3, Name4=Name4, Name5=Name5, Name6=Name6, Name7= Name7, Name8=Name8,Name9=Name9,Name10=Name10,Name11=Name11,Name12=Name12,Name13=Name13,Name14=Name14,Name15=Name15, MAC1=MAC1, MAC2=MAC2, MAC3=MAC3, MAC4=MAC4, MAC5=MAC5, MAC6=MAC6, MAC7=MAC7,MAC8=MAC8,MAC9=MAC9,MAC10=MAC10,MAC11=MAC11,MAC12=MAC12,MAC13=MAC13,MAC14=MAC14,MAC15=MAC15, connect1=connect1, connect2=connect2, connect3=connect3, connect4=connect4, connect5=connect5, connect6=connect6, connect7=connect7,connect8=connect8,connect9=connect9,connect10=connect10,connect11=connect11,connect12=connect12,connect13=connect13,connect14=connect14,connect15=connect15, vendor1=vendor1, vendor2=vendor2, vendor3=vendor3, vendor4=vendor4, vendor5=vendor5, vendor6=vendor6, vendor7=vendor7,vendor8=vendor8,vendor9=vendor9,vendor10=vendor10,vendor11=vendor11,vendor12=vendor12,vendor13=vendor13,vendor14=vendor14,vendor15=vendor15, ls1=ls1,ls2=ls2,ls3=ls3,ls4=ls4,ls5=ls5,ls6=ls6,ls7=ls7,ls8=ls8,ls9=ls9,ls10=ls10,ls11=ls11,ls12=ls12,ls13=ls13,ls14=ls14,ls15=ls15)
    


@app.route("/zigbee", methods=["POST", "GET"])
def zigbee():

    if request.method == "POST":
        accept = request.form["accept"] # returned mac from button
        if accept.split(',',1)[0]=="ignore": #If Button ignore
            query="UPDATE ble SET status=2 WHERE mac='"+accept.split(',',1)[1]+"';"
        elif accept.split(',',1)[0]=="accept": #If Button Bekannt
            query="UPDATE ble SET status=1 WHERE mac='"+accept.split(',',1)[1]+"';"
        
        #Connect to Database
        try:
            conn = mariadb.connect(
                    user="writer",
                    password="PW4Writer!",
                    host="127.0.0.1",
                    port=3306,
                    database="radio_mon"
            )
        except mariadb.Error as e:
            print(f"[x] Error while connecting: {e}")
        cursor = conn.cursor()
        # Update Status of Entry
        try:
            cursor.execute(query)
            conn.commit()
            conn.close()
        except mariadb.Error as e:
            print(f"[x] Error while executing update: {e}")


        return redirect(url_for("unknownble")) # Redirect to BLE Site
    else:
        for i in range(0,15):
            exec("global Name%d; global MAC%d; global connect%d; global vendor%d; global ls%d; Name%d='';MAC%d=''; connect%d=''; vendor%d=''; ls%d='';"% (i+1,i+1,i+1, i+1, i+1, i+1,i+1,i+1,i+1,i+1));
        try:
            conn = mariadb.connect(
                    user="reader",
                    password="PW4readonly",
                    host="127.0.0.1",
                    port=3306,
                    database="radio_mon"
            )
        except mariadb.Error as e:
            print(f"[x] Error while Connecting: {e}")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * from ble where status IS NULL;")
            BLEdata = cursor.fetchall()
        except mariadb.Error as e:
            print(f"[x] Error while Reading Data: {e}")


        for i in range(0,len(BLEdata)):
            exec("""global Name%d; Name%d = BLEdata[%d][0].replace('"', '');""" % (i+1,i+1,i)); 
            exec("""global MAC%d; MAC%d = BLEdata[%d][1].replace('"', '');""" % (i+1,i+1,i)); 
            exec("""global vendor%d; vendor%d = BLEdata[%d][3].replace('"', '');""" % (i+1,i+1,i)); 
            exec("""global connect%d; connect%d = BLEdata[%d][2].replace('"', '').replace('True', 'Ja').replace('False','Nein');""" % (i+1,i+1,i)); 
            exec("""global ls%d; ls%d = BLEdata[%d][4];"""% (i+1,i+1,i));
            print(MAC1)
        return render_template("zigbee.html")

@app.errorhandler(404)
def default(error):
       return redirect(url_for("home"))


if __name__ == "__main__":
        app.run(debug=True)

