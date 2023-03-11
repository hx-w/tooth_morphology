# -*- coding: utf-8 -*-

import json
from quickchart import QuickChart


def generate_summary_chart(title: str, labels: list, datasets: list) -> str:
    '''
    @param see quickchart bar chart
    @return image url
    '''
    qc = QuickChart()
    qc.width = 800
    qc.height = 500
    qc.version = '2'

    _config = {
        'type': 'bar',
        'data': {
            'labels': labels,
            'datasets': datasets,
        },
        'options': {
            'legend': {
                'display': False,
            },
            'stacked': True,
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
            'scales': {
                'xAxes': [
                    {
                        'display': True,
                        'scaleLabel': {
                            'display': True,
                            'labelString': 'Model types',
                        },
                        'ticks': {
                            'fontFamily': 'Mono'
                        }
                    },
                ],
                'yAxes': [
                    {
                        "ticks": {
                            'min': 0,
                            # 'max': max(datasets[0]['data']) + 5,
                            'fontFamily': 'Mono'
                        },
                        'display': True,
                        'scaleLabel': {
                            'display': True,
                            'labelString': 'Instance counts',
                        },
                    },
                ],
            },
        },
    }

    qc.config = json.dumps(_config)
    return qc.get_url()
