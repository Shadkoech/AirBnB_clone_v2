# Puppet lint that automates the deployment of web_static

# Install Nginx if not installed
package { 'nginx':
  ensure => installed,
}

# Create directories
file { '/data/':
  ensure => 'directory',
}

file { '/data/web_static/':
  ensure => 'directory',
}

file { '/data/web_static/releases/':
  ensure => 'directory',
}

file { '/data/web_static/shared/':
  ensure => 'directory',
}

file { '/data/web_static/releases/test/':
  ensure => 'directory',
}

# Creating fake HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => 'Kotech here we go',
}

# Creating symbolic link
file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test/',
  require => File['/data/web_static/releases/test/'],
}

# Giving ownership to the ubuntu user and group
file { '/data/':
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

# Updating Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => '
    server {
        listen 80;
        listen [::]:80 default_server;
        add_header X-Served-By $hostname;
        root   /var/www/html;
        index  index.html index.htm index.nginx-debian.html;

        location /hbnb_static {
            alias /data/web_static/current;
            index index.html index.htm;
        }

        location /redirect_me {
            return 301 https://www.github.com/Shadkoech/;
        }

        error_page 404 /404.html;
        location /404 {
          root /etc/nginx/html;
          internal;
        }
    }
  ',
  require => Package['nginx'],
}

# Restarting Nginx
service { 'nginx':
  ensure    => 'running',
  subscribe => File['/etc/nginx/sites-available/default'],
}
