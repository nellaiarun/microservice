#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Arun T
"""
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
import json

from models.products import ProductModel

class Product(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('src_id', type=int, required=True, help='Source System Id cannot be blank')
  parser.add_argument('prod_id', type=int, required=True, help='Natural Product Id cannot be blank')
  parser.add_argument('prod_name', type=str, required=True, help='Product must have a name')
  parser.add_argument('long_name', type=str, required=False, default='Unknown')
  parser.add_argument('prod_eff_date', type=str, required=False, default='01-01-9999')
  parser.add_argument('prod_end_date', type=str, required=False, default='01-01-9999')
  parser.add_argument('curr_ind', type=str, required=False, default='Y')
  parser.add_argument('sectr_name', type=str, required=False, default='Unknown')
  parser.add_argument('sectr_abbr_code', type=str, required=False, default='UKN')
  parser.add_argument('categ_name', type=str, required=False, default='Unknown')
  parser.add_argument('categ_abbr_code', type=str, required=False, default='UKN')
  parser.add_argument('co_name', type=str, required=False, default='Unknown')
  parser.add_argument('co_abbr_code', type=str, required=False, default='UKN')
  parser.add_argument('seg_name', type=str, required=False, default='Unknown')
  parser.add_argument('seg_abbr_code', type=str, required=False, default='UKN')
  parser.add_argument('brand_name', type=str, required=False, default='Unknown')
  parser.add_argument('brand_abbr_code', type=str, required=False, default='UKN')
  parser.add_argument('globl_form_name', type=str, required=False, default='Unknown')
  parser.add_argument('globl_form_abbr_code', type=str, required=False, default='UKN')
  parser.add_argument('item_gtin', type=int, required=False, default=0)
  parser.add_argument('su', type=float, required=False, default=0.00)
  parser.add_argument('gender', type=str, required=False, default='Universal')
  parser.add_argument('unit_sz_as', type=str, required=False, default='Unknown')
  
  @jwt_required()
  def post(self):
    received_data = Product.parser.parse_args()
    if ProductModel.getProductByNameAndSourceId(received_data['prod_name'], received_data['src_id']):
      return({'error': 'Product {0} with {1} Source already exists!'.format(received_data['prod_name'], received_data['src_id'])}, 400)
    product = ProductModel(received_data['src_id'], received_data['prod_id'], received_data['prod_name'], received_data['long_name'], received_data['prod_eff_date'], received_data['prod_end_date'], received_data['curr_ind'], received_data['sectr_name'], received_data['sectr_abbr_code'], received_data['categ_name'], received_data['categ_abbr_code'], received_data['co_name'], received_data['co_abbr_code'], received_data['seg_name'], received_data['seg_abbr_code'], received_data['brand_name'], received_data['brand_abbr_code'], received_data['globl_form_name'], received_data['globl_form_abbr_code'], received_data['item_gtin'], received_data['su'], received_data['gender'], received_data['unit_sz_as'])
    if product.createRefinedProduct():
      return({'message': 'Product {0} created successfully'.format(received_data['prod_name'])}, 201)
    else:
      return({'Error': 'An Error occurred while creating Product {0}!'.format(received_data['prod_name'])}, 404)


class ProductList(Resource):
  def get(self, prod_name, src_id):
    product = ProductModel.getProductByNameAndSourceId(prod_name, src_id)
    return({'Product': json.loads(json.dumps(product, sort_keys=True, indent=4, separators=(',',':'), default=str))}, 200 if product else 404)


class ProductListById(Resource):
  def get(self, prod_id):
    product = ProductModel.getProductById(prod_id)
    return(json.loads(json.dumps(product, sort_keys=True, indent=4, separators=(',',':'), default=str)), 200 if product else 404)


class ProductsList(Resource):
  def get(self):
    products = ProductModel('*','*','*','*','31-Dec-9999','31-Dec-9999','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*')
    allProducts = products.getAllProducts()
    if allProducts:
      return({'Products': json.loads(json.dumps(allProducts, sort_keys=True, indent=4, separators=(',',':'), default=str))}, 200)
    return({'error': 'no items found'}, 404)
