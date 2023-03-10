# -*- coding: utf-8 -*-

from stats import (
    fetch_model_types,
    generate_model_counts,
    get_PR_ids,
    fetch_PR_diff,
    generate_diff_data
)

from chart_summary import generate_summary_chart
from chart_diff import generate_diff_chart

from dump import update_chart_url


def update_summary():
    model_types = generate_model_counts()
    bar_datasets = [{
        'label': 'dataset elements counts',
        "backgroundColor": 'rgba(54, 162, 235, 0.5)',
        "borderWidth": 1,
        "data": model_types['counts']
    }]
    url = generate_summary_chart(
        'dataset summary',
        model_types['labels'],
        bar_datasets
    )
    update_chart_url('summary', url)


def update_diff():
    model_types = fetch_model_types()
    data_pr = get_PR_ids()

    stats = fetch_PR_diff(model_types, data_pr)

    data_source = generate_diff_data(model_types, data_pr, stats)

    url = generate_diff_chart('dataset updates', data_source)
    update_chart_url('diff', url)

if __name__ == '__main__':
    print('==> updating summary chart')
    update_summary()
    print('==> updating diff chart')
    update_diff()