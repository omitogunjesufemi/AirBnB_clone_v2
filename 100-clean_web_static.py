#!/usr/bin/python3
"""
Fabric script (based on the file 3-deploy_web_static.py) that deletes
out-of-date archives, using the function do_clean
"""
from fabric.api import *
import os

env.user = "ubuntu"
env.hosts = ['54.237.64.177', '52.91.136.101']


def do_clean(number=0):
    """
    Delete all unnecessary archives (all archives minus the number to keep) in
    the versions folder
    Delete all unnecessary archives (all archives minus the number to keep) in
    the /data/web_static/releases folder of both of your web servers
    """
    with lcd("versions/"):
        ld = local("ls -l | wc -l", capture=True)
        t_f = int(ld.stdout) - 1
        num = int(number)
        if num == 0:
            num = 1
        while (t_f > num):
            f_n = local("ls | head -1", capture=True)
            f_name = str(f_n.stdout)
            local(f"find -type f -name '{f_name}' | xargs rm")
            t_f = t_f - 1

    with cd("/data/web_static/releases"):
        ld = run("ls -l | wc -l", capture=True)
        t_f = int(ld.stdout) - 1
        print(t_f)
        num = int(number)
        if num == 0:
            num = 1
        while (t_f > num):
            f_n = run("ls -tr | head -1", capture=True)
            f_name = str(f_n.stdout)
            sudo(f"find -type d -name '{f_name}' | xargs rm")
            t_f = t_f - 1
