import requests
import json


class AutoSubmitFlag:
    def __init__(self, config_path: str):
        self.__getConfig(config_path)

    def __getConfig(self, config_path: str):
        f = open(config_path)
        file = f.read()
        try:
            self.config = json.loads(file)
        except json.JSONDecodeError:
            print('config.json文件解析出错，请检查后重试！')
            exit()

    def submitFlag(self, change_id: int, flag: str) -> str:
        headers = {}
        cookies = {}
        for key, value in self.config['submitFlag']['headers'].items():
            headers[key] = value
        for key, value in self.config['submitFlag']['cookies'].items():
            cookies[key] = value
        url = self.config['submitFlag']['submitUrl']
        data = {"challenge_id": change_id, "submission": flag}
        response = requests.post(url=url, data=json.dumps(data), headers=headers, cookies=cookies)
        return response.text
