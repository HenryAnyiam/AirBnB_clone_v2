#!/usr/bin/python3
"""distributes an archive to the web servers, using the function do_deploy"""

from fabric.api import *
import os


env.hosts = ["ubuntu@3.86.7.132", "ubuntu@54.167.172.117"]
env.key_filename = "~/.ssh/school"


def do_deploy(archive_path):
    """deploy file to server

    Args:
        archive_path: path to file
    """
    env.hosts = ["ubuntu@3.86.7.132", "ubuntu@54.167.172.117"]
    if os.path.exists(archive_path):
        try:
            new_file = archive_path.split('/')[-1]
            new_path = "/tmp/" + new_file
            new_folder = "/data/web_static/releases/" + new_file.split('.')[0]
            put(archive_path, new_path)
            run(f"sudo mkdir -p {new_folder}")
            run(f"sudo tar -xzf {new_path} -C {new_folder}")
            run(f"sudo rm {new_path}")
            run(f"sudo mv -n {new_folder}/web_static/* {new_folder}")
            run(f"sudo rm -rf {new_folder}/web_static/")
            run("sudo rm -rf /data/web_static/current")
            run(f"sudo ln -s {new_folder} /data/web_static/current")
            print("New version deployed!")
            return True
        except Exception:
            return False
    else:
        return False
