#dependencies 
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt

from flask import Flask, jsonify

import datetime as dt
import pandas as pd

#setting yup the DB
engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

#references to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

#flask begins
#flask begins
#flask begins
#flask begins
app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"/api/v1.0/precipitation---"
        f"/api/v1.0/stations---"
        f"/api/v1.0/tobs---"
        f"/api/v1.0/<start>---"
        f"/api/v1.0/<start>/<end>"
    )

#1'st directory
@app.route("/api/v1.0/precipitation")
def directory_1():

    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).all()

    date_prcp = []
    for date, precipitation in results:
        dict_1 = {}
        dict_1['date'] = date
        dict_1['prcp'] = precipitation
        date_prcp.append(dict_1)

    return jsonify(date_prcp)

# 2'nd directory
@app.route('/api/v1.0/stations')
def directory_2():
#Return a JSON list of stations from the dataset.'''

    session = Session(engine)
    results = session.query(Station.station).all()
    return jsonify(results)


# 3rd directory
@app.route("/api/v1.0/tobs")
def directory_3():

    session = Session(engine)
    column_choice = [Measurement.date, Measurement.prcp]
    precipitation_data = session.query(*column_choice).\
        filter(func.strftime('%Y', Measurement.date) == '2015')
    df_precip = pd.DataFrame(precipitation_data)
    last_date = list(df_precip['date'])[-1]

    time_one_year_ago = dt.datetime.strptime(last_date, '%Y-%m-%d') - dt.timedelta(365)

    return jsonify(time_one_year_ago)

@app.route("/api/v1.0/")
def directory_4():

    session = Session(engine)
    session_query_2 = session.query(Measurement.station, Measurement.id, Measurement.tobs).all()
    df_2 = pd.DataFrame(session_query_2)
    max_value = df_2['tobs'].max()
    min_value = df_2['tobs'].min()
    avg_output = df_2.groupby('station')['tobs'].mean()
    avg_most_active = avg_output.loc[['USC00519281']]
   

    #PRINTED STRANGE, but all the information is here. 
    return f'{max_value} {min_value} {avg_most_active}'



if __name__ == '__main__':
    app.run(debug=True)


