# using puppet to make chnages to the default ssh config file
# so that one can connect to a server withough typing a password

#include lib

file_line { 'SSH Private Key':
	path               => '/etc/ssh/ssh_config',
	match              => '^\s*IdentityFile\s+~/.ssh/id_rsa$',
	replace            => true,
	append_on_no_match => true
}

file_line {'Deny Password Auth':
	path               => '/etc/ssh/ssh_config',
	line               => '    PasswordAuthentication no',
	match              => '^\s*PasswordAuthentication\s+(yes|no)$',
	replace            => true,
	append_on_no_match => true
}
