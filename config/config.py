import jwt
from datetime import datetime,timedelta
import os

jwtkey = "Keyproject"
token_expire_minutes = 60
dbinfo={
    "hostname":"localhost",
    "username":"root",
    "password":"@Ditya1510",
    "database":"projectshopmanager"
}
dbtable={
    "shopkeeper":"shopkeeper",
    "product":"product",
    "shops":"shops"
}
def generate_jwt_token(userdata):
    exptime = datetime.now() + timedelta(minutes=token_expire_minutes)
    exp_epoch_time = int(exptime.timestamp())
    payload = {
        "payload":userdata,
        "exp":exp_epoch_time
    }
    return jwt.encode(payload,jwtkey,algorithm="HS256")

shopImagePath = "uploads/shop-images/"
productImagePath = "uploads/product-images/"

def writeFileShop(file):
    uniquename = str(datetime.now().timestamp()).replace(".","")
    filenamesplit = str(file.filename).split(".")
    extension = filenamesplit[len(filenamesplit)-1]
    databaseFileName = f"{shopImagePath}{uniquename}.{extension}"
    file.save(databaseFileName)
    return databaseFileName

def writeFileProduct(file):
    uniquename = str(datetime.now().timestamp()).replace(".","")
    filenamesplit = str(file.filename).split(".")
    extension = filenamesplit[len(filenamesplit)-1]
    databaseFileName = f"{productImagePath}{uniquename}.{extension}"
    file.save(databaseFileName)
    return databaseFileName

def removeFile(fileName):
    if os.path.exists(fileName):
        os.remove(fileName)
    else:
        print("The file does not exist")