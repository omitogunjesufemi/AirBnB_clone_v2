#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from datetime import datetime
from fabric.api import *


def do_pack():
    """All files in the folder web_static must be added to the final archive

    All archives must be stored in the folder versions (your function should
    create this folder if it doesn't exist)

    The name of the archive created must be:
        web_static_<year><month><day><hour><minute><second>.tgz

    The function do_pack must return the archive path if the archive has
    been correctly generated. Otherwise, it should return None
    """
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(now)
    local("mkdir -p versions/")
    x = local(f"tar -cvzf {file_name} web_static")
    if x.succeeded:
        return ("versions/{}".format(file_name))
    else:
        return None
