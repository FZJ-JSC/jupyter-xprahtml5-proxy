import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel('INFO')

HERE = os.path.dirname(os.path.abspath(__file__))


def get_xpra_executable(prog):
    from shutil import which

    # Find prog in known locations
    other_paths = [
        os.path.join('/opt/xpra/bin', prog),
    ]

    wp = os.path.join(HERE, 'bin', prog)
    if os.path.exists(wp):
        return wp

    if which(prog):
        return prog

    for op in other_paths:
        if os.path.exists(op):
            return op

    if os.getenv("XPRA_BIN") is not None:
        return os.getenv("XPRA_BIN")

    raise FileNotFoundError(f'Could not find {prog} in PATH')


def _xprahtml5_urlparams():
    url_params = '?sharing=true'

    return url_params


def _xprahtml5_mappath(path):

    # always pass the url parameter
    if path in ('/', '/index.html', ):
        url_params = _xprahtml5_urlparams()
        path = '/index.html' + url_params

    return path


def setup_xprahtml5():
    """ Setup commands and and return a dictionary compatible
        with jupyter-server-proxy.
    """
    from tempfile import mkdtemp

    # ensure a known secure sockets directory exists, as /run/user/$UID might not be available
    socket_path = mkdtemp(prefix='xpra_sockets_' + str(os.getuid()) + '_')
    logger.info('Created secure socket directory for Xpra: ' + socket_path)

    # launchers url file including url parameters
    path_info = 'xprahtml5/index.html' + _xprahtml5_urlparams()

    # create command
    cmd = [
        get_xpra_executable('xpra'),
        'start',
        '--html=on',
        '--bind={unix_socket},auth=none',  # using sockets + jupyter-server-proxy => auth is not needed here
        '--socket-dir=' + socket_path,
        '--start=xterm -fa "DejaVu Sans Mono" -fs 14',
        '--clipboard-direction=both',
        '--no-keyboard-sync',  # prevent keys from repeating unexpectedly on high latency
        '--no-mdns',  # do not advertise the xpra session on the local network
        '--no-bell',
        '--no-speaker',
        '--no-printing',
        '--no-microphone',
        '--no-notifications',
        '--no-dbus',
        '--no-systemd-run',  # do not delegated start-cmd to the system wide proxy server instance
        '--sharing',  # this allows to open the desktop in multiple browsers at the same time
        '--no-daemon',  # mandatory
    ]
    logger.info('Xpra command: ' + ' '.join(cmd))

    return {
        'environment': {
            'XDG_RUNTIME_DIR': socket_path,
        },
        'command': cmd,
        'unix_socket': socket_path + '/xpra-server',
        'mappath': _xprahtml5_mappath,
        'absolute_url': False,
        'timeout': 90,
        'new_browser_tab': True,
        'launcher_entry': {
            'enabled': True,
            'icon_path': os.path.join(HERE, 'icons/xpra-logo.svg'),
            'title': 'Xpra Desktop',
            'path_info': path_info,
        },
        'progressive': True,
    }
