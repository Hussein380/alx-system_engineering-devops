# Puppet manifest to install Flask from pip3

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

