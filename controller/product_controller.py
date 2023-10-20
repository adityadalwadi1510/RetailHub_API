from app import app
from flask import request
from datetime import datetime
from model.product_model import product_model
from model.auth_model import auth_model
from config.config import *;

productModelObj=product_model()
authModelObj=auth_model()

@app.route("/product",methods=["POST"])
# @authModelObj.token_auth()
def prodcut_add_controller():
    return productModelObj.product_add_model(request.form)

@app.route("/product/<id>",methods=["GET"])
# @authModelObj.token_auth()
def get_prodcut_get_controller(id):
    return productModelObj.product_get_one_model(id)

@app.route("/product/<id>",methods=["PATCH"])
# @authModelObj.token_auth()
def update_prodcut_update_controller(id):
    return productModelObj.product_update_model(request.form,id)

@app.route("/product/<shop_id>/limit/<limit>/page/<pno>",methods=["GET"])
# @authModelObj.token_auth()
def prodcut_get_list_controller(shop_id,limit,pno):
    return productModelObj.product_get_list_model(shop_id,int(limit),int(pno))

@app.route("/product/<id>/<value>",methods=["DELETE"])
# @authModelObj.token_auth()
def prodcut_disable_controller(id,value):
    return productModelObj.product_disable_model(id,value)

@app.route("/product/upload-image/<product_id>/<index>",methods=["POST"])
# @authModelObj.token_auth()
def product_upload_image_controller(product_id,index):
    file = request.files['productImage']
    databaseFileName = writeFileProduct(file)
    return productModelObj.product_upload_image_model(product_id,databaseFileName,index)