# -*- coding: utf-8 -*-

from stats import generate_status
from chart_bar import generate_chart_bar
from dump import update_chart_url

if __name__ == '__main__':
    label_counts = generate_status()

    bar_datasets = [{
        'label': 'dataset elements counts',
        "backgroundColor": 'rgb(75, 192, 192)',
        "borderWidth": 1,
        "data": label_counts['counts']
    }]

    bar_url = generate_chart_bar(
        'dataset summary',
        label_counts['labels'],
        bar_datasets
    )

    update_chart_url('summary', bar_url)

