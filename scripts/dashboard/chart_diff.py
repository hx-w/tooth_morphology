# -*- coding: utf-8 -*-

import json
from quickchart import QuickChart


def generate_diff_chart(title: str, data_source: dict) -> str:
    '''
    @param see quickchart bar stack chart
    @return image url
    '''
    qc = QuickChart()
    qc.width = 500
    qc.height = 300
    qc.version = '2'

    _config = {
        'type': 'bar',
        'data': data_source,
        'options': {
            'title': { 
                'display': True,
                'text': title,
            },
            'tooltips': {
                'mode': 'index',
                'intersect': False,
            },
            'responsive': True,
            'scales': {
                'xAxes': [
                    {
                        'stacked': True,
                    },
                ],
                'yAxes': [
                    {
                        'stacked': True,
                    },
                ],
            },
        },
    }

    qc.config = json.dumps(_config)
    return qc.get_url()
