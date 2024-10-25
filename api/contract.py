import requests
import config

class contractAPI:
    def __init__(self):
        self.url_upload = config.BASE_URL + "/api/common/upload"
        self.url_addContract = config.BASE_URL + "/api/contract"

    # 上传合同
    def upload_contract(self, test_data,token):
        header_data = {
            "Authorization": token
        }
        return requests.post(url=self.url_upload,files={"file":test_data},headers=header_data)

    # 新增合同
    def add_contract(self,test_data,token):
        header_data = {
            "Authorization": token
        }
        return requests.post(url=self.url_addContract,json=test_data,headers=header_data)

