import sqlite3

cloudantCredentials = {
  'username':'4bf164f1-4c0b-4611-b1e7-8a202f3da690-bluemix',
  'password':"""cb9162ba37e156d0ff1ec21354b13c9c01f5e93bd9b358ba3ab41c5d5fb5f67a""",
  'host':'4bf164f1-4c0b-4611-b1e7-8a202f3da690-bluemix.cloudant.com',
  'port':'443',
  'url':'https://4bf164f1-4c0b-4611-b1e7-8a202f3da690-bluemix:cb9162ba37e156d0ff1ec21354b13c9c01f5e93bd9b358ba3ab41c5d5fb5f67a@4bf164f1-4c0b-4611-b1e7-8a202f3da690-bluemix.cloudant.com'
}

db = sqlite3.connect('home-assistant_v2.db')
cursor = db.cursor()
