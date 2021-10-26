#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Derek on 2021/10/26
"""
-------------------------------------------------
File Name : main_requests 
Description : show basic usage of requests
Author : derek
Email : derek_simon@outlook.com
-------------------------------------------------
Change Activity:
    2021/10/26: create
-------------------------------------------------
"""

__author__ = 'derek'


import requests

if __name__ == '__main__':

    response = requests.get('https://cn.bing.com/')
    print(response.request.headers)
    print(response.request.body)

    print(response.url)
    print(response.status_code)
    print(response.headers)
    print(response.text)
    #print(response.json())

