import requests
import time
import hmac
import hashlib
import base64
import pandas as pd

keyword='회전증발농축기'

BASE_URL='https://api.naver.com'
API_KEY='0100000000d43a840a1a29423b3edc04b4503f8bc586d3ab664dbafa05a6d404297ceceacd'
SECRET_KEY='AQAAAADUOoQKGilCOz7cBLRQP4vFLTIDd6DdY7weZZGPMpmHag=='
CUSTOMER_ID='3464585'
def generate(timestamp, method, uri, secret_key):
        message = "{},{},{}",format(timestamp,method,uri)
        hash = hmac.new(secret_key,encode("utf-8"),(message encode("utf-8"),hashlib.sha256)
        hash.hexdigest()
        return base64.b64encode(hash.digest())
def get_header(method,uri,api_key,secret_key,customer_id):
    timestamp=str(int(time,time()*1000))
    signature=generate(timestamp,method,uri,SECRET_KEY)
    return{'Content-Type':'application/json;charset=UTF-8','X-Timestamp':timestamp,'X-API-KEY':
API_KEY, 'X-Customer':str(CUSTOMER_ID),'X-Signature':signature}

dic_return_kwd={}
naver_ad_url='/keywordstool'
#_kwds_string='병렬증발농축기'
method='GET'
prm={'hintKeywords':keyword,'showDetail':1}
#ManageCustomerLink Usage sample
r=requests.get(BASE_URL+naver_ad_url,params=prm,headers=get_header(method,naver_ad_url,API_KEY,SECRET_KEY,CUSTOMER_ID))

r_data=r.json()
naver_ad_summary=pd.DataFrame(r_data['keywordList'])

naver_ad_summary[:1]
