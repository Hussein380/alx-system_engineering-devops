# update the system repository

exec { 'update system':
        command => '/usr/bin/apt-get update',
}

# Install nginx package
package { 'nginx':
        ensure  => 'installed',
        require => Exec['update system'],
}
# Create an index.html file with "Hello World!" content
file {'/var/www/html/index.html':
        content => 'Hello World!',
}

# Add a redirect rule to nginx configuration file
exec {'redirect_me':
        command  => 'sed -i "24i\    rewrite ^/redirect_me https://th3-gr00t.tk/ permanent;" /etc/nginx/sites-available/default',
        provider => 'shell',
}

# Add a custom HTTP header to nginx configuration file
exec {'HTTP header':
        command  => 'sed -i "25i\    add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
        provider => 'shell',
}

# Ensure nginx service is running
service {'nginx':
        ensure => running,
        require => Package['nginx'],
}
