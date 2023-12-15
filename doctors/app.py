# from flask import Flask, jsonify
# from pymongo import MongoClient
# import os

# DOCTORS_DB_URL = ""
# if os.environ.get("DOCTORS_DB_URL"):
#     DOCTORS_DB_URL = os.environ.get("DOCTORS_DB_URL")
# else:
#     DOCTORS_DB_URL = "localhost:27017"

# print(f"DOCTORS_DB_URL: {DOCTORS_DB_URL}")

# app = Flask(__name__)

# # Connect to MongoDB
# client = MongoClient(f'mongodb://{DOCTORS_DB_URL}')
# db = client['Doctor-Appointment-System']
# doctors_collection = db['Doctor']

# # Check if the collection is empty
# if doctors_collection.count_documents({}) == 0:
#     # Insert doctors data into MongoDB
#     doctors_data = [
#         {'id': "1", 'firstName': "Muhammad Ali", 'lastName': "Kahoot", 'speciality': "DevOps"},
#         {'id': "2", 'firstName': "Good", 'lastName': "Doctor", 'speciality': "Test"}
#     ]
#     doctors_collection.insert_many(doctors_data)
#     print("Doctors data inserted successfully.")

# @app.route('/hello')
# def hello():
#     greeting = "Hello world!"
#     return greeting

# @app.route('/doctors', methods=["GET"])
# def getDoctors():
#     doctors = list(doctors_collection.find({}, {'_id': False}))
#     print(doctors)
#     return jsonify(doctors)

# @app.route('/doctor/<id>', methods=["GET"])
# def getDoctor(id):
#     doctor = doctors_collection.find_one({'id': id}, {'_id': False})
#     return jsonify(doctor)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=9090)

from flask import Flask, jsonify, request
app = Flask(__name__)

doctors = [
  { 'id': "1",'firstName': "Muhammad Ali", 'lastName': "Kahoot", 'speciality':"DevOps"  },
  { 'id': "2",'firstName': "Good", 'lastName': "Doctor",'speciality':"Test"  }
]

@app.route('/hello')
def hello():
  greeting = "Hello world!"
  return greeting

@app.route('/doctors', methods=["GET"])
def getDoctors():
  return jsonify(doctors)

@app.route('/doctor/<id>', methods=["GET"])
def getDoctor(id):
  id = int(id) - 1
  return jsonify(doctors[id])

if __name__ == "__main__":
  app.run(host="0.0.0.0",port=9090)