#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ["3.90.80.220", "54.157.143.192"]

def do_deploy(archive_path):
    """Distributes an archive"""
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"

        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}{}/".format(path, no_ext))
        run("tar -xzf /tmp/{} -C {}{}/".format(file_name, path, no_ext))
        run("sudo rm /tmp/{}".format(file_name))
        run("sudo mv {0}{1}/web_static/* {0}{1}/".format(path, no_ext))
        run("sudo rm -rf {}{}/web_static".format(path, no_ext))
        run("sudo rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path, no_ext))

        print("*** New version deployed! ***")
        return True
    except:
        return False
