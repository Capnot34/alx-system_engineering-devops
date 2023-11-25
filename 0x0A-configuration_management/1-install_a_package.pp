# This Puppet manifest installs Flask version 2.1.0 using pip3

# Install Flask package
package { 'flask':
  ensure   => '2.1.0',    # Ensure the Flask package is version 2.1.0
  provider => '/usr/bin/pip3',  # Use pip3 as the package provider
}

# Install Python3 package
package { 'python3':
  ensure   => 'installed',   # Ensure Python3 is installed
  provider => '/usr/bin/python3',  # Use python3 as the package provider
}

