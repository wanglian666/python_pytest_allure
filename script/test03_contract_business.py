# 合同新增业务
import allure
import pytest
import os

from api.login import LoginAPI
from api.crouse import crouseAPI
from api.contract import contractAPI

# 获取项目根路径
current_file_name = __file__;
BASE_PATH = os.path.dirname(current_file_name)  # D:\\python_study\\KDTX\\script\\test03_contract_business.py

# 创建测试类
@allure.feature("主流程")
class TestBusinessContract:
    token = None

    # 前置处理
    def setup_class(self):
        self.login_api = LoginAPI()
        self.crouse_api = crouseAPI()
        self.contract_api = contractAPI()

    # 后置处理
    def teardown(self):
        pass

    # 1、登录成功
    def test01_login_success(self):
        # 获取验证码
        res_v = self.login_api.get_verifyCode()
        # 打印uuid数据
        print(res_v.json().get('uuid'))

        # 登录
        login_data = {
            "username":"admin",
            "password":"HM_2023_test",
            "code":"2",
            "uuid":res_v.json().get('uuid')
        }
        res_l = self.login_api.login(login_data)
        if res_l.json().get('code') == 200:
            print("登录成功")
        TestBusinessContract.token = res_l.json().get('token')

    # 2、添加课程成功
    def test02_addCrouse(self):
        data = {
            "name": "测试开发提升课01",
            "subject": "6",
            "price": 899,
            "applicablePerson": "2",
            "info": "测试开发提升课01"
        }

        res = self.crouse_api.add_crouse(data,TestBusinessContract.token)
        if res.json().get('code') == 200:
            print("课程添加成功")

    # 3、上传合同成功
    def test03_upload_contract(self):
        f = open(BASE_PATH+"/../data/test.pdf","rb")
        res = self.contract_api.upload_contract(test_data=f,token=TestBusinessContract.token)
        if res.json().get('code') == 200:
            print("合同上传成功")

    # 4、合同新增成功
    def test04_addContract(self):
        data = {
            "name": "测试888",
            "phone": "13612341888",
            "contractNo": "HT10012099",
            "subject": "6",
            "courseId": 99,
            "channel": "0",
            "activityId": 77,
            "fileName": "/profile/upload/2023/01/05/86e5a3b8-b08c-470c-a17d-71375c3a8b9f.pdf"
        }
        res = self.contract_api.add_contract(test_data=data,token=TestBusinessContract.token)
        print(res.status_code)
        print(res.json())

if __name__ == '__main__':
    pytest.main()

