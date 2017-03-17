# create a file in /tmp.
file { '/tmp/holberton':
ensure => 'present',
content => 'I love Puppet',
group => 'www-data',
owner => 'www-data',
mode => '0744'
}