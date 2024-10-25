import allure
import pytest

from api.login import LoginAPI
from api.crouse import crouseAPI
from config import BASE_PATH
from common import utils

@allure.feature("删除课程模块")
class TestDeleteCrouseAPI:
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
        TestDeleteCrouseAPI.TOKEN = res_l.json().get('token')
        print("TOKEN = ",TestDeleteCrouseAPI.TOKEN)

    # 课程删除
    @pytest.mark.parametrize("id,status,message,code",utils.build_data(BASE_PATH+"/data/deleteCrouse.json"))
    def test_deleteCrouse(self,id,status,message,code):
        if code == 401:
            token = "xxx"
        else:
            token = TestDeleteCrouseAPI.TOKEN
        response = self.crouse_api.delete_crouse(crouse_id=id,token=token)
        # print(response)
        assert status == response.status_code
        assert message in response.text
        assert code == response.json().get('code')
