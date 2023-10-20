import bcrypt
import mysql.connector
from flask import make_response
from datetime import datetime,timedelta
from config.config import *
import jwt
import os

class shop_model():
    def __init__(self):
        try:
            self.conn=mysql.connector.connect(
                host=dbinfo['hostname'],
                user=dbinfo['username'],
                password=dbinfo['password'],
                database=dbinfo['database'])
            self.cur=self.conn.cursor(dictionary=True)
            self.conn.autocommit=True
            print("Connection success")
        except:
            print("some error")

    def shop_add_model(self,data):
        qry=f"INSERT INTO {dbtable['shops']}"
        qry+=f"(name, address, shopkeeper_id) VALUES('{data['name']}','{data['address']}',{data['shopkeeper']})"
        self.cur.execute(qry)
        return make_response({"message":"Successfully added"},200)


    def shop_list_get_model(self,shopkeeper_id,limit,pno):
        starting=(limit*pno)-limit
        qry=f"SELECT * FROM {dbtable['shops']} WHERE shopkeeper_id = {shopkeeper_id} LIMIT {starting},{limit}"
        self.cur.execute(qry)
        result=self.cur.fetchall()
        if len(result)>0:
            return make_response({"message":result,"page_no":pno,"limit":len(result)}, 200)
        else:
            return make_response({"message":"Data not found"}, 204)
    
    def shop_get_one_model(self,id):
        qry=f"SELECT * FROM {dbtable['shops']} WHERE id = {id}"
        self.cur.execute(qry)
        result=self.cur.fetchall()
        if len(result)>0:
            return make_response({"message":result}, 200)
        else:
            return make_response({"message":"Data not found"}, 204)

    def shop_update_model(self,data,id):
        qry=f"UPDATE {dbtable['shops']} SET "
        for key in data:
            qry+=f"{key}='{data[key]}', "
        qry=qry[:-2]+f" WHERE id={id}"
        self.cur.execute(qry)
        if(self.cur.rowcount) > 0:
            return make_response({"message":"Updated"},201)
        else :
            return make_response({"message":"Nothing to update"},202)
    
    def shop_off_model(self,id,v):
        qry=f"UPDATE {dbtable['shops']} SET is_open={v} WHERE id = {id}"
        self.cur.execute(qry)
        if self.cur.rowcount == 1:
            return make_response({"message":"Shop Updated successfully"},201)
        else:
            return make_response({"message":"Nothing to update"},202)
    
    def shop_disable_model(self,id,v):
        qry=f"UPDATE {dbtable['shops']} SET is_enable={v} WHERE id = {id}"
        self.cur.execute(qry)
        if self.cur.rowcount == 1:
            return make_response({"message":"User Updated successfully"},201)
        else:
            return make_response({"message":"Nothing to update"},202)
    
    def shop_upload_image_model(self,path,shop_id,index):
        qry = f"SELECT photo_{index} FROM {dbtable['shops']} WHERE id = {shop_id}"
        self.cur.execute(qry)
        result = self.cur.fetchall()
        removeFile(f"{result[0][f'photo_{index}']}")
        qry = f"UPDATE {dbtable['shops']} SET photo_{index} = '{path}' WHERE id = {shop_id}"
        self.cur.execute(qry)
        if self.cur.rowcount == 1:
            return make_response({"message":"User Updated successfully"},201)
        else:
            return make_response({"message":"Nothing to update"},202)
