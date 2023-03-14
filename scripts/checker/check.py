# -*- coding: utf-8 -*-

'''
Check merging changes (PR) to master branch.
'''

import os
from typing import List
from fetcher import DiffFilesFetcher
from logger import logger
from rules import (
    BaseRule,
    Rule_Manifold, Rule_Centralized,
    Rule_Attachments, Rule_DirectoryStructure,
    Rule_Orientation
)
import trimesh

NEED_COMMIT = False

def check_file(filepath: str, rules: List[BaseRule]) -> bool:
    '''
    @param [filename] file path
    @return True if file is valid, otherwise False
    '''
    global NEED_COMMIT
    logger.info(f'checking file: {filepath}')
    mesh = trimesh.load(filepath)
    older_num = mesh.vertices.shape[0]
    mesh.remove_unreferenced_vertices()
    if older_num != mesh.vertices.shape[0]:
        logger.info(f'{mesh.metadata["file_name"]} => Remove unreferenced vertices')
        mesh.export(filepath)
        NEED_COMMIT = True

    return all([rule.__call__(mesh) for rule in rules])


if __name__ == '__main__':
    rules = [
        Rule_Manifold,
        # Rule_Centralized,
        # Rule_Attachments,
        # Rule_Orientation
    ]

    files = DiffFilesFetcher.fetch()

    logger.info(f'files to check: {files}')

    if Rule_DirectoryStructure.__call__() and \
        all([check_file(f, rules) for f in files]):

        logger.info('==> PR check passed <==')
    else:
        logger.error('xxxx PR check failed xxxx')
        raise Exception('PR check failed')

    if NEED_COMMIT:
        logger.info('==> Need post commit <==')
        os.system('git config --local user.name "github-actions[bot]"')
        os.system('git config --local user.email "github-actions[bot]@users.noreply.github.com"')
        os.system('git add .')
        os.system('git commit -m "Remove unreferenced vertices"')
