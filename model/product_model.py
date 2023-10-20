import bcrypt
import mysql.connector
from flask import make_response
from datetime import datetime,timedelta
from config.config import *
import jwt

class product_model():
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

    def product_add_model(self,data):
        qry = f"INSERT INTO {dbtable['product']}("
        qry+= f"name, description, ingredients, remarks, shop_id) "
        qry+= f"VALUES('{data['name']}', '{data['description']}', '{data['ingredients']}', '{data['remarks']}', {data['shop_id']})"
        self.cur.execute(qry)
        return make_response({"message":"Successfully added"},200)
    
    def product_get_one_model(self,id):
        qry=f"SELECT * FROM {dbtable['product']} WHERE id = {id}"
        self.cur.execute(qry)
        result=self.cur.fetchall()
        if len(result)>0:
            return make_response({"message":result}, 200)
    
    def product_update_model(self,data,id):
        qry=f"UPDATE {dbtable['product']} SET "
        for key in data:
            qry+=f"{key}='{data[key]}', "
        qry=qry[:-2]+f" WHERE id={id}"
        self.cur.execute(qry)
        if(self.cur.rowcount) > 0:
            return make_response({"message":"Updated"},201)
        else :
            return make_response({"message":"Nothing to update"},202)
    
    def product_get_list_model(self,shop_id,limit,pno):
        starting=(limit*pno)-limit
        qry=f"SELECT * FROM {dbtable['product']} WHERE shop_id = {shop_id} LIMIT {starting},{limit}"
        self.cur.execute(qry)
        result=self.cur.fetchall()
        if len(result)>0:
            return make_response({"message":result,"page_no":pno,"limit":len(result)}, 200)
        else:
            return make_response({"message":"Data not found"}, 204)
    
    def product_disable_model(self,id,v):
        qry=f"UPDATE {dbtable['product']} SET is_available={v} WHERE id = {id}"
        self.cur.execute(qry)
        if self.cur.rowcount == 1:
            return make_response({"message":"User Updated successfully"},201)
        else:
            return make_response({"message":"Nothing to update"},202)
    
    def product_upload_image_model(self,product_id,image_name,index):
        qry = f"SELECT photo_{index} FROM {dbtable['product']} WHERE id = {product_id}"
        self.cur.execute(qry)
        result = self.cur.fetchall()
        removeFile(f"{result[0][f'photo_{index}']}")
        qry = f"UPDATE {dbtable['product']} SET photo_{index} = '{image_name}' WHERE id = {product_id}"
        self.cur.execute(qry)
        if self.cur.rowcount == 1:
            return make_response({"message":"User Updated successfully"},201)
        else:
            return make_response({"message":"Nothing to update"},202)