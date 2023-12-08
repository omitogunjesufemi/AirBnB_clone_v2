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
    if number <= 1:
        pass
    else:
        pass
