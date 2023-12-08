#!/usr/bin/python3
"""Fabric script that distributes an archive to your web server
 using the function deploy"""

from fabric.api import *
from os import path
from datetime import datetime


env.hosts = ['54.152.59.218', '3.84.255.77']
env.user = 'ubuntu'


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


def do_deploy(archive_path):
    """Fabric script that distributes a compressed  archive to
    web servers"""

    if path.exists(archive_path):

        # ra_path(remote_archive path), rd_path (remote_deployment path)
        # Extract files from archive path
        archive = archive_path.split('/')[1]

        # Defining paths for the archive on the server
        ra_path = "/tmp/{}".format(archive)
        r_folder = archive.split('.')[0]
        rd_path = "/data/web_static/releases/{}/".format(r_folder)

        # Uploading the archive into the web server
        put(archive_path, ra_path)

        # Creating deployement folder on ws
        run("mkdir -p {}".format(rd_path))

        # Extracting the archive contents
        run("tar -xzf {} -C {}".format(ra_path, rd_path))

        # Removing the no longer needed uploaded archive
        run("rm {}".format(ra_path))

        # Moving contents from web_static subfolder to deployment folder
        run("mv -f {}web_static/* {}".format(rd_path, rd_path))

        # Then removing the empty web_static subfolder
        run("rm -rf {}web_static".format(rd_path))

        # Removing existing symbolic links
        run("rm -rf /data/web_static/current")

        # Creating a new symbolic link to the laterst version of code
        run("ln -s {} /data/web_static/current".format(rd_path))

        return True

    return False


def deploy():
    """reates and distributes an archive to your web servers,
    using the function deploy"""

    new_archive = do_pack()
    if new_archive is None:
        return False

    return do_deploy(new_archive)


def do_clean(number=0):
    """Deletes all out of date archives """

    files = local("ls -1t versions", capture=True)
    file_names = files.split("\n")
    n = int(number)
    if n in (0, 1):
        n = 1

    for i in file_names[n:]:
        local("rm versions/{}".format(i))

    dir_server = run("ls -1t /data/web_static/releases")
    dir_server_names = dir_server.split("\n")

    for i in dir_server_names[n:]:
        if i is 'test':
            continue
        run("rm -rf /data/web_static/releases/{}".format(i))
