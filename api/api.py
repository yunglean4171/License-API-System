from flask import Flask
from flask_restful import Api, Resource
import mysql.connector

app = Flask(__name__)
api = Api(app)

# mysql database login credentials
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="licensesystem"
)
cursor = mydb.cursor()

class CheckKey(Resource):
    def get(self, licensekey, id):   
        mydb.reconnect()     
        cursor.execute(f"SELECT * FROM licensekey WHERE lkey = '{licensekey}' AND id = '{id}';")
        msg = cursor.fetchone()  
        if not msg:
          return 'false'
        else:
          return 'true'

class DeleteLicense(Resource):
    def delete(self, secretkey, licensekey):
        mydb.reconnect()   
        cursor.execute(f"SELECT * FROM secretkey WHERE skey = '{secretkey}';")
        msg = cursor.fetchone()  
        if not msg:
          return 'wrong secretkey!'
        else:
          mydb.reconnect()   
          cursor.execute(f"DELETE FROM `licensekey` WHERE lkey = '{licensekey}';")
          mydb.commit()
          return 'licensekey has been deleted'

class AddLicense(Resource):
    def post(self, secretkey, licensekey, id):      
        mydb.reconnect()   
        cursor.execute(f"SELECT * FROM secretkey WHERE skey = '{secretkey}';")
        msg = cursor.fetchone()  
        if not msg:
          return 'wrong secretkey!'
        else:
          mydb.reconnect()   
          sql = "INSERT INTO licensekey (lkey, id) VALUES (%s, %s)"
          val = (f"{licensekey}", f"{id}")
          cursor.execute(sql, val)
          mydb.commit()
          return 'licensekey has been added'

api.add_resource(CheckKey, "/<string:licensekey>/<string:id>")
api.add_resource(DeleteLicense, "/del/<string:secretkey>/<string:licensekey>")
api.add_resource(AddLicense, "/add/<string:secretkey>/<string:licensekey>/<string:id>")

if __name__ == '__main__':
    app.run(debug=True)  