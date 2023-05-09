import json
from sqlalchemy import JSON, create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Base, Country

from flask import Flask, render_template, request

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

@app.route("/addCountryToDatabase", methods = ["POST"])
def addCountryToDatabase():
    print("inside addCountryToDatabase...")
    json_data = request.get_json()
    addCountry(json_data)
    return "ok"

def addCountry(json_data):
    name_obj = json_data["name"]
    tld_array = parseArrayData("tld", json_data)
    cca2 = json_data["cca2"]
    ccn3 = parseSingleData("ccn3", json_data)
    cca3 = json_data["cca3"]
    cioc = parseSingleData("cioc", json_data)
    independent = parseBooleanData("independent", json_data)
    status = json_data["status"]
    unMember = json_data["unMember"]
    currencies_obj = parseObjectData("currencies", json_data)
    idd_obj = json_data["idd"]
    capital_array = parseArrayData("capital", json_data)
    altSpellings_array = json_data["altSpellings"]
    region = json_data["region"]
    subregion = parseSingleData("subregion", json_data)
    languages_obj = parseObjectData("languages", json_data)
    latlng_array = json_data["latlng"]
    landlocked = json_data["landlocked"]
    borders_array = parseArrayData("borders", json_data)
    area = json_data["area"]
    flag = json_data["flag"]
    maps_obj = json_data["maps"]
    population = json_data["population"]
    
    gini_obj = parseObjectData("gini", json_data)
    fifa = parseSingleData("fifa", json_data)

    car_obj = json_data["car"]
    timezones_array = json_data["timezones"]
    continents_array = json_data["continents"]
    flags_obj = json_data["flags"]
    coatOfArms_obj = { "NA": "NA" }
    startOfWeek = json_data["startOfWeek"]
    capitalInfo_obj = json_data["capitalInfo"]
    postalCode_obj = parseObjectData("postalCode", json_data)

    country = Country(json.dumps(name_obj), ",".join(tld_array), cca2, ccn3, cca3, cioc, independent, 
            status, unMember, json.dumps(currencies_obj), json.dumps(idd_obj), ",".join(capital_array), 
            ",".join(altSpellings_array), region, subregion, json.dumps(languages_obj), 
            ",".join(str(i) for i in latlng_array), landlocked, ",".join(borders_array), area, flag, 
            json.dumps(maps_obj), population, json.dumps(gini_obj), fifa, json.dumps(car_obj), 
            ",".join(timezones_array), ",".join(continents_array), json.dumps(flags_obj), 
            json.dumps(coatOfArms_obj), startOfWeek, json.dumps(capitalInfo_obj), json.dumps(postalCode_obj))
    session.add(country)
    session.commit()

def parseObjectData(keyword, json_data): 
    if keyword in json_data:
        value = json_data[keyword]
        if len(value) == 0:
            value = {"NA" : "NA"}
    else:
        value = {"NA" : "NA"}
    return value

def parseArrayData(keyword, json_data): 
    if keyword in json_data:
        value = json_data[keyword]
        if not value:
            value = ["NA"]
    else:
        value = ["NA"]
    return value

def parseSingleData(keyword, json_data): 
    if keyword in json_data:
        value = json_data[keyword]
    else:
        value = "NA"
    return value

def parseBooleanData(keyword, json_data): 
    if keyword in json_data:
        value = json_data[keyword]
    else:
        value = False
    return value

if __name__ == "__main__":
    app.run()







# print("banana")
# results = session.query(Country).all()
# for r in results:
#     print(r)
# print("end")


# results = session.query(Person).filter(Person.lastName == "Grown")
# for r in results:
#     print(r)



# print("banana")
# myJson = json.dumps(name_obj)
# print(myJson)
 
# test1 = Test(myJson)
# print(test1)
# session.add(test1)
# session.commit()

# results = session.query(Test).all()
# json_object = results[0].toJson()
# print("testing...")
# print(json_object)
# keys = json_object.keys()
# for key in keys: 
#     print(key, json_object[key]["common"])