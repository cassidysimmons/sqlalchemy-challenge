# Import the dependencies.

from flask import Flask
from flask import jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd
import datetime as dt


#################################################
# Database Setup
#################################################

# reflect an existing database into a new model
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect the tables
Base = automap_base()
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# ========================= home route ==================================
@app.route("/")
def home():
    print("server received request for 'home' page...")
    return (
        f"welcome to the hawaii stations api!<br/>"
        f"available routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )

# ====================== precipitation route ==============================
@app.route("/api/v1.0/precipitation")
def precipitation():
    # calculating the date one year from the last date
    date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    # query date and prcp within specified date range
    twelve_months = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= date).all()

    # close the session
    session.close()

    # loop to create dictionary /w query results...
    prcp_list = []
    for date, precipitation in twelve_months:
        prcp_dict = {}
        prcp_dict['date'] = date
        prcp_dict['prcp'] = precipitation
        prcp_list.append(prcp_dict)

    print("server received request for 'precipitation' page...")
    return jsonify(prcp_list)

# ================================ stations route =================================
@app.route("/api/v1.0/stations")
def stations():
    # query stations + convert to tuple (because json)
    station_names = session.query(Station.station).all()
    station_tup = [tuple(row) for row in station_names]

    # close the session
    session.close()

    # loop to create dictionary /w (tuple) query results... 
    station_list = []
    for station in station_tup:
        station_dict = {}
        station_dict['station'] = station
        station_list.append(station)

    print()
    return jsonify(station_list)

# ==================================== tobs route ===================================
@app.route("/api/v1.0/tobs")
def tobs():
    # redefine 'date' 
    date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # query date and temp observation only for the most avtive station
    year_of_tobs = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.date >= date).\
    where(Measurement.station == 'USC00519523').all()

    # close the session
    session.close()

    # loop to create dictionary /w query results... 
    tobs_list = []
    for date, tobs in year_of_tobs:
        tobs_dict = {}
        tobs_dict['date'] = date
        tobs_dict['tobs'] = tobs
        tobs_list.append(tobs_dict)

    print("server received request for 'tobs' page...")
    return jsonify(tobs_list)

# =================================== temp start date route ===============================
@app.route("/api/v1.0/<start>")
def start(start):

    date = session.query(Measurement.date).all()

    t_max = session.query(func.max(Measurement.tobs)).\
    filter(Measurement.date >= {start}).all()

    t_min = session.query(func.min(Measurement.tobs)).\
    filter(Measurement.date >= {start}).all()

    t_avg = session.query(func.round(func.avg(Measurement.tobs),1)).\
    filter(Measurement.date >= {start}).all()

    t_list = []
    for date, tobs in t_min, t_avg, t_max:
        t_dict = {}
        t_dict["date"] = date
        t_dict["tobs"] = tobs
        t_list.append(t_dict)


    canonicalized = start.replace(" ","").lower()
    for d in date:
        search_term = d["start"].replace(" ","").lower()

        if search_term ==  canonicalized:
            return jsonify(t_list)

    print("server received request for 'temp_start' page...")
    return jsonify({"error": f"date {start} not found in data set..."}), 404

# =================================== temp start + end date route =======================
@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    print("server received request for 'temp_start_end' page...")
    return

if __name__ == "__main__":
    app.run(debug=True)