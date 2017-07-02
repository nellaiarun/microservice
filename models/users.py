#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Arun T
"""
import uuid

import commons

class UserModel():
  def __init__(self, userId, userName, password):
    self.id = userId #Flask-JWT : identity = getattr(identity, 'id') or identity['id']
    self.userName = userName
    self.password = password

  @classmethod
  def getUserByName(cls, userName):
    try:
      rc = commons.g_session.execute(commons.g_select_user_count, [userName])[0]
      if rc.count == 0: return(None)
    except:
      return(-99)
    else:
      record = commons.g_session.execute(commons.g_select_user_by_name, [userName])[0]
      return cls(str(record.user_id), record.username, record.password)

  @classmethod
  def getUserById(cls, userId):
    userId = uuid.UUID(userId)
    records = commons.g_session.execute(commons.g_select_user_by_id, [userId])
    for row in records:
      if row.user_id == userId:
        user = cls(str(row.user_id), row.username, row.password)
        return user
    return None

  def register(self):
    try:
      commons.g_session.execute_async(commons.g_insert_user, [self.userName, self.password])
    except:
      return(False)
    else:
      return(True)
