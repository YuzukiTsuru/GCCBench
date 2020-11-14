import shlex
import subprocess

from .get_time import get_time
from utils.color_static import *


def command_runner(shell_cmd: str, stage=PROCESS, thread_num=0) -> int:
    cmd = shlex.split(shell_cmd)
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # Main stdout
    while p.poll() is None:
        line = p.stdout.readline()
        line = str(line.strip(), encoding="utf-8")
        if line:
            if thread_num is 0:
                print('{} | {} |: [{}]\r'.format(get_time(), stage, line))
            else:
                print('{} | {} | {} |: [{}]\r'.format(get_time(), stage, thread_num, line))
    if p.returncode is 0:
        print(SUCCESS)
        return 0
    else:
        print(FAIL)
        return -1
