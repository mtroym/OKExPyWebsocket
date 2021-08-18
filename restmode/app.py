# coding=utf8
from pprint import pprint

import requests
import urllib3

import app_utils as u
from config import HTTP_URL

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def request_get(request_path):
    # http时需要访问什么接口，headers和url都得设置成相同的
    target_url = HTTP_URL + request_path
    headers = u.header_util.get_rest_sign(request_path=request_path)
    response = requests.get(target_url, headers=headers, verify=False, params={"instId": "KSM-USDT-SWAP"})
    return response.json()


if __name__ == "__main__":
    res = request_get("/api/v5/market/ticker")
    # pprint(res, width=20)
    if res["code"] == "0":
        for market in res["data"]:
            print("market: {}, Price: {}".format(market["instId"], market["last"]))
        # pprint(res["data"], width=20)
    else:
        print(res)
        # print(res["code"], res["data"])
