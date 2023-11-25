# This Puppet manifest installs Flask version 2.1.0 using pip3

# Install Flask package
package { 'flask':
  ensure   => '2.1.0',    # Ensure the Flask package is version 2.1.0
  provider => 'pip3',      # Use pip3 as the package provider
}

# Install Python3 package using the system's package manager
package { 'python3':
  ensure   => 'installed',   # Ensure Python3 is installed
  provider => 'apt',         # Use apt as the package provider
}

# Install puppet-lint gem
package { 'puppet-lint':
  ensure   => '2.1.0',    # Ensure puppet-lint is version 2.1.0
  provider => 'gem',       # Use gem as the package provider
}
