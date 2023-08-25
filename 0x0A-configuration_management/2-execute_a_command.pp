# executing he kill command

exec { 'killmenow':
  command => '/bin/pkill killmenow'
}
