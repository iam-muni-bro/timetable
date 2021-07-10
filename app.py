from flask import Flask, render_template, request
import gspread

gc= gspread.service_account(filename="timetable.json")

#opening file
sh = gc.open('TimeTable')
# Accessing the data
timeTable = sh.get_worksheet(0)

app = Flask(__name__)


@app.route("/")
def home():
    dateAndTime = (timeTable.acell("A1").value).split(',')
    day = {
        'm' : (timeTable.acell("A2").value).split(','),
        't' : (timeTable.acell("A3").value).split(','),
        'w' : (timeTable.acell("A4").value).split(','),
        'th' : (timeTable.acell("A5").value).split(','),
        'f' : (timeTable.acell("A6").value).split(','),
        's' : (timeTable.acell("A7").value).split(',')
        }
    return render_template("index.html",day = day , dateAndTime=dateAndTime)
