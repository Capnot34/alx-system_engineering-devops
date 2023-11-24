# 2-execute_a_command.pp

# Define the command to kill the process using pkill
exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => '/usr/bin',
  logoutput   => true,
  refreshonly => true,
}

# Ensure the process is started initially
exec { 'start_killmenow':
  command => '/bin/bash -c "while true; do sleep 2; done"',
  path    => '/bin',
  creates => '/usr/bin/killmenow',
  require => Exec['killmenow'],
}
