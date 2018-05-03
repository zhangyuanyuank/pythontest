import requests
import unittest
import json
#from bs4 import BeautifulSoup


class MyTestSuite(unittest.TestCase):

    def model(self,url):
        result = requests.get(url, params={})
        r = result.json()
        print(r)
        return r


    def testbaidu(self):
        # test百度请求接口
        req=MyTestSuite.model(self,"https://api.aliexpress.com/openapi/param2/100/aliexpress.mobile/Itao.ProfileMobileApi.findUeMemberByMemberSeq_V31/13022?fakeMemberSeq=979496062&curFakeSeq=979496062&tb_eagleeyex_dump=1&_aop_signature=3A128F4345195480C3229DDE8D418934CBFE65D2&lang1=ru_US&tb_eagleeye_traceid=0b8ad74115215375670067000f")
        self.assertEqual(req.get('body').get('isLogin'), True, 'isLogin返回错误')
        #self.assertEqual(r.get('body').get('status'), 'enable')


    def getToken(self):
        # test 请求接口
        url = "https://api.aliexpress.com/openapi/param2/102/aliexpress.mobile/member.login/13022?_currency=USD&account=xx19@163.com&needRefreshToken=true&_lang=en_US&password=hello12345&deviceId=VQapjjkAoQQDAFZCkgIWGe5/&_aop_nonce=1XmNQVr4&_aop_signature=882875658327FE3ABE18CE4EF60D9BAD5C84809E"
        result= requests.post(url, params={})
        r = result.json()
        print(r)
        print(r.get('body').get('accessToken'))
        return  r.get('body').get('accessToken')


    def getTreeRanking(self):
        url="https://api.aliexpress.com/openapi/param2/100/aliexpress.mobile/Ugc.UgcCoinsTree.getTreeMixStatus/13022?access_token=a9d6022c-c751-453f-9858-abb74c334161&toMemberSeq=792106836&tb_eagleeyex_dump=1&_aop_signature=0C7D54BBFA498EEFB89CB96269E1E74C3DE36D72&tb_eagleeye_traceid=0bfa2e2415223986006728400f"
        result = requests.get(url, params={})
        r = result.json()
        print(r)
        self.assertEqual(r.get('head').get('code'), '200', 'code不为200')


    '''
    def dailyrecommendsMtop(self):
        url ="https://acs.aliexpress.com/gw/mtop.aliexpress.ugc.dailyrecommends.get/1.0/?origin=2&_lang=en_US&streamId=e9de90bf-bef0-4abf-be0b-b088dce0fc45"
        token =MyTestSuite()
        params= {'accesstoken': token.getToken()}
        result = requests.post(url, params=params)
        print(requests)
        r = result.json()
        print(r)
        self.assertEqual(r.get('data').get('hasNext'), "false", 'hasnext返回错误')
     '''









