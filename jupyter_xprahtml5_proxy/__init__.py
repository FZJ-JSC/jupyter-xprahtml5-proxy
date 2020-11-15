import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel('INFO')

HERE = os.path.dirname(os.path.abspath(__file__))


def _xprahtml5_mappath(path):
    from getpass import getuser

    uri_parms = '?' + '&'.join([
        'username=' + getuser(),
        # 'password=' + _xprahtml5_passwd,
        # 'encryption=AES',
        # 'key=' + _xprahtml5_aeskey,
        # 'sharing=true',
    ])

    if path in ('/', '/index.html', ):
        path = '/index.html' + uri_parms
        logger.info('Xpra URI: ' + path)

    return path


def setup_xprahtml5():
    """ Setup commands and and return a dictionary compatible
        with jupyter-server-proxy.
    """
    from pathlib import Path
    from tempfile import gettempdir, mkstemp
    from random import choice
    from string import ascii_letters, digits

    global _xprahtml5_passwd, _xprahtml5_aeskey

    # password generator
    def _get_random_alphanumeric_string(length):
        letters_and_digits = ascii_letters + digits
        return (''.join((choice(letters_and_digits) for i in range(length))))

    # ensure a known secure sockets directory exists, as /run/user/$UID might not be available
    socket_path = os.path.join(gettempdir(), 'xpra_sockets_' + str(os.getuid()))
    Path(socket_path).mkdir(mode=0o700, parents=True, exist_ok=True)
    logger.info('Created secure socket directory for Xpra: ' + socket_path)

    # generate file with random one-time-password
    _xprahtml5_passwd = _get_random_alphanumeric_string(16)
    try:
        fd_passwd, fpath_passwd = mkstemp()
        logger.info('Created secure password file for Xpra: ' + fpath_passwd)

        with open(fd_passwd, 'w') as f:
            f.write(_xprahtml5_passwd)

    except Exception:
        logger.error("Passwd generation in temp file FAILED")
        raise FileNotFoundError("Passwd generation in temp file FAILED")

    # generate file with random encryption key
    _xprahtml5_aeskey = _get_random_alphanumeric_string(16)
    try:
        fd_aeskey, fpath_aeskey = mkstemp()
        logger.info('Created secure encryption key file for Xpra: ' + fpath_aeskey)

        with open(fd_aeskey, 'w') as f:
            f.write(_xprahtml5_aeskey)

    except Exception:
        logger.error("Encryption key generation in temp file FAILED")
        raise FileNotFoundError("Encryption key generation in temp file FAILED")

    # create command
    cmd = [
        os.path.join(HERE, 'share/launch_xpra.sh'),
        'start',
        '--html=on',
        '--bind-tcp=0.0.0.0:{port}',
        # '--socket-dir="' + socket_path + '/"',  # fixme: socket_dir not recognized
        # '--server-idle-timeout=86400',  # stop server after 24h with no client connection
        # '--exit-with-client=yes',  # stop Xpra when the browser disconnects
        '--start=xterm',
        # '--start-child=xterm', '--exit-with-children',
        # '--tcp-auth=file:filename=' + fpath_passwd,
        # '--tcp-encryption=AES',
        # '--tcp-encryption-keyfile=' + fpath_aeskey,
        '--clipboard-direction=both',
        '--no-bell',
        '--no-speaker',
        '--no-printing',
        '--no-microphone',
        '--no-notifications',
        '--dpi=96',
        # '--sharing',
    ]
    logger.info('Xpra command: ' + ' '.join(cmd))

    return {
        'environment': {  # as '--socket-dir' does not work as expected, we set this
            'XDG_RUNTIME_DIR': socket_path,
        },
        'command': cmd,
        'mappath': _xprahtml5_mappath,
        'absolute_url': False,
        'timeout': 30,
        'new_browser_tab': True,
        'launcher_entry': {
            'enabled': True,
            'icon_path': os.path.join(HERE, 'share/xpra-logo.svg'),
            'title': 'Xpra Desktop',
        },
    }
