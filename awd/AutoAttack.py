import json
import HackRequests
import logging
import re


class AutoAttack:
    def __init__(self, config_path: str):
        logging.basicConfig(level=logging.INFO,format='%(asctime)s---%(levelname)s: %(message)s')
        self.__parse(config_path)

    def __parse(self, config_path: str):
        f = open(config_path)
        file = f.read()
        try:
            self.config = json.loads(file)
        except json.JSONDecodeError:
            print('attack.json文件解析出错，请检查后重试！')
            exit()

    def __attack(self, headers: str, data: str, ssl: bool = False) -> list:
        request = HackRequests.hackRequests()
        response = request.httpraw(raw=headers, post=data, ssl=ssl)
        return response.text()

    def __findFlag(self,html):
        flag = re.findall(r'flag{.*?}',html)
        return flag

    def aoe(self):
        flags = []
        for challengeName, challengeData in self.config.items():
            logging.info('正在攻击的题目为 ----> '+challengeName)
            if challengeData['ssl'] == 'True':
                html = self.__attack(challengeData['header'], challengeData['data'], ssl=True)
            else:
                html = self.__attack(challengeData['header'], challengeData['data'])
            flag = self.__findFlag(html)
            flags += flag
        return flags