# Set up server configuration with puppet
file_line{'Set alias name':
  path => '/etc/ssh/ssh_config',
  line => 'Host 54.205.163.79
    HostName 54.205.163.79
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no',
}
