# -*- coding: utf-8 -*-

'''
decorators for exception handling
'''

import functools
from logger import logger

def exception_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f'{func} Exception: {e}')
            return False
    return wrapper
