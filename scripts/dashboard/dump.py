# -*- coding: utf-8 -*-

import os
import requests

def update_chart_url(chart_type: str, chart_url: str):
    # read env
    TOKEN = os.environ['TOKEN']
    API = os.environ['API']

    resp = requests.post(API, json={
        'token': TOKEN,
        'chart_type': chart_type,
        'chart_url': chart_url,
    })

    if resp.status_code != 200:
        print(resp.content.decode('utf-8'))
        raise Exception('update failed')
    
    print('update success')

