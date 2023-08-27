# puppet to create a config file

class ssh {
  $private_key_file = '~/.ssh/school'

  # Configure the SSH client to use the private key
  ssh_config {
    'default':
      identity_file => $private_key_file,
  }

  # Refuse to authenticate using a password
  ssh_config {
    '*':
      password_authentication => 'no',
  }
}
