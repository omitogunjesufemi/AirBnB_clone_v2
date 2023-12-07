#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

nginx_exist=$(sudo service nginx status 2>&1 >/dev/null)
if [ "$nginx_exist" ]
then
    sudo apt-get update -y
    sudo apt-get upgrade -y
    sudo apt-get install nginx -y
fi

sudo mkdir -p /data/web_static/releases/test/

# Creating a fake HTML file with simple context to test Nginx
ind="<html>
	<head>
	</head>
	<body>
		Holberton School
  	</body>
</html>"

echo "$ind" | sudo tee /data/web_static/releases/test/index.html

sudo mkdir -p /data/web_static/shared

# Creating Symbolic link
sudo rm -rf /data/web_static/current
#sudo mkdir -p /data/web_static/current
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Give ownership of /data folder to the user and his group
sudo chown -R "ubuntu":"ubuntu" /data/

# Update the Nginx configuration to serve static content
n_conf="
server {
       server_name _;

       location /hbnb_static/ {
       		alias /data/web_static/current/;
       }
}"

echo "$n_conf" | sudo tee -a /etc/nginx/sites-enabled/default

# Restart nginx server
sudo service nginx restart
