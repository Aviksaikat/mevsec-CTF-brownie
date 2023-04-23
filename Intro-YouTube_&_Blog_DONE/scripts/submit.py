#!/usr/bin/python3
from requests import get


def submit(FLAG_ID):
    # print(FLAG_ID)
    r = get(f"http://5.196.27.132:8080/get_flag?instance_ID={FLAG_ID}")
    print(r.text)
