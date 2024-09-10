from flask import Flask
from flask import Flask, request
import json
from config import db

app = Flask(__name__)

@app.get("/")
def home():
    return "Welcome to the product catalog"

@app.get("/about")
def about():
    me = {"name":"Lizbeth Ramirez"}
    return json.dumps(me)

@app.get("/footer")
def footer():
    pageName = {"pageName": "organika"}
    return json.dumps(pageName)

products = []

def fix_id(obj):
    obj["_id"]=str(obj["_id"])
    return obj

@app.get("/api/catalog")
def get_catalog():
    products = list(db.products.find())
    return json.dumps([fix_id(product) for product in products])

#  Los datos se gaurdaran en la base de datos
# @app.get("/api/products")
# def read_products():
#     return json.dumps(products)

@app.post("/api/catalog")
def save_product():
    item = request.get_json()
    db.products.insert_one(item)
    return json.dumps(fix_id(item))

# @app.post("/api/products")
# def save_products():
#     item = request.get_json()
#     # products.append(item)
#     db.products.insert_one(item)
#     print(item)
#     return json.dumps(fix_id(item))

#  Los datos se actualizaran en la base de datos
# @app.put("/api/products/<int:index>")
# def update_products(index):
#     update_item = request.get_json()
#     if 0<=index<len(products):
#         products[index]=update_item
#         return json.dumps(update_item)
#     else:
#         return "That index does not exist"
    
@app.get("/api/reports/total")
def get_total_value():
    products = list(db.products.find())
    total_value = sum(product.get('price', 0) for product in products)
    return json.dumps({"total_value": total_value})

@app.get("/api/products/<category>")
def get_products_by_category(category):
    products = list(db.products.find({"category": category}))
    return json.dumps([fix_id(product) for product in products])
    
@app.get("/api/products/count")
def num_products():
    count = db.products.count_documents({})
    return json.dumps({"count": count})

app.run(debug=True)