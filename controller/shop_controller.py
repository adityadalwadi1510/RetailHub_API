from app import app
from flask import request
from datetime import datetime
from model.shop_model import shop_model
from model.auth_model import auth_model
from config.config import *;
shopModel=shop_model()
authModelObj=auth_model()


@app.route("/shop",methods=["POST"])
# @authModelObj.token_auth()
def shop_add_controller():
    return shopModel.shop_add_model(request.form)

@app.route("/shop/<shopkeeper_id>/limit/<limit>/page/<pno>",methods=["GET"])
# @authModelObj.token_auth()
def shop_get_controller(shopkeeper_id,limit,pno):
    return shopModel.shop_list_get_model(shopkeeper_id,int(limit),int(pno))

@app.route("/shop/<id>",methods=["GET"])
# @authModelObj.token_auth()
def shop_one_shop_controller(id):
    return shopModel.shop_get_one_model(id=id)

@app.route("/shop/<id>",methods=["PATCH"])
# @authModelObj.token_auth()
def shop_update_controller(id):
    return shopModel.shop_update_model(data=request.form,id=id)

@app.route("/shop/shop-off/<id>/<value>",methods=["PATCH"])
# @authModelObj.token_auth()
def shop_off_controller(id,value):
    return shopModel.shop_off_model(id,value)

@app.route("/shop/<id>/<value>",methods=["DELETE"])
# @authModelObj.token_auth()
def shop_disable_controller(id,value):
    return shopModel.shop_disable_model(id=id,v=value)

@app.route("/shop/upload-image/<shop_id>/<index>",methods=["POST"])
# @authModelObj.token_auth()
def shop_upload_image_controller(shop_id,index):
    file = request.files['shopImage']
    databaseFileName = writeFileShop(file)
    return shopModel.shop_upload_image_model(databaseFileName,shop_id,index)