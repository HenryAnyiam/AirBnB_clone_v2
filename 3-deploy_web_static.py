#!/usr/bin/python3
"""creates and distributes an archive to my web servers"""

from fabric.api import *
import os
from datetime import datetime
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


env.hosts = ["ubuntu@3.86.7.132", "ubuntu@54.167.172.117"]
env.key_filename = "~/.ssh/school"


def deploy():
    output_file = do_pack()
    if output_file is not None:
        return do_deploy(output_file)
    else:
        return False
