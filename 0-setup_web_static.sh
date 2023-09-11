#!/usr/bin/env bash
#set up web server for deployment of web_static
#install nginx
apt-get -y update
apt-get -y  install nginx
#create folders
content="\
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "$content" > /data/web_static/releases/test/index.html

#creat symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

#change file ownership
chown -R ubuntu:ubuntu /data/

#serve the content of /data/web_static/current/ to hbnb_static
sed -i '/server_name _;/a \\n\tlocation \/hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tindex index.html index.htm;\n\t}' /etc/nginx/sites-available/default
service nginx restart
