# 1-install_a_package.pp

package { 'python3-pip':
  ensure => present,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => '/usr/bin',
  require => Package['python3-pip'],
  notify  => Exec['update_bashrc'],
}

exec { 'update_bashrc':
  command => 'echo "export PATH=$PATH:/usr/local/bin" >> ~/.bashrc',
  path    => '/usr/bin',
  onlyif  => 'test -f ~/.bashrc',
  require => Exec['install_flask'],
}
