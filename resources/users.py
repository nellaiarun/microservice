#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Arun T
"""
from flask_restful import Resource, reqparse

from models.users import UserModel

class SignUp(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('username', type=str, required=True, help="Username cannot be blank")
  parser.add_argument('password', type=str, required=True, help="Password cannot be blank")
  
  def post(self):
    received_data = SignUp.parser.parse_args()
    if not(UserModel.getUserByName(received_data["username"]) in [None, -99]):
      return({'message': 'An user with that name already exists!'}, 400)
    newUser = UserModel(0, received_data['username'], received_data['password'])
    if newUser.register():
      return({'message': 'User has been signed up successfully!'}, 201)
    else:
      return({'Error': 'An Error occurred while creating user {0}!'.format(received_data['username'])}, 404)
