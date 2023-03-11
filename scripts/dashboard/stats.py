# -*- coding: utf-8 -*-

import os
from typing import List, Dict
import datetime

import requests
import seaborn as sns


TOKEN = os.environ['TOKEN']

DATASETS_DIR = 'datasets'

def fetch_model_types() -> List[str]:
    '''
    @return list of labels
    '''
    return list(filter(
        lambda x: os.path.isdir(os.path.join(DATASETS_DIR, x)),
        os.listdir(DATASETS_DIR)
    ))

def count_model_types(label: str) -> int:
    '''
    @param label
    @return number of files in label
    '''
    def _target_valid(dir: str) -> bool:
        '''must be a obj file in the dir
        '''
        if not os.path.isdir(dir): return False
        return len([f for f in os.listdir(dir) if f.endswith('.obj')])

    _base = os.path.join(DATASETS_DIR, label)
    valid_dirs = [d for d in os.listdir(_base) if _target_valid(os.path.join(_base, d))]
    return len(valid_dirs)

def generate_model_counts() -> dict:
    labels = fetch_model_types()
    counts = [count_model_types(label) for label in labels]

    return {'labels': labels, 'counts': counts}

def get_PR_ids() -> Dict[str, int]: # {date: id}
    try:
        resp = requests.get(
            'https://api.github.com/repos/hx-w/tooth_morphology/pulls',
            params={'state': 'closed', 'direction': 'asc'},
            auth=('hx-w', TOKEN)
        )
        if resp.status_code != 200:
            raise Exception('get PR ids failed')
        
        valid_pr_info = list(filter(lambda x: x['merged_at'] is not None, resp.json()))
        dates = list(map(
            lambda x: datetime.datetime.strptime(
                x['merged_at'], '%Y-%m-%dT%H:%M:%SZ'
            ).date().strftime('%Y-%m-%d'),
            valid_pr_info
        ))
        valid_pr_number = list(map(lambda x: x['number'], valid_pr_info))

        date_pr = {}
        for date, pr in zip(dates, valid_pr_number):
            if date not in date_pr:
                date_pr[date] = []
            date_pr[date].append(pr)  
        return date_pr

    except Exception as e:
        print(f'Error: {e}')
        return {}

def fetch_PR_diff(interest_types: List[str], data_pr: Dict[str, str]) -> dict:
    '''
    @return {
        date: {
            model_type: {
                addition: int,
                deletion: int,
                total: int,
            }
        }
    }
    '''

    stats= {}

    for date, prs in data_pr.items():
        stats[date] = {}
        for pr in prs:
            # request GitHub api
            resp = requests.get(
                f'https://api.github.com/repos/hx-w/tooth_morphology/pulls/{pr}/files',
                auth=('hx-w', TOKEN)
            )
            if resp.status_code != 200:
                print('get PR diff failed: ', pr)
                continue
            
            add_or_delete = list(filter(
                lambda x: (
                        x['status'] in ['added', 'removed', 'modified'] and
                        x['filename'].endswith('.obj') and
                        len(x['filename'].split('/')) > 1 and
                        x['filename'].split('/')[1] in interest_types
                    ),
                    resp.json()
            ))

            for item in add_or_delete:
                model_type = item['filename'].split('/')[1]
                if model_type not in stats[date]:
                    stats[date][model_type] = {
                        'addition': 0,
                        'deletion': 0,
                        'total': 0,
                    }
                if item['status'] == 'added':
                    stats[date][model_type]['addition'] += 1
                    stats[date][model_type]['total'] += 1
                elif item['status'] == 'removed':
                    stats[date][model_type]['deletion'] -= 1
                    stats[date][model_type]['total'] -= 1
                else:
                    stats[date][model_type]['addition'] += 1
                    stats[date][model_type]['deletion'] -= 1

    return stats


def generate_diff_data(interest_types: List[str], date_pr: Dict[str, int], stats: dict) -> dict:
    # colors = sns.color_palette("husl", len(interest_types))
    colors = sns.hls_palette(len(interest_types), l=.3, s=.8)
    raw_colors = list(map(lambda x: f'rgba({int(x[0] * 255)}, {int(x[1] * 255)}, {int(x[2] * 255)}, 0.8)', colors))
    weak_colors = list(map(lambda x: f'rgba({int(x[0] * 255)}, {int(x[1] * 255)}, {int(x[2] * 255)}, 0.4)', colors))

    data_source = {
        'labels': list(date_pr.keys()),
        'datasets': []
    }

    for i, model_type in enumerate(interest_types):
        ''' addition, deletion, total
        '''
        # total
        data_total = list(map(
            lambda date: stats[date][model_type]['total'] if model_type in stats[date] else 0,
            date_pr.keys()
        ))
        data_source['datasets'].append({
            'type': 'line',
            'label': f'{model_type} - Total',
            'borderColor': raw_colors[i].replace('0.8', '1.0'),
            'data': data_total,
            'fill': False,
        })

        # addition
        data_addition = list(map(
            lambda date: stats[date][model_type]['addition'] if model_type in stats[date] else 0,
            date_pr.keys()
        ))
        data_source['datasets'].append({
            'type': 'bar',
            'label': f'- Addition',
            'backgroundColor': raw_colors[i],
            'data': data_addition,
            'stack': model_type
        })

        # deletion
        data_deletion = list(map(
            lambda date: stats[date][model_type]['deletion'] if model_type in stats[date] else 0,
            date_pr.keys()
        ))
        data_source['datasets'].append({
            'type': 'bar',
            'label': f'- Deletion',
            'backgroundColor': weak_colors[i],
            'data': data_deletion,
            'stack': model_type
        })


    return data_source


if __name__ == '__main__':
    # test diff

    model_types = fetch_model_types()
    data_pr = get_PR_ids()

    stats = fetch_PR_diff(model_types, data_pr)

    data_source = generate_diff_data(model_types, data_pr, stats)

    from chart_diff import generate_diff_chart

    url = generate_diff_chart('datasets updates', data_source)
    print(url)
