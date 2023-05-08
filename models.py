from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, Boolean
from sqlalchemy.ext.declarative import declarative_base
import json

Base = declarative_base()

class Country(Base):
    __tablename__ = "countries"

    name = Column("name", String, primary_key=True)
    tld = Column("tld", String)
    cca2 = Column("cca2", String)
    ccn3 = Column("ccn3", String)
    cca3 = Column("cca3", String)
    cioc = Column("cioc", String)
    independent = Column("independent", Boolean)
    status = Column("status", String)
    unMember = Column("unmember", Boolean)
    currencies = Column("currencies", String)
    idd = Column("idd", String)
    capital = Column("capital", String)
    altSpellings = Column("altspellings", String)
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
    coatOfArms = Column("coatofarms", String)
    startOfWeek = Column("startofweek", String)
    capitalInfo = Column("capitalinfo", String)
    postalCode = Column("postalcode", String)

    def __init__(self, name, tld, cca2, ccn3, cca3, cioc, independent, status, unMember, 
        currencies, idd, capital, altSpellings, region, subregion, languages, latlng,
        landlocked, borders, area, flag, maps, population, gini, fifa, car, timezones,
        continents, flags, coatOfArms, startOfWeek, capitalInfo, postalCode):

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



