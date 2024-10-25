import json

import allure
import pytest
from api.login import LoginAPI
from config import BASE_PATH
from common import utils

# 读取json文件
@allure.feature("登录模块--参数化allure open report/allure-report")
def build_data(json_file):
    test_data = []
    # 打开Json文件
    # f = open(json_file,'r',encoding="UTF-8")
    with open(json_file,'r',encoding="UTF-8") as f:
        # 加载json文件数据
        json_data = json.load(f)
        for case_data in json_data:
            # 数据格式转换[{},{}]-->[(),()]
            username = case_data['username']
            password = case_data['password']
            status = case_data['status']
            message = case_data['message']
            code = case_data['code']
            test_data.append((username, password, status, message, code))
    # f.close()
    return test_data

class TestLoginAPI:
    # 初始化
    uuid = None

    # 前置处理
    def setup_method(self):
        self.login_api = LoginAPI()
        # 获取图片验证码
        response = self.login_api.get_verifyCode()
        TestLoginAPI.uuid = response.json().get('uuid')

    @pytest.mark.parametrize("username,pwd,status,message,code",utils.build_data(BASE_PATH +"/data/login.json"))
    def test_login(self,username,pwd,status,message,code):
        login_data = {
            "username": username,
            "password": pwd,
            "code": "2",
            "uuid": TestLoginAPI.uuid
        }
        response = self.login_api.login(test_data=login_data)
        assert status == response.status_code
        assert message in response.text
        assert code == response.json().get('code')
