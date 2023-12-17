# puppet_install_nginx_web_server.pp

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  content => "
    server {
        listen 80;
        server_name _;

        location / {
            echo 'Hello World!';
        }

        location /redirect_me {
            return 301 https://www.example.com/redirected_page.html;
        }

        error_page 404 /404.html;
        location = /404.html {
            root /usr/share/nginx/html;
            internal;
            echo 'Ceci n\'est pas une page.';
        }
    }
  ",
}

# Restart Nginx
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}
