#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Arun T
"""
import json
from uuid import UUID
from cassandra.util import Date

class DateEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Date):
      encoded_object = str(obj)
    elif isinstance(obj, UUID):
      encoded_object = str(obj)
    return encoded_object