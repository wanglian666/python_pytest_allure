import requests

import config


class crouseAPI:
    def __init__(self):
        self.url_addCrouse = config.BASE_URL + "/api/clues/course"
        self.url_queryCrouse = config.BASE_URL + "/api/clues/course/list"

    # 添加课程
    def add_crouse(self,test_data,token):
        header_data = {
            "Authorization":token
        }
        return requests.post(url=self.url_addCrouse,json=test_data,headers=header_data)

    # 查询课程列表
    def query_crouse(self,keywords,token):
        header_data = {
            "Authorization": token
        }
        return requests.get(url=self.url_queryCrouse,params=dict(keywords),headers=header_data)

    # 修改课程
    def update_crouse(self,test_data,token):
        header_data = {
            "Authorization": token
        }
        return requests.put(url=self.url_addCrouse,json=test_data,headers=header_data)

    # 删除课程
    def delete_crouse(self,crouse_id,token):
        header_data = {
            "Authorization": token
        }
        return requests.delete(url=self.url_addCrouse+f"/{crouse_id}",headers=header_data)
