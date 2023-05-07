import json
from sqlalchemy import JSON, create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Base, Person, Country, Test

engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session=Session()

# name_obj = { 
#     "name": {
#         "common" : "Brazil",
#         "official" : "Federative Republic of Brazil", 
#         "nativeName" : {
#             "por" : {
#                 "official" : "República Federativa do Brasil",
#                 "common" : "Brasil"
#             }
#         }
#     }
# }

# tld_array = [".br"]
# cca2 = "BR"
# ccn3 = "076"
# cca3 = "BRA"
# cioc = "BRA"
# independent = "true"
# status = "officially-assigned"
# unMember = "true"
# currencies_obj = {
#     "BRL": {
#         "name": "Brazilian real",
#         "symbol": "R$"
#     }
# }

# idd_obj = {
#     "root": "+5",
#     "suffixes": [
#         "5"
#     ]
# }

# capital = ["Brasilia"]
# altSpellings = ["BR", "Brasil", "Federative Republic of Brazil", "República Federativa do Brasil"]
# region = "Americas"
# subregion = "South America"
# languages_obj = { "por" : "Portuguese"}
# latlng_array = ["-10", "-55"]
# landlocked = "false"
# borders_array = ["ARG", "BOL", "COL", "GUF", "GUY", "PRY", "PER", "SUR", "URY", "VEN"]
# area = 8515767
# flag = "BR"
# maps_obj = {
#     "googleMaps": "https://goo.gl/maps/waCKk21HeeqFzkNC9",
#     "openStreetMaps": "https://www.openstreetmap.org/relation/59470"
# }
# population = 212559409
# gini_obj = { "2019": 53.4 }
# fifa = "BRA"
# car_obj = { 
#     "signs": [ "BR" ],
#     "side": "right"
# }
# timezones_array = ["UTC-05:00", "UTC-04:00", "UTC-03:00", "UTC-02:00"]
# continents_array = ["South America"]
# flags_obj = {
#     "png": "https://flagcdn.com/w320/br.png",
#     "svg": "https://flagcdn.com/br.svg",
#     "alt": "The flag of Brazil has a green field with a large yellow rhombus in the center. Within the rhombus is a dark blue globe with twenty-seven small five-pointed white stars depicting a starry sky and a thin white convex horizontal band inscribed with the national motto 'Ordem e Progresso' across its center."
# }
# coatOfArms_obj = {
#     "png": "https://mainfacts.com/media/images/coats_of_arms/br.png",
#     "svg": "https://mainfacts.com/media/images/coats_of_arms/br.svg"
# }
# startOfWeek = "monday"
# capitalInfo_obj = { "latlng": [-15.79, -47.88] }
# postalCode_obj = {
#     "format": "#####-###",
#     "regex": "^(\\d{8})$"
# }

# country01 = Country(json.dumps(name_obj), ",".join(tld_array), cca2, ccn3, cca3, cioc, independent, status, unMember, 
#         json.dumps(currencies_obj), json.dumps(idd_obj), ",".join(capital), ",".join(altSpellings), region, subregion,
#         json.dumps(languages_obj), ",".join(latlng_array),
#         landlocked, ",".join(borders_array), area, flag, json.dumps(maps_obj), population, json.dumps(gini_obj),
#         fifa, json.dumps(car_obj), ",".join(timezones_array),
#         ",".join(continents_array), json.dumps(flags_obj), json.dumps(coatOfArms_obj),
#         startOfWeek, json.dumps(capitalInfo_obj), json.dumps(postalCode_obj))
# session.add(country01)
# session.commit()

results = session.query(Country).all()
print(results)

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