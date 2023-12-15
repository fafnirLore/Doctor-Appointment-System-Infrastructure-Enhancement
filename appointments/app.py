# from flask import Flask, jsonify
# from pymongo import MongoClient
# import os

# app = Flask(__name__)
# APPOINTMENTS_DB_URL = ""
# if os.environ.get("APPOINTMENTS_DB_URL"):
#     APPOINTMENTS_DB_URL = os.environ.get("APPOINTMENTS_DB_URL")
# else:
#     APPOINTMENTS_DB_URL = "localhost:27017"

# print(f"APPOINTMENTS_DB_URL: {APPOINTMENTS_DB_URL}")

# appointments = [
#     {'id': "1", 'doctor': "1", 'date': "21 Nov 2023", 'rating': "Good"},
#     {'id': "2", 'doctor': "1", 'date': "22 Nov 2023", 'rating': "Bad"},
#     {'id': "3", 'doctor': "2", 'date': "22 Nov 2023", 'rating': "Good"},
#     {'id': "4", 'doctor': "1", 'date': "22 Nov 2023", 'rating': "Bad"},
#     {'id': "5", 'doctor': "2", 'date': "22 Nov 2023", 'rating': "Good"}
# ]

# # Connect to MongoDB
# client = MongoClient(f'mongodb://{APPOINTMENTS_DB_URL}')
# db = client['Doctor-Appointment-System']
# appointments_collection = db['Appointment']

# # Check if the collection is empty
# if appointments_collection.count_documents({}) == 0:
#     # Insert appointment data into MongoDB
#     result = appointments_collection.insert_many(appointments)
#     print("Appointment data inserted successfully.")
# else:
#     print("Database is not empty. Appointment data not inserted.")

# @app.route('/hello')
# def hello():
#     greeting = "Hello world!"
#     return greeting

# @app.route('/appointments', methods=["GET"])
# def getAppointments():
#     appointments = list(appointments_collection.find( {}, {'_id': False}))
#     return jsonify(appointments)

# @app.route('/appointment/<id>', methods=["GET"])
# def getAppointment(id):
#     appointment = appointments_collection.find_one({'id': id}, {'_id': False})
#     return jsonify(appointment)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=7070)

from flask import Flask, jsonify, request
app = Flask(__name__)

appointments = [
  { 'id': "1",'doctor': "1", 'date': "21 Nov 2023", 'rating':"Good"  },
  { 'id': "2",'doctor': "1", 'date': "22 Nov 2023", 'rating':"Bad"  },
  { 'id': "3",'doctor': "2", 'date': "22 Nov 2023", 'rating':"Good"  },
  { 'id': "4",'doctor': "1", 'date': "22 Nov 2023", 'rating':"Bad"  },
  { 'id': "5",'doctor': "2", 'date': "22 Nov 2023", 'rating':"Good"  },
]

@app.route('/hello')
def hello():
  greeting = "Hello world!"
  return greeting

@app.route('/appointments', methods=["GET"])
def getAppointments():
  return jsonify(appointments)

@app.route('/appointment/<id>', methods=["GET"])
def getAppointment(id):
  id = int(id) - 1
  return jsonify(appointments[id])

if __name__ == "__main__":
  app.run(host="0.0.0.0",port=7070)