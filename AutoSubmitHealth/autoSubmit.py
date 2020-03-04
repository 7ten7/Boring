import requests
from fromDbGetUser import getUserAll

def autoSubmit():

    userDict = getUserAll()
    for user in userDict:
        try:
            url = 'https://info.webvpn.wzvtc.cn/supply/check.jsp'
            submiturl = 'https://info.webvpn.wzvtc.cn/supply/put.jsp'
            session = requests.session()
            response = session.post(url=url,verify=False,data={
                'name':user['username'],
                'abc':user['password']
            })
            #print(response.text)
            if ('密码出错' in response.text):
                print('密码出错!!!')
                continue
            elif('用户名不存在' in response.text):
                print('用户名不存在!!!')
                continue
            else:
                response = session.post(url=submiturl,verify=False,data={
                    'b1':user['site'],
                    'b2':user['phone'],
                    'a1':'0',
                    'a11':'%C7%EB%B5%E3%BB%F7%B2%A2%CC%EE%D0%B4%CA%B5%B2%E2%CC%E5%CE%C2',
                    'a2':'0',
                    'a21':'%C7%EB%B5%E3%BB%F7%B2%A2%CC%EE%D0%B4%CA%B5%B2%E2%CC%E5%CE%C2',
                    'a3':'0',
                    'a4':'0',
                    'a41':'%C8%E7%D3%D0%A3%AC%C7%EB%B5%E3%BB%F7%B2%A2%CC%EE%D0%B4%CB%B5%C3%F7',
                    'a5':'0',
                    'a51':'',
                    'a52':'',
                    'a6':'0',
                    'a61':'',
                    'a62':'',
                    'a63':'0',
                    'a631':'',
                    'a7':'0',
                    'a71':'',
                    'a72':'',
                    'a73':'',
                    'a8':'1',
                    'a81':'',
                    'a9':'0',
                    'a91':'',
                    'a92':'',
                    'a93':'',
                    'a94':0
                })
                #print(response.text)
        except Exception:
            pass
    return True