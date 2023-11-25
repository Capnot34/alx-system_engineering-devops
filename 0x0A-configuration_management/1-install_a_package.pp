# This Puppet manifest installs flask from pip3
exec { 'install-flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
}
