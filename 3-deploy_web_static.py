#!/usr/bin/python3
"""creates and distributes an archive to my web servers"""

from fabric.api import *
import os
from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy
from datetime import datetime


env.hosts = ["ubuntu@3.86.7.132", "ubuntu@54.167.172.117"]
env.key_filename = "~/.ssh/school"


def deploy():
    output_file = do_pack
    if output_file != None;
