#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from datetime import datetime
from fabric.api import local
from os import path


def do_pack():
    """generates a tgz archive"""

    dt = datetime.utcnow()
    file_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                              dt.month,
                                                              dt.day,
                                                              dt.hour,
                                                              dt.minute,
                                                              dt.second)

    if path.isdir("versions") is False:
        local("mkdir -p versions")

    fab_stat = local("tar -cvzf {} web_static".format(file_name))

    if fab_stat.succeeded:
        file_size = path.getsize(file_name)

        print("web_static packed: {} -> {} Bytes".format(file_name, file_size))
        return file_name
    else:
        return None
