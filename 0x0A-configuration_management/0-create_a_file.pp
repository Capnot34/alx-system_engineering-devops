# This Puppet manifest creates a file with specific permissions,
# path, owner, group, and content.

file { '/tmp/school':
  ensure  => 'present',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
