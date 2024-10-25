import allure
import pytest

from api.login import LoginAPI
from api.crouse import crouseAPI
from config import BASE_PATH
from common import utils

@allure.feature("课程信息更新模块")
class TestUpdateCrouseAPI:
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
        TestUpdateCrouseAPI.TOKEN = res_l.json().get('token')
        print(TestUpdateCrouseAPI.TOKEN)

    # 课程修改
    @pytest.mark.parametrize("id,name,subject,price,applicablePerson,info,status,message,code",utils.build_data(BASE_PATH+'/data/updateCrouse.json'))
    def test_updateCrouse(self,id,name,subject,price,applicablePerson,info,status,message,code):
        data = {
            "id": id,
            "name": name,
            "subject": subject,
            "price": price,
            "applicablePerson": applicablePerson,
            "info": info
        }

        if code == 401:
            token = "xxx"
        else:
            token = TestUpdateCrouseAPI.TOKEN
        response = self.crouse_api.update_crouse(test_data=data,token=token)
        # print('课程修改',response.json())
        assert status == response.status_code
        assert message in response.text
        assert code == response.json().get('code')
