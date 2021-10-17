from flask import Flask, json, request, jsonify
import products_dao #need to import products file to get products data access object
from sql_connection import get_sql_connection #need this here to connect to database

app = Flask(__name__)

connection = get_sql_connection()

@app.route("/getProducts", methods=['GET'])
def get_products():
    products = products_dao.get_all_products(connection)
    response = jsonify(products) #need to jsonify (wrap in json) for the flask server
    response.headers.add('Access-Control-Allow-Origin', '*') #CORS policy to allow response
    return response    

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)