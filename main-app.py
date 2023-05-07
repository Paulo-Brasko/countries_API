import json
from sqlalchemy import JSON, create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Base, Person, Country, Test

engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session=Session()

# p1 = Person(31323, "Mike", "Grown", "m", 30)
# p2 = Person(31324, "Anna", "Grown", "f", 36)
# p3 = Person(31325, "Brenno", "Grown", "m", 14)

# session.add(p1)
# session.add(p2)
# session.add(p3)

# session.commit()

# results = session.query(Person).all()
# print(results)

# results = session.query(Person).filter(Person.lastName == "Grown")
# for r in results:
#     print(r)

# # elements in tuples
# list1 = ('1', '2', '3', '4')
 
# # put any character to join
# s = ","
 
# # joins elements of list1 by '-'
# # and stores in string s
# s = s.join(list1)
 
# # join use to join a list of
# # strings to a separator s
# print(s)

# t1 = Thing(1, s, "hohoho")
# session.add(t1)
# session.commit()

# results = session.query(Thing).all()
# print(results)

name_obj = { 
    "name": {
        "common" : "Brazil",
        "official" : "Federative Republic of Brazil", 
        "nativeName" : {
            "por" : {
                "official" : "República Federativa do Brasil",
                "common" : "Brasil"
            }
        }
    }
}

print("banana")
myJson = json.dumps(name_obj)
print(myJson)
 
# test1 = Test(myJson)
# print(test1)
# session.add(test1)
# session.commit()

results = session.query(Test).all()
json_object = results[0].toJson()
print("testing...")
print(json_object)
keys = json_object.keys()
for key in keys: 
    print(key, json_object[key]["common"])