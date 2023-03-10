# -*- coding: utf-8 -*-

import re
import os
import subprocess
from typing import List
from wraper import exception_handler


class DiffFilesFetcher:
    _main_branch = 'master'
    _interested_files_patterns = [re.compile(r'.*obj')]

    @classmethod
    def _execute_shell_command(self, cmd: str) -> str:
        '''
        @param [cmd] shell command
        @return stdout of command to string
        '''
        return subprocess.check_output(cmd, shell=True).decode('utf-8')
    
    @classmethod
    @exception_handler
    def fetch(cls) -> List[str]:
        otps = cls._execute_shell_command(f'git diff --name-only origin/{cls._main_branch}')

        return list(filter(
            lambda f: (
                os.path.exists(f) and
                any([p.match(f) for p in cls._interested_files_patterns])
            ),
            otps.strip().split('\n')
        ))
