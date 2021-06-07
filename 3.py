#!/usr/bin/env python
# coding=utf-8

import requests


class RunMain:

    def __init__(self):
        pass

    @staticmethod
    def send_post(url, params=None):

        try:
            res = requests.post(url=url, data=params)
            return res
        except Exception as msg:
            return msg

    @staticmethod
    def send_get(url, params=None):
        try:
            res = requests.get(url=url, params=params)
            return res
        except Exception as msg:
            return msg

    def run_main(self, url, method, params=None):
        if method == 'GET':
            print('This is a get request')
            res = self.send_get(url, params)
        elif method == 'POST':
            print('This is a post request')
            res = self.send_post(url, params)

            return res
        else:
            print('请重新输入请求方式')
        return res


if __name__ == '__main__':
    # url_dict0 = {
    #     'url': 'http://baidu.com/',
    #     'method': 'GET'
    # }
    url0 = 'http://baidu.com/'
    params0 = {
        'key1': 'params1', 'key2': 'params2'
    }
    Res = RunMain()
    res0 = Res.run_main(url=url0, method='GET')
    print(res0)
    print(type(res0))

