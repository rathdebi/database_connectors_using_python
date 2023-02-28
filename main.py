# !/usr/bin/env python

# This is a sample Python script to create database connectors for a given database.
# It will have database environment setup, reader and writer methods as such.

class DBConnect1(SnowflakeObject): # inherit from snowflake object base class
	"""create a database connector sql server with db_user, db_host, db_port, db_password,
	(jdbc/odbc)-[on-prem] credentials, and snowflake - db_user, db_host, db_port, db_password,
	(jdbc/odbc)-[on-prem]"""
	def __init__(): pass
	def read_buffer(): pass
	def write_buffer(): pass


class DBConnect1(SnowflakeObjectBaseClass): # inherit from Snowflake base class
    """this is a concept of database connectors using inline database credentials to 
    host and setup database instance with read and write methods"""
    import logging
	
    def __init__(self,db_user,db_password,dd_host_name):
        self.user = db_user
        self.password = db_password
        self.host = db_host_name
        
    def read_buffer(self,read_connector):
        if read_connector:
            logging.logger("read successful.")
        else:
            raise Exception("database error")
        
    def write_buffer(self,write_connector):
        if write_connector:
            logging.logger("write successful.")
        else:
            raise Exception("database error")


