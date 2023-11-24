# 1-install_a_package.pp

# Ensure python3-pip is installed
package { 'python3-pip':
  ensure => present,
}

# Install Flask version 2.1.0
package { 'Flask':
  ensure  => '2.1.0',
  require => Package['python3-pip'],
}
