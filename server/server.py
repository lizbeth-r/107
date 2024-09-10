from flask import Flask, request
import json
from config import db

app = Flask(__name__)

@app.get("/")
def home():
    return "hello from flask"

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

@app.get("/api/products")
def read_products():
    return json.dumps(products)

@app.post("/api/products")
def save_products():
    item = request.get_json()
    # products.append(item)
    db.products.insert_one(item)
    print(item)
    return json.dumps(fix_id(item))

@app.put("/api/products/<int:index>")
def update_products(index):
    update_item = request.get_json()
    if 0<=index<len(products):
        products[index]=update_item
        return json.dumps(update_item)
    else:
        return "That index does not exist"
    
@app.get("/api/products/count")
def num_products():
    count = len(products)
    return json.dumps({"count": count})

app.run(debug=True)