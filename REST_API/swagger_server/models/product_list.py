# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.product import Product  # noqa: F401,E501
from swagger_server import util


class ProductList(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, total: int=None, products: List[Product]=None):  # noqa: E501
        """ProductList - a model defined in Swagger

        :param total: The total of this ProductList.  # noqa: E501
        :type total: int
        :param products: The products of this ProductList.  # noqa: E501
        :type products: List[Product]
        """
        self.swagger_types = {
            'total': int,
            'products': List[Product]
        }

        self.attribute_map = {
            'total': 'total',
            'products': 'products'
        }
        self._total = total
        self._products = products

    @classmethod
    def from_dict(cls, dikt) -> 'ProductList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ProductList of this ProductList.  # noqa: E501
        :rtype: ProductList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def total(self) -> int:
        """Gets the total of this ProductList.


        :return: The total of this ProductList.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total: int):
        """Sets the total of this ProductList.


        :param total: The total of this ProductList.
        :type total: int
        """

        self._total = total

    @property
    def products(self) -> List[Product]:
        """Gets the products of this ProductList.


        :return: The products of this ProductList.
        :rtype: List[Product]
        """
        return self._products

    @products.setter
    def products(self, products: List[Product]):
        """Sets the products of this ProductList.


        :param products: The products of this ProductList.
        :type products: List[Product]
        """

        self._products = products