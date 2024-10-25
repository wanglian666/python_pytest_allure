import requests
import config

# 创建接口类
class LoginAPI:
    # 初始化
    def __init__(self):
        self.url_verify = config.BASE_URL + "/api/captchaImage"
        self.url_login = config.BASE_URL + "/api/login"

    # 获取验证码接口
    def get_verifyCode(self):
        response = requests.get(url=self.url_verify)
        return response

    # 登录接口
    def login(self,test_data):
        return requests.post(url=self.url_login,json=test_data)

