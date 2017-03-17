# Using strace find out why Apache returning a 500 error.
exec { 'typo' :
  path    => '/bin/',
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php"
}
