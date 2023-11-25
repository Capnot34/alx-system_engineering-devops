# 1-install_a_package.pp

# Ensure 'python3-pip' is installed
package { 'python3-pip':
  ensure => installed,
}

# Install Flask version 2.1.0 using pip3
exec { 'install-flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  require => Package['python3-pip'],
}
