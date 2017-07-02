#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Arun T
"""
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
#from uwsgidecorators import postfork

from commons import connect
from security import authenticate, identity
from resources.products import Product, ProductList, ProductListById, ProductsList
from resources.users import SignUp

#@postfork
def initialize():
  connect()

app = Flask(__name__)
app.secret_key = "aruns_microservices_demo"
api = Api(app)
jwt = JWT(app, authentication_handler=authenticate, identity_handler=identity)

api.add_resource(Product, '/product/refine', endpoint='create_a_product')
api.add_resource(ProductList, '/product/search/<string:name>','/product/search/<string:name>/<int:sourceId>', defaults={'sourceId' : 1}, endpoint='list_a_product')
api.add_resource(ProductListById, '/product/search/id/<int:prod_id>', endpoint='list_a_product_by_id')
api.add_resource(ProductsList, '/product/catalog', endpoint='list_all_products')
api.add_resource(SignUp, '/user/register', endpoint='signup_user')

if __name__ == '__main__':
  initialize()
  app.run(debug=True, threaded=True)