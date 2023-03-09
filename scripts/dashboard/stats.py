# -*- coding: utf-8 -*-

import os
from typing import List

DATASETS_DIR = 'datasets'

def generate_labels() -> List[str]:
    '''
    @return list of labels
    '''
    return list(filter(
        lambda x: os.path.isdir(os.path.join(DATASETS_DIR, x)),
        os.listdir(DATASETS_DIR)
    ))

def count_label(label: str) -> int:
    '''
    @param label
    @return number of files in label
    '''
    def _target_valid(dir: str) -> bool:
        '''must be a obj file in the dir
        '''
        if not os.path.isdir(dir): retur False
        return len([f for f in os.listdir(dir) if f.endswith('.obj')])

    _base = os.path.join(DATASETS_DIR, label)
    valid_dirs = [d for d in os.listdir(_base) if _target_valid(os.path.join(_base, d))]
    return len(valid_dirs)

def generate_status() -> dict:
    labels = generate_labels()
    counts = [count_label(label) for label in labels]

    return {'labels': labels, 'counts': counts}

