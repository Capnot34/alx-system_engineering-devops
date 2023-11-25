#This code installs the packet puppet-lint
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
