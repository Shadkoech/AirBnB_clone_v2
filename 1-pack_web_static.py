#!/usr/bin/python3
"""Fabric script generating a .tgz archive from files
in the web_static folder of AirBnB clone repo"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """A function that compresses the files in web_static folder
    into an archive before they can be sent """

    local("mkdir -p versions")

    current_dt = datetime.now()
    time_stamp = current_dt.strftime("%Y%m%d%H%M%S")
    archive_file = "web_static_{}.tgz".format(time_stamp)
    archive_path = "versions/{}".format(archive_file)

    compress_result = local("tar -cvzf {} web_static".format(archive_path))

    if compress_result.succeeded:
        return archive_path
    else:
        return None
