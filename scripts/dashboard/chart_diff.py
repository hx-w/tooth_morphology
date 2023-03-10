# -*- coding: utf-8 -*-

import json
from quickchart import QuickChart


def generate_diff_chart(title: str, data_source: dict) -> str:
    '''
    @param see quickchart bar stack chart
    @return image url
    '''
    qc = QuickChart()
    qc.width = 600
    qc.height = 400
    qc.version = '2'

    _config = {
        'type': 'bar',
        'data': data_source,
        'options': {
            'legend': {
                'labels': {
                    'fontSize': 15,
                    # 'fontStyle': 'bold',
                    'fontColor': '#404040',
                    'padding': 8,
                },
                'align': 'start'
            },
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
            'scales': {
                'xAxes': [
                    {
                        'display': True,
                        'scaleLabel': {
                            'display': True,
                            'labelString': 'Dates with changes',
                        },
                        'ticks': {
                            'fontFamily': 'Consolas'
                        }
                    },
                ],
                'yAxes': [
                    {
                        'display': True,
                        'scaleLabel': {
                            'display': True,
                            'labelString': 'Instance changes',
                        },
                        'ticks': {
                            'fontFamily': 'Consolas'
                        }
                    },
                ],
            },
        },
    }

    qc.config = json.dumps(_config)
    return qc.get_url()
