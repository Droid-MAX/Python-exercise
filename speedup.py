#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import requests

url = 'http://dc.qq.com/ebitapi/speedup/open'

header = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'dc.qq.com/ebitapi/speedup/open',
    'Accept': '*/*',
    'Host': 'dc.qq.com',
    'Content-Length': '193',
    'Expect': '100-continue',
    'Connection': 'Keep-Alive'
}

while(1):
    response = requests.post(url, headers=header,
                             json={"bizid": 1734, "dial_acct": "", "dltool": 0,
                                   "guid": "209a1d7e6c1e75551197075641e1adeb",
                                   "seckey": "1234dfje2ls", "signature": "sDPppeWGOyHzefmgnNUMj5PST6g=",
                                   "user_id": "jVQzRyg9LFFEGgRE6HtVnsH2y4WhWmIl"})
    print(response.status_code)
    print(response.json())
    time.sleep(1800)
