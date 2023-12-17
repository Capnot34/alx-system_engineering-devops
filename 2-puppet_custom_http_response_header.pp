# Puppet manifest to configure a custom HTTP header

class custom_http_response_header {
  package { 'nginx':
    ensure => 'installed',
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    mode    => '0644',
    content => "server {\n\tadd_header X-Served-By $hostname;\n\tlocation / {\n\t\tproxy_pass http://127.0.0.1:80;\n\t}\n}\n",
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure => 'running',
    enable => true,
  }
}

include custom_http_response_header
