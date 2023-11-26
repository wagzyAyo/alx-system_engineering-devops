# ssh configuration file
file_line {'Set alias name':
    path  => '/etc/ssh/ssh_config',
    line  => 'Host 54.236.43.72
        HostName 54.236.43.72
        User ubuntu
        IdentifyFile ~/.ssh/school
        passwordAuthentication no',
}
