import allure
import pytest
from config import BASE_PATH
from common import utils

from api.login import LoginAPI
from api.crouse import crouseAPI

@allure.feature("查询课程列表模块")
class TestQueryCrouseAPI:
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
        TestQueryCrouseAPI.TOKEN = res_l.json().get('token')
        print(TestQueryCrouseAPI.TOKEN)

    # 课程查询
    @pytest.mark.parametrize("keyword,status,message,code",utils.build_data(BASE_PATH+"/data/queryCrouse.json"))
    def test_queryCrouse(self,keyword,status,message,code):
        if code == 401:
            token = "xxxx"
        else:
            token = TestQueryCrouseAPI.TOKEN

        response = self.crouse_api.query_crouse(keywords=keyword,token=token)
        # print('课程查询',response.json())
        assert response.status_code == status
        assert message in response.text
        assert response.json().get('code') == code