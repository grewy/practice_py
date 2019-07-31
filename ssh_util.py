import paramiko

class Ssh(object):

  def __init__(self,ip,user="root", passwd="nutanix/4u"):
    self.ip = ip
    self.user = user
    self.passwd = passwd

  def run(self, command='/bin/true', bufsize=-1, key_filename='',
          timeout=120, port=22, pkey=None):
    """
    Excecutes a command using paramiko and returns the result.
    :param host: Host to connect
    :param port: The port number
    :param user: The username of the system
    :param command: The command to run
    :param key_filename: SSH private key file.
    :param pkey: RSAKey if we want to login with a in-memory key
    :return:
    """
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(hostname=self.ip, port=port,
                   username=self.user, password=self.passwd,
                   banner_timeout=10)

    chan = client.get_transport().open_session()
    chan.settimeout(timeout)
    chan.set_combine_stderr(True)
    chan.get_pty()

    chan.exec_command(command)
    stdout = chan.makefile('r', bufsize)
    stdout_text = stdout.read()
    status = int(chan.recv_exit_status())
    client.close()
    return stdout_text, status