# Create a manifest that kills a process named killmenow

exec { 'killmenow':
  path        => ['/bin', '/usr/bin'] # Specify the path to pkill
  command     => 'pkill -f killmenow',
  refreshonly => 'true',
}
