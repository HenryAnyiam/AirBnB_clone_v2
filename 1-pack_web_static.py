#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static folder of the
AirBnB Clone repo, using the function do_pack."""

from fabric.api import *
import os
from datetime import datetime


@runs_once
def do_pack():
    """archive the webstatic directory"""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    date = datetime.now()
    output_file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            date.year, date.month, date.day,
            date.hour, date.minute, date.second)
    try:
        print(f"Packing web_static to {output_file}")
        local(f"tar -czvf {output_file} web_static")
        size = os.path.getsize(output_file)
        print(f"web_static packed: {output_file} -> {size}Bytes")
    except Exception:
        output_file = None
    return output_file
