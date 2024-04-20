# Create a manifest that kills a process named killmenow

exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => ['/bin', '/usr/bin'] # Specify the path to pkill
  refreshonly => 'true',
}
