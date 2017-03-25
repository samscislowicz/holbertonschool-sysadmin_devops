# Using strace find out why Apache returning a 500 error.
exec { 'sed' :
     path => '/bin/',
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
}
