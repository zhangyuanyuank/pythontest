import requests
import unittest
import json
#from bs4 import BeautifulSoup


class MyTestSuite(unittest.TestCase):


    def testbaidu(self):
        # test百度请求接口
        url = "https://api.aliexpress.com/openapi/param2/100/aliexpress.mobile/Itao.ProfileMobileApi.findUeMemberByMemberSeq_V31/13022?fakeMemberSeq=979496062&curFakeSeq=979496062&tb_eagleeyex_dump=1&_aop_signature=3A128F4345195480C3229DDE8D418934CBFE65D2&lang1=ru_US&tb_eagleeye_traceid=0b8ad74115215375670067000f"
        result = requests.get(url, params={})
        r=result.json()
        print(r)
        self.assertEqual(r.get('body').get('isLogin'),True,'isLogin')
        self.assertEqual(r.get('body').get('status'), 'enable')



    def testitao(self):
        # test itao请求接口
        url = "https://ru.itao.com"
        result1 = requests.get(url, params={})
        #r1= result1.text
        print(result1)








