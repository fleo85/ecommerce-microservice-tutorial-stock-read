import pprint
import pymongo

from pymongo import MongoClient


def insert_into(host, product):
    client = MongoClient(host)
    db = client.ecommerce
        
    try:
        prod_id = product["id"]
        prod_in_db = db.products.find_one({"id": prod_id})
        if prod_in_db is not None:
            if product["quantita"] == 0:
                db.products.delete_one({"id": prod_id})
                print(" [x] Product removed.")
            else:
                db.products.update_one({"id": prod_id}, {"$set": product})
                print(" [x] Product updated.")
        else:
            db.products.insert_one(product)
            print(" [x] Product added.")
        pprint.pprint(product)
        
    except pymongo.errors.DuplicateKeyError:
        print(f"ERROR: duplicate key {product['_id']}")
    
