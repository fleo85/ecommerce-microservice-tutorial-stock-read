import connexion
import six

from pymongo import MongoClient

from swagger_server.models.product_list import ProductList  # noqa: E501
from swagger_server.models.product import Product
from swagger_server import util


def products_get(offset=None, limit=None):  # noqa: E501
    """products_get

     # noqa: E501

    :param offset: 
    :type offset: int
    :param limit: The numbers of items to return.
    :type limit: int

    :rtype: ProductList
    """
    client = MongoClient("mongodbhost")
    db = client.ecommerce
    if offset is not None and limit is not None:
        prods = db.products.find().skip(offset).limit(limit)
    else:
        prods = db.products.find()
        
    to_ret = []
    for prod in prods:
        pr = Product(prod)
        to_ret.append(pr)
    
    return ProductList(len(to_ret), to_ret)
    
