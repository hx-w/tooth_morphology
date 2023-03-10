# -*- coding: utf-8 -*-

import json
from quickchart import QuickChart


def generate_summary_chart(title: str, labels: list, datasets: list) -> str:
    '''
    @param see quickchart bar chart
    @return image url
    '''
    qc = QuickChart()
    qc.width = 500
    qc.height = 350
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
                    'anchor': 'end',
                    'align': 'top',
                    'color': '#fff',
                    'backgroundColor': 'rgba(34, 139, 34, 0.6)',
                    'borderColor': 'rgba(34, 139, 34, 1.0)',
                    'borderWidth': 1,
                    'borderRadius': 5,
                },
                "roundedBars": True 
            },
        },
    }

    qc.config = json.dumps(_config)
    return qc.get_url()
