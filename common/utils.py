import json

# json数据转换
# [{},{}]-->[(),()]
def build_data(json_file):
    test_data = []
    # 打开Json文件
    with open(json_file,'r',encoding="UTF-8") as f:
        # 加载json文件数据
        json_data = json.load(f)
        for case_data in json_data:
            temp_list = []
            allKey = case_data.keys()
            for key in allKey:
                temp_list.append(case_data[key])
            test_data.append(tuple(temp_list))
    print('测试数据',test_data)
    return test_data