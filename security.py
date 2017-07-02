#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Arun T
"""
from werkzeug.security import safe_str_cmp

from models.users import UserModel

def authenticate(name, pwd):
  validUser = UserModel.getUserByName(name)
  if validUser == -99: validUser = None
  if validUser and safe_str_cmp(validUser.password, pwd):
    return validUser

def identity(payload):
  userId = payload['identity']
  return UserModel.getUserById(userId)
  