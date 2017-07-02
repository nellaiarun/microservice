#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Arun T
"""
import pandas as pd
from datetime import datetime
from dateutil.parser import parse
from cassandra.query import named_tuple_factory

import commons

class ProductModel:
  def __init__(self, src_id, prod_id, prod_name, long_name, prod_eff_date, prod_end_date, curr_ind, sectr_name, sectr_abbr_code, categ_name, categ_abbr_code, co_name, co_abbr_code, seg_name, seg_abbr_code, brand_name, brand_abbr_code, globl_form_name, globl_form_abbr_code, item_gtin, su, gender, unit_sz_as):
    self.src_id = src_id
    self.prod_id = prod_id
    self.prod_name = prod_name
    self.long_name = long_name
    self.prod_eff_date = datetime.date(parse(prod_eff_date))
    self.prod_end_date = datetime.date(parse(prod_end_date))
    self.curr_ind = curr_ind
    self.sectr_name = sectr_name
    self.sectr_abbr_code = sectr_abbr_code
    self.categ_name = categ_name
    self.categ_abbr_code = categ_abbr_code
    self.co_name = co_name
    self.co_abbr_code = co_abbr_code
    self.seg_name = seg_name
    self.seg_abbr_code = seg_abbr_code
    self.brand_name = brand_name
    self.brand_abbr_code = brand_abbr_code
    self.globl_form_name = globl_form_name
    self.globl_form_abbr_code = globl_form_abbr_code
    self.item_gtin = item_gtin
    self.su = su
    self.gender = gender
    self.unit_sz_as = unit_sz_as

  @classmethod
  def getProductByNameAndSourceId(cls, prod_name, src_id):
    prod_name = prod_name.strip()
    try:
      records = commons.g_session.execute(commons.g_select_prod, [prod_name, src_id], timeout=None)
      for record in records:
        if record.prod_name == prod_name:
          return({'prod_skid' : record.prod_skid, 'src_id' : record.src_id, 'prod_id' : record.prod_id, 'prod_name' : record.prod_name, 'long_name' : record.long_name, 'prod_eff_date' : record.prod_eff_date, 'prod_end_date' : record.prod_end_date, 'curr_ind' : record.curr_ind, 'sectr_name' : record.sectr_name, 'sectr_abbr_code' : record.sectr_abbr_code, 'categ_name' : record.categ_name, 'categ_abbr_code' : record.categ_abbr_code, 'co_name' : record.co_name, 'co_abbr_code' : record.co_abbr_code, 'seg_name' : record.seg_name, 'seg_abbr_code' : record.seg_abbr_code, 'brand_name' : record.brand_name, 'brand_abbr_code' : record.brand_abbr_code, 'globl_form_name' : record.globl_form_name, 'globl_form_abbr_code' : record.globl_form_abbr_code, 'item_gtin' : record.item_gtin, 'su' : record.su, 'gender' : record.gender, 'unit_sz_as' : record.unit_sz_as})
      return(None)
    except:
      return(None)

  @classmethod
  def getProductById(cls, prod_id):
    try:
      records = commons.g_session.execute(commons.g_select_prod_by_id, [prod_id])
      for record in records:
        if record.prod_id == prod_id:
          return({'prod_skid' : record.prod_skid, 'src_id' : record.src_id, 'prod_id' : record.prod_id, 'prod_name' : record.prod_name, 'long_name' : record.long_name, 'prod_eff_date' : record.prod_eff_date, 'prod_end_date' : record.prod_end_date, 'curr_ind' : record.curr_ind, 'sectr_name' : record.sectr_name, 'sectr_abbr_code' : record.sectr_abbr_code, 'categ_name' : record.categ_name, 'categ_abbr_code' : record.categ_abbr_code, 'co_name' : record.co_name, 'co_abbr_code' : record.co_abbr_code, 'seg_name' : record.seg_name, 'seg_abbr_code' : record.seg_abbr_code, 'brand_name' : record.brand_name, 'brand_abbr_code' : record.brand_abbr_code, 'globl_form_name' : record.globl_form_name, 'globl_form_abbr_code' : record.globl_form_abbr_code, 'item_gtin' : record.item_gtin, 'su' : record.su, 'gender' : record.gender, 'unit_sz_as' : record.unit_sz_as})
      return({'prod_id' : prod_id})
    except:
      return(None)

  def createRefinedProduct(self):
    try:
      commons.g_session.execute_async(commons.g_insert_prod, [self.src_id, self.prod_id, self.prod_name, self.long_name, self.prod_eff_date, self.prod_end_date, self.curr_ind, self.sectr_name, self.sectr_abbr_code, self.categ_name, self.categ_abbr_code, self.co_name, self.co_abbr_code, self.seg_name, self.seg_abbr_code, self.brand_name, self.brand_abbr_code, self.globl_form_name, self.globl_form_abbr_code, self.item_gtin, self.su, self.gender, self.unit_sz_as])
    except:
      return(False)
    else:
      return(True)

  def getAllProducts(self):
    rc = commons.g_session.execute(commons.g_select_prod_count)[0]
    if rc.count == 0: return(None)
    commons.g_session.row_factory = lambda columns, rows: pd.DataFrame(rows, columns=columns)
    try:
      records = commons.g_session.execute(commons.g_select_prod_specific, timeout=None)
      df = records._current_rows
      df.columns = ['prod_skid', 'src_id', 'prod_id', 'prod_name', 'long_name', 'prod_eff_date', 'prod_end_date', 'curr_ind', 'sectr_name', 'sectr_abbr_code', 'categ_name', 'categ_abbr_code', 'co_name', 'co_abbr_code', 'seg_name', 'seg_abbr_code', 'brand_name', 'brand_abbr_code', 'globl_form_name', 'globl_form_abbr_code', 'item_gtin', 'su', 'gender', 'unit_sz_as']
      return(df.to_dict(orient='records'))
    except:
      return(None)
    finally:
      commons.g_session.row_factory = named_tuple_factory
