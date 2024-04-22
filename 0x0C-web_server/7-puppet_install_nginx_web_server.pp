# Update system package lists
exec { 'update system':
  command => '/usr/bin/apt-get update',
}

# Install Nginx package
package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system'],
}

# Create a simple HTML file
file {'/var/www/html/index.html':
  content => 'Hello World!',
}

# Configure Nginx to redirect /redirect_me to a YouTube video
exec {'redirect_me':
  command  => 'sed -i "24i\    rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
  provider => 'shell',
}

# Ensure Nginx service is running
service {'nginx':
  ensure => running,
  require => Package['nginx'],
}
