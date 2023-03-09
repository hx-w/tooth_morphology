# -*- coding: utf-8 -*-

import os
from typing import Any
from abc import ABCMeta
from trimesh import Trimesh
import numpy as np

from logger import logger
from wraper import exception_handler


class BaseRule(metaclass=ABCMeta):

    @classmethod
    def __call__(cls, *args: Any) -> bool:
        ...


class Rule_Manifold(BaseRule):

    def __str__(self):
        return 'Rule: manifold'

    @classmethod
    @exception_handler
    def __call__(cls, mesh: Trimesh) -> bool:
        _nm = mesh.metadata["file_name"]
        logger.info(f'{_nm} => is_watertight: {mesh.is_watertight}')
        logger.info(f'{_nm} => is_winding_consistent: {mesh.is_winding_consistent}')
        logger.info(f'{_nm} => is_volume: {mesh.is_volume}')

        return (
            mesh.is_watertight and
            mesh.is_winding_consistent and
            mesh.is_volume
        )


class Rule_Centralized(BaseRule):
    __Threshold = 1e-3

    def __str__(self):
        return 'Rule: mesh center at origin'

    @classmethod
    @exception_handler
    def __call__(cls, mesh: Trimesh) -> bool:
        _nm = mesh.metadata["file_name"]
        logger.info(f'{_nm} => mesh centroid: {mesh.centroid}')
        return np.all(np.abs(mesh.centroid) < cls.__Threshold)


class Rule_Attachments(BaseRule):

    def __str__(self):
        return 'Rule: attachments available'

    @classmethod
    @exception_handler
    def __call__(cls, mesh: Trimesh) -> bool:
        _nm = mesh.metadata["file_name"]
        abs_path = mesh.metadata['file_path'].strip(_nm)

        _attatch_suffix = ['.tfm']
        _attatch_files = [
            f for f in os.listdir(abs_path)
            if os.path.splitext(f)[-1] in _attatch_suffix
        ]

        logger.info(f'{_nm} => attachments: {_attatch_files}')
        return len(_attatch_files) > 0

class Rule_DirectoryStructure(BaseRule):
    DATASETS_DIR = 'datasets'

    def __str__(self):
        return 'Rule: directory structure'

    @classmethod
    @exception_handler
    def __call__(cls, *args: Any) -> bool:
        '''
        1. no model at invalid dir
        2. all leaf dirs have at least one model
        '''
        def _is_valid_dir(dir: str) -> bool:
            return os.path.isdir(dir) and all(not f.endswith('obj') for f in os.listdir(dir))

        sec_level = filter(
            lambda x: os.path.isdir(os.path.join(cls.DATASETS_DIR, x)),
            os.listdir(cls.DATASETS_DIR)
        )
        sec_level = list(map(lambda x: os.path.join(cls.DATASETS_DIR, x), sec_level))
        logger.info(f'second level: {sec_level}')
        if any(not _is_valid_dir(d) for d in sec_level):
            return False
        
        third_level = [os.path.join(d, f) for d in sec_level for f in os.listdir(d)]
        third_level = list(filter(os.path.isdir, third_level))
        logger.info(f'third level: {third_level}')
        if any(_is_valid_dir(d) for d in third_level):
            return False

        return True
    

if __name__ == '__main__':
    print(Rule_DirectoryStructure.__call__())
