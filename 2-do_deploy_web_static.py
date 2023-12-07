#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers, using the function do_deploy
"""
from fabric.api import *
import os

env.user = "ubuntu"
env.hosts = ['54.237.64.177', '52.91.136.101']


def do_deploy(archive_path):
    """
    Upload the archive to the /tmp/ directory of the web server

    Uncompress the archive to the folder /data/web_static/releases/
    <archive filename without extension> on the web server

    Delete the archive from the web server

    Delete the symbolic link /data/web_static/current from the web server

    Create a new the symbolic link /data/web_static/current on the web server,
    linked to the new version of your code (/data/web_static/releases/
    <archive filename without extension>)

    Returns False if the file at the path archive_path doesn't exist
    """
    if !os.path.exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")

        new_path = archive_path.partition(".")[0]
        new_path = new_path.partition("/")[2]
        new_path = f"/data/web_static/releases/{new_path}/"
        run(f"mkdir -p {new_path}")

        run(f"tar -xzvf /tmp/{archive_path.split('/')[1]} -C {new_path}")

        run(f"rm /tmp/{archive_path.split('/')[1]}")

        run("rm -rf /data/web_static/current")

        run(f"mv {new_path}web_static/* {new_path}")
        run(f"rm -rf {new_path}web_static/")

        run(f"ln -s {new_path} /data/web_static/current")

        return True
    except Exception:
        return False
