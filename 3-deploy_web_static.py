#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py) that creates and
distributes an archive to your web servers, using the function deploy
"""
import os
from fabric.api import *
from datetime import datetime

env.user = "ubuntu"
env.hosts = ['54.237.64.177', '52.91.136.101']


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
        return (file_name)
    else:
        return None


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
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")

        new_path = archive_path.partition(".")[0]
        new_path = new_path.partition("/")[-1]
        new_path = f"/data/web_static/releases/{new_path}/"

        run(f"mkdir -p {new_path}")

        run(f"tar -xzvf /tmp/{archive_path.split('/')[1]} -C {new_path}")

        run(f"rm /tmp/{archive_path.split('/')[-1]}")

        run("rm -rf /data/web_static/current")

        run(f"mv {new_path}web_static/* {new_path}")
        run(f"rm -rf {new_path}web_static/")

        run(f"ln -s {new_path} /data/web_static/current")

        get(f"{new_path}", "/data/web_static/releases/")
        get("/data/web_static/current", "/data/web_static/")
        return True
    except Exception:
        return False


def deploy():
    """
    Call the do_pack() function and store the path of the created archive

    Return False if no archive has been created

    Call the do_deploy(archive_path) function, using the new path of the
    new archive

    Return the return value of do_deploy
    """
    archive_path = do_pack()
    if archive_path is None:
        return False

    print(archive_path)
    return do_deploy(archive_path)
