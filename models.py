from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
import json

Base = declarative_base()

class Person(Base):
    __tablename__ = "people"

    ssn = Column("ssn", Integer, primary_key=True)
    firstName = Column("firstName", String)
    lastName = Column("lastName", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, ssn, first, last, gender, age):
        self.ssn = ssn
        self.firstName = first
        self.lastName = last
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"({self.ssn} {self.firstName} {self.lastName} {self.gender} {self.age})"

class Country(Base):
    __tablename__ = "countries"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    tld = Column("tld", String)
    cca2 = Column("cca2", String)
    ccn3 = Column("ccn3", String)
    cca3 = Column("cca3", String)
    cioc = Column("cioc", String)
    independent = Column("independent", String)
    status = Column("status", String)
    unMember = Column("unMember", String)
    currencies = Column("currencies", String)
    idd = Column("idd", String)
    capital = Column("capital", String)
    altSpellings = Column("altSpellings", String)
    region = Column("region", String)
    subregion = Column("subregion", String)
    languages = Column("languages", String)
    latlng = Column("latlng", String)
    landlocked = Column("landlocked", String)
    borders = Column("borders", String)
    area = Column("area", String)
    flag = Column("flag", String)
    maps = Column("translations", String)
    population = Column("population", String)
    gini = Column("gini", String)
    fifa = Column("fifa", String)
    car = Column("car", String)
    timezones = Column("timezones", String)
    continents = Column("continents", String)
    flags = Column("flags", String)
    coatOfArms = Column("coatOfArms", String)
    startOfWeek = Column("startOfWeek", String)
    capitalInfo = Column("capitalInfo", String)
    postalCode = Column("postalCode", String)

    def __init__(self, id, name, tld, cca2, ccn3, cca3, cioc, independent, status, unMember, 
        currencies, idd, capital, altSpellings, region, subregion, languages, latlng,
        landlocked, borders, area, flag, maps, population, gini, fifa, car, timezones,
        continents, flags, coatOfArms, startOfWeek, capitalInfo, postalCode):

        self.id = id
        self.name = name
        self.tld = tld
        self.cca2 = cca2
        self.ccn3 = ccn3
        self.cca3 = cca3
        self.cioc = cioc
        self.independent = independent
        self.status = status
        self.unMember = unMember
        self.currencies = currencies
        self.idd = idd
        self.capital = capital
        self.altSpellings = altSpellings 
        self.region = region
        self.subregion = subregion
        self.languages = languages
        self.latlng = latlng
        self.landlocked = landlocked
        self.borders = borders 
        self.area = area
        self.flag = flag
        self.maps = maps
        self.population = population
        self.gini = gini
        self.fifa = fifa
        self.car = car
        self.timezones = timezones
        self.continents = continents
        self.flags = flags
        self.coatOfArms = coatOfArms
        self.startOfWeek = startOfWeek
        self.capitalInfo = capitalInfo
        self.postalCode = postalCode

    def __repr__(self):
        return f"({self.name})"
    
class Test(Base):
    __tablename__ = "test"

    name = Column("name", String, primary_key=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"({self.name})"

    def toJson(self):
        return json.loads(self.name)
    
# {"name": {"common": "Brazil", "official": "Federative Republic of Brazil", "nativeName": {"por": {"official": "Rep\u00fablica Federativa do Brasil", "common": "Brasil"}}}}

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


