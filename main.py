# !/usr/bin/env python
#--------------------------------------------------------
# Copyright (c) Hexaware Technology. All rights reserved.
# For more information please visit https://hexaware.com/
#--------------------------------------------------------

# This is a sample Python script to create database connectors for a given database.
# It will have database environment setup, reader and writer methods as such.

SnowflakeObject = "Debi"

class DBConnect1(SnowflakeObject): # inherit snowflake python object
	"""create a database connector sql server with db_user, db_host, db_port, db_password,
	(jdbc/odbc)-[on-prem] credentials, and snowflake - db_user, db_host, db_port, db_password,
	(jdbc/odbc)-[on-prem]"""
	def __init__(): pass
	def read_buffer(): pass
	def write_buffer(): pass


