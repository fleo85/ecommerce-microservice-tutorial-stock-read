import pprint
import pymongo

from pymongo import MongoClient


def insert_into(host, product):
    client = MongoClient(host)
    db = client.ecommerce
        
    try:
        db.products.insert_one(product)
        print(" [x] Product added.")
        pprint.pprint(product)
        
    except pymongo.errors.DuplicateKeyError:
        print(f"ERROR: duplicate key {product['_id']}")
    
