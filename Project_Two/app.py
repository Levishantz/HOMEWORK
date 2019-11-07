# Dependencies

import pandas as pd
import datetime as dt
from flask import Flask, jsonify
import matplotlib.pyplot as plt
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine, func


from matplotlib import style
style.use('fivethirtyeight')


# setting up the DB
# need to refernce table

engine = create_engine(
    "postgresql://levi:levi@localhost:5432/Finance_project_2")
# print("Engine initialized")
# Base = automap_base()
# print("Automapped")
# Base.prepare(engine, reflect=True)
# print("Base is prepared")
# balance_sheet = Base.classes.get(balance_sheet)
# print("Balance sheet initialized")

# s = Session(engine)
# s.query(balance_sheet).all()


# reflect the tables
# Base.prepare(engine, reflect=True)


# Reference the tables

# place tables here place tables here place tables here
# place tables here place tables here place tables here

# flask begins
# flask begins
# flask begins
# flask begins

app = Flask(__name__)


@app.route("/")
def welcome():
    """List all available api routes."""
    return "/api/v1.0/"

# first der.
@app.route("/api/v1.0/bs")
def balance():
    print("Session created")
    """display balance sheet"""
    results = pd.read_sql("select * from balance_sheet", engine)
    return jsonify(results.to_dict(orient="records"))

  
@app.route("/api/v1.0/is")
def income():
    print("Session created")
    """display income statement"""
    results_1 = pd.read_sql("select * from income_statement", engine)
    return jsonify(results_1.to_dict(orient="records"))


if __name__ == '__main__':
    app.run(debug=True)