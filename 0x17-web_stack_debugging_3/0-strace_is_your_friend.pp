#Fix Apache is returning a 500 error.

file { '/var/www/html/wp-settings.php':
  ensure => file,
  notify => Exec['replace_wp_settings'],
}

exec { 'replace_wp_settings':
  command     => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path        => '/bin:/usr/bin',
  refreshonly => true,
  subscribe   => File['/var/www/html/wp-settings.php'],
}
