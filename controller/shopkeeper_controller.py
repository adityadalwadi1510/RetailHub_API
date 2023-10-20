from app import app
from flask import request
from datetime import datetime
from model.shopkeeper_model import shopkeeper_model
from model.auth_model import auth_model

shopkeeperModelObj=shopkeeper_model()
authModelObj=auth_model()

@app.route("/shopkeeper/login",methods=['POST'])
def shopkeeper_login_controller():
    # return "shopkeeper_login_controller"
    return shopkeeperModelObj.shopkeeper_login_model(request.form)

@app.route("/shopkeeper",methods=['POST'])
def shopkeeper_signup_controller():
    # return "shopkeeper_signup_controller"
    return shopkeeperModelObj.shopkeeper_signup_model(request.form)

@app.route("/shopkeeper/<id>",methods=['PATCH'])
def shopkeeper_update_controller(id):
     return shopkeeperModelObj.shopkeeper_update_model(data=request.form,id=id)

@app.route("/shopkeeper/<id>/<value>",methods=['DELETE'])
def shopkeeper_disable_controller(id,value):
     return shopkeeperModelObj.shopkeeper_disable_model(id,value)

@app.route("/shopkeeper/<id>",methods=['GET'])
def shopkeeper_detail_controller(id):
     return "shopkeeper_detial_controller"





