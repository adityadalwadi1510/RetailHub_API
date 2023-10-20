import bcrypt
import mysql.connector
from flask import make_response
from datetime import datetime,timedelta
from config.config import *
import jwt

class shopkeeper_model():
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

    def shopkeeper_signup_model(self,data):
        email = data['email']
        if(self.checkemail(email=email)):
            return make_response({"message":"User with email is already exists"},409)
        password = data['password']
        bytePwd = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashpass =bcrypt.hashpw(password=bytePwd,salt=salt)
        qry = f"INSERT INTO {dbtable['shopkeeper']}(email,password,salt) VALUES('{email}','{hashpass.decode()}','{salt.decode()}')"
        self.cur.execute(qry)
        qry = f"SELECT id FROM {dbtable['shopkeeper']} WHERE email = '{email}'"
        self.cur.execute(qry)
        result=self.cur.fetchall()
        id = result[0]['id']
        userdata = {
            "email":email,
            "id":id
            # role id need to add
        }
        token = generate_jwt_token(userdata=userdata)
        return make_response({"token":token},200)

    def shopkeeper_login_model(self,data):
        pwd=data['password'].encode('utf-8')
        email=data['email']
        qry=f"SELECT password,salt,enable FROM {dbtable['shopkeeper']} WHERE email='{email}'"
        self.cur.execute(qry)
        result=self.cur.fetchall()
        if len(result) == 0:
            return make_response({"message":"User not exists"},404)
        else:
            if(result[0]['enable'] == 0):
                return make_response({"message":"Please contact to our technical team"},203)
            usersalt = result[0]['salt'].encode('utf-8')
            userpass = result[0]['password']
            pwdhash=bcrypt.hashpw(pwd,usersalt).decode()
            if(userpass == pwdhash):
                qry=f"SELECT id,name,phone,email,address FROM {dbtable['shopkeeper']} WHERE email='{email}'"
                self.cur.execute(qry)
                result=self.cur.fetchall()
                userdata={
                    "id":result[0]['id'],
                    "email":result[0]['email']
                    # role id need to add
                    }
                token = generate_jwt_token(userdata=userdata)
                return make_response({"token":token,"data":result[0]},200)
            else:
                return make_response({"message":"Password is does not match with email"},401)

    
    def shopkeeper_update_model(self,data,id):
        qry=f"UPDATE {dbtable['shopkeeper']} SET "
        for key in data:
            qry+=f"{key} = '{data[key]}', "
        qry=qry[:-2]+f" WHERE id={id}"
        self.cur.execute(qry)
        if self.cur.rowcount == 1:
            return make_response({"message":"User Updated successfully"},201)
        else:
            return make_response({"message":"Nothing to update"},202)
    
    def shopkeeper_disable_model(self,id,v):
        qry=f"UPDATE {dbtable['shopkeeper']} SET enable={v} WHERE id = {id}"
        self.cur.execute(qry)
        if self.cur.rowcount == 1:
            return make_response({"message":"User Updated successfully"},201)
        else:
            return make_response({"message":"Nothing to update"},202)

    def checkemail(self,email):
        qry = f"SELECT id FROM {dbtable['shopkeeper']} WHERE email = '{email}'"
        self.cur.execute(qry)
        result=self.cur.fetchall()
        if(len(result) == 1): return True
        else: return False