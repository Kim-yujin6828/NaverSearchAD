import time
import requests
import pandas as pd

import Signaturehelper

    def get_header(method, uri, api_key, secret_key, customer_id):
    timestamp = str(round(time.time() * 1000))
    signature = signaturehelper.Signature.generate(timestamp, method, uri, SECRET_KEY)
    return {'Content-Type': 'application/json; charset=UTF-8', 'X-Timestamp': timestamp, 'X-API-KEY': API_KEY, 'X-Customer': str(CUSTOMER_ID), 'X-Signature': signature}

BASE_URL = 'https://api.naver.com'
API_KEY = '0100000000b6927c1ac66cb557dd39df9e2f978ab5ae7500fbc1dee1cf5da92614728a5376'
SECRET_KEY = 'AQAAAAC2knwaxmy1V905354vl4q1VKqCPoB6ca8LtOIcyrMdbg=='
CUSTOMER_ID = '3464585'

uri = '/keywordstool'
method = 'GET'
keyword='회전증발농축'
r = requests.get(BASE_URL + uri, params={'siteId':None, 'biztpId':None, 'hintKeywords': keyword, 'event':None, 'month':None, 'showDetail':'1'}, headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))

df_keyword = pd.DataFrame([r.json()['keywordList'][0]]).set_index('relKeyword')

df_keyword.rename({'monthlyPcQcCnt':'월간 PC조회수','monthlyMobileQcCnt':'월간 모바일 조회수','monthlyAvePcClkCnt':'월간 평균 PC 클릭수', 'monthlyAveMobileClkCnt':'월간 평균 모바일 클릭수', 'monthlyAvePcCtr':'월간 평균 PC 클릭율', 'monthlyAveMobileCtr':'월간 평균 모바일 클릭율', 'plAvgDepth':'월간 평균 PC 광고수', 'compIdx':'PC 광고 기반 경쟁력'}, axis=1, inplace=True)
df_keyword.index.name = '키워드'

df_keyword = df_keyword[['월간 PC조회수', '월간 모바일 조회수', '월간 평균 PC 클릭수', '월간 평균 모바일 클릭수', '월간 평균 PC 클릭율', '월간 평균 모바일 클릭율', '월간 평균 PC 광고수', 'PC 광고 기반 경쟁력']]
df_keyword
