# Redoing task #0 using puppet

exec { 'install nginx':
  path    => '/usr/bin',
  command => 'sudo apt update -y && sudo apt install nginx -y'
}

exec { 'create test directory':
  path    => '/usr/bin',
  command => 'sudo mkdir -p /data/web_static/releases/test/',
  require => Exec['install nginx']
}

$ind="<html>
	<head>
	</head>
	<body>
		Holberton School
  	</body>
</html>"

file { 'index.html':
  ensure  => 'file',
  path    => '/data/web_static/releases/test/index.html',
  content => $ind,
  require => Exec['create test directory']
}

exec { 'create shared directory':
  path    => '/usr/bin',
  command => 'sudo mkdir -p /data/web_static/shared',
  require => File['index.html']
}

exec { 'Remove Sym link for current file':
  path    => '/usr/bin',
  command => 'sudo rm -rf /data/web_static/current',
  require => Exec['create shared directory']
}

exec { 'Create Sym link for current file':
  path    => '/usr/bin',
  command => 'sudo ln -sf /data/web_static/releases/test /data/web_static/current',
  require => Exec['Remove Sym link for current file']
}

exec { 'Change ownership':
  path    => '/usr/bin',
  command => 'sudo chown -R ubuntu:ubuntu /data/',
  require => Exec['Create Sym link for current file']
}


$n_conf="
server {
       server_name _;

       location /hbnb_static/ {
       		alias /data/web_static/current/;
       }
}"

file { 'default file':
  ensure  => 'file',
  path    => '/etc/nginx/sites-enabled/default',
  content => $n_conf,
  require => Exec['Change ownership']
}

exec { 'Restart nginx':
  path    => '/usr/bin',
  command => 'sudo service nginx restart',
  require => File['default file']
}
