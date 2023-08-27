# puppet to create a config file

class ssh {
  $private_key_file = '~/.ssh/school'

  ssh_config {
    'default':
      identity_file => $private_key_file,
  }

  ssh_config {
    '*':
      password_authentication => 'no',
  }
}
