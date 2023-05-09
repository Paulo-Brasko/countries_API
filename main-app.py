import json
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Base, Country

from flask import Flask, render_template

app = Flask(__name__)

engine = create_engine("sqlite:///countries.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session=Session()

@app.route("/")
def index():
    return render_template("main-page.html")

@app.route("/countries")
def getListOfCountries():
    countries = session.query(Country).all()
    listOfCountries = []
    for country in countries:
        json_data = json.loads(country.name)
        listOfCountries.append(json_data["common"])
    listOfCountries.sort()
    return listOfCountries;

@app.route("/country/<name>/")
def getCountryByName(name):
    countries = session.query(Country).all()
    for country in countries:
        json_data = json.loads(country.name)
        country_name = json_data["common"]
        if (country_name.lower() == name.lower()):
            return country.toJson()
    return "country not found"

if __name__ == "__main__":
    app.run()
