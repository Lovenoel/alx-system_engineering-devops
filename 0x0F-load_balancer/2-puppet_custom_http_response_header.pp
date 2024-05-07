# Setup New Ubuntu server with Nginx and add a custom HTTP header

# Update system package index
exec { 'update system':
  command => '/usr/bin/apt-get update',
}

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
  require => Exec['update system'],
}

# Create index.html with "Hello World!" content
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# Add a redirect rule to nginx configuration
exec { 'redirect_me':
  command  => 'sed -i "24i\    rewrite ^/redirect_me https://th3-gr00t.tk/ permanent;" /etc/nginx/sites-available/default',
  provider => 'shell',
  require  => Package['nginx'],
}

# Add custom HTTP header to nginx configuration
exec { 'HTTP header':
  command  => 'sed -i "25i\    add_header X-Served-By $hostname;" /etc/nginx/sites-available/default',
  provider => 'shell',
  require  => Exec['redirect_me'],
}

# Ensure nginx service is running
service { 'nginx':
  ensure  => 'running',
  require => Exec['HTTP header'],
}
