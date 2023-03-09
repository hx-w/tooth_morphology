# -*- coding: utf-8 -*-

import json
from quickchart import QuickChart


def generate_chart_bar(title: str, labels: list, datasets: list) -> str:
    '''
    @param see quickchart bar chart
    @return image url
    '''
    qc = QuickChart()
    qc.width = 500
    qc.height = 300
    qc.version = '2'

    _config = {
        'type': 'bar',
        'data': {
            'labels': labels,
            'datasets': datasets,
        },
        'options': {
            'title': { 
                'display': True,
                'text': title,
            },
            'plugins': {
                'datalabels': {
                    'anchor': 'center',
                    'align': 'center',
                    'color': '#666',
                    'font': {
                        'weight': 'normal',
                    },
                },
                "roundedBars": True 
            },
        },
    }

    qc.config = json.dumps(_config)
    return qc.get_url()
