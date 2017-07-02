#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Arun T
"""
from cassandra.cluster import Cluster

g_cluster = None
g_session = None
g_insert_prod = None
g_select_prod = None
g_select_prod_by_id = None
g_select_prod_specific = None
g_select_prod_count = None
g_select_user_count = None
g_select_user_by_id = None
g_select_user_by_name = None
g_insert_user = None

CASSANDRA_HOST = ['127.0.0.1']


def connect():
  global g_cluster, g_session, g_insert_prod, g_select_prod, g_select_prod_by_id, g_select_prod_specific, g_select_prod_count, g_select_user_count, g_select_user_by_id, g_select_user_by_name, g_insert_user, CASSANDRA_HOST
  g_cluster = Cluster(contact_points=CASSANDRA_HOST)
  g_session = g_cluster.connect()
  g_insert_prod = g_session.prepare("""insert into proddb.prod_dim(prod_skid, src_id, prod_id, prod_name, long_name, prod_eff_date, prod_end_date, curr_ind, sectr_name, sectr_abbr_code, categ_name, categ_abbr_code, co_name, co_abbr_code, seg_name, seg_abbr_code, brand_name, brand_abbr_code, globl_form_name, globl_form_abbr_code, item_gtin, su, gender, unit_sz_as) values(uuid(), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""")
  g_select_prod = g_session.prepare("""select * from proddb.prod_dim where prod_name=? and src_id=?""")
  g_select_prod_by_id = g_session.prepare("""select * from proddb.prod_dim where prod_id=? limit 1 allow filtering""")
  g_select_prod_specific = g_session.prepare("""select prod_skid, src_id, prod_id, prod_name, long_name, prod_eff_date, prod_end_date, curr_ind, sectr_name, sectr_abbr_code, categ_name, categ_abbr_code, co_name, co_abbr_code, seg_name, seg_abbr_code, brand_name, brand_abbr_code, globl_form_name, globl_form_abbr_code, item_gtin, su, gender, unit_sz_as from proddb.prod_dim""")
  g_select_prod_count = g_session.prepare("""select count(*) from proddb.prod_dim""")
  g_select_user_count = g_session.prepare("""select count(*) from usersdb.users where username=?""")
  g_select_user_by_name = g_session.prepare("""select user_id, username, password from usersdb.users where username=? limit 1""")
  g_select_user_by_id = g_session.prepare("""select user_id, username, password from usersdb.users where user_id=? limit 1 allow filtering""")
  g_insert_user = g_session.prepare("""insert into usersdb.users(user_id, username, password) values(uuid(), ?, ?)""")
