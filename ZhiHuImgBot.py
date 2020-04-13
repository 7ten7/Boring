import requests
import re
import os
import time

class zhihu:
    def __init__(self,limit,offset):
        self.limit = limit
        self.offset = offset
        self.imgs = set()
        self.getImgUrlList()

    def getImgUrl(self,limit,offset):
        url = 'https://www.zhihu.com/api/v4/questions/58498720/answers?include=content&limit={}&offset={}'.format(limit,offset)
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
        }
        response = requests.get(url=url, headers=headers)
        r_json = response.json()
        try:
            for ones in r_json['data']:
                self.imgs = self.imgs | set(re.findall(r'data-original="(.*?)"', ones['content']))
        except Exception:
            print('发生错误，请检查')

    def getImgUrlList(self):
        if self.limit > 5:
            num = self.limit // 5
            last_num = self.limit - (num * 5)
            for i in range(num+1):
                if i < num:
                    print('[Analysis] 正分析第'+ str(i+1) +'组URL。')
                    self.getImgUrl(5,self.offset+i*5)
                    time.sleep(1) # 控制下时间，避免并发过快
                elif last_num != 0:
                    self.getImgUrl(last_num,self.offset+i*5)
        else:
            self.getImgUrl(5, self.offset)

    def dowload(self):
        i = 1
        for img_url in self.imgs:
            print('[Download] 正在下载第'+ str(i) +'张图片。')
            time.sleep(1) # 控制下时间，避免并发过快
            img_raw = requests.get(img_url).content
            if (not os.path.exists('zhihuIMG')):
                os.mkdir('zhihuIMG')
            img = open('zhihuIMG/pic' + str(i) + '.jpg', 'wb')
            img.write(img_raw)
            img.close()
            i += 1
        print('[END] 全部图片下载完毕！！！')

a = zhihu(1075,1)
a.dowload()