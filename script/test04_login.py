import allure
import pytest

from api.login import LoginAPI

@allure.feature("登录模块")
class TestLoginAPI:
    # 初始化
    uuid = None

    # 前置处理
    def setup_method(self):
        self.login_api = LoginAPI()
        # 获取图片验证码
        response = self.login_api.get_verifyCode()
        TestLoginAPI.uuid = response.json().get('uuid')

    def teardown_method(self):
        pass

    # 登录成功
    @allure.story("登录成功")
    def test01_login_success(self):
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestLoginAPI.uuid
        }
        response = self.login_api.login(test_data=login_data)
        # 断言响应状态码为200
        assert response.status_code == 200
        # 断言响应数据包含“成功”
        assert '成功' in response.text
        # 断言响应json数据中code值
        assert response.json().get('code') == 200

    # 登录失败--用户名为空
    @allure.story("登录失败--用户名为空")
    def test02_login_without_username(self):
        login_data = {
            "username": "",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestLoginAPI.uuid
        }
        response = self.login_api.login(test_data=login_data)
        # 断言响应状态码为200
        assert response.status_code == 200
        # 断言响应数据包含“错误”
        assert '错误' in response.text
        # 断言响应json数据中code值
        assert response.json().get('code') == 500

    # 登录失败--用户名不存在
    @allure.story("登录失败--用户名不存在")
    def test03_login_username_not_exist(self):
        login_data = {
            "username": "jack666",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestLoginAPI.uuid
        }
        response = self.login_api.login(test_data=login_data)
        # 断言响应状态码为200
        assert response.status_code == 200
        # 断言响应数据包含“错误”
        assert '错误' in response.text
        # 断言响应json数据中code值
        assert response.json().get('code') == 500

if __name__ == '__main__':
    pytest.main()