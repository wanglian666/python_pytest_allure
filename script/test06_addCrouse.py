import allure
import pytest

from api.login import LoginAPI
from api.crouse import crouseAPI
from common import utils
from config import BASE_PATH

@allure.feature("合同新增模块")
class TestAddCrouseAPI:
    # 初始化
    TOKEN = None

    # 前置处理
    def setup_class(self):
        self.login_api = LoginAPI()
        self.crouse_api = crouseAPI()

        # 登录成功
        res_v = self.login_api.get_verifyCode()
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": res_v.json().get('uuid')
        }
        res_l = self.login_api.login(test_data=login_data)
        TestAddCrouseAPI.TOKEN = res_l.json().get('token')
        print(TestAddCrouseAPI.TOKEN)

    # 课程添加
    @pytest.mark.parametrize("name,subject,price,applicablePerson,info,status,message,code",utils.build_data(BASE_PATH+"/data/addCrouse.json"))
    def test_addCrouse(self,name,subject,price,applicablePerson,info,status,message,code):
        data = {
            "name": name,
            "subject": subject,
            "price": price,
            "applicablePerson": applicablePerson,
            "info": info
          }
        if code == 401:
            token = "xxxxx"
        else:
            token = TestAddCrouseAPI.TOKEN

        response = self.crouse_api.add_crouse(test_data=data, token=token)
        # print(response.json())
        assert response.status_code == status
        assert message in response.text
        assert response.json().get('code') == code
