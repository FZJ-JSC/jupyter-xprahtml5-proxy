from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, 'README.md'), 'r', encoding = 'utf-8') as fh:
    long_description = fh.read()

version='0.2.2'
setup(
    name = 'jupyter-xprahtml5-proxy',
    version = version,
    packages = find_packages(),

    url = 'https://github.com/FZJ_JSC/jupyter-xprahtml5-proxy',
    download_url = 'https://github.com/FZJ-JSC/jupyter-xprahtml5-proxy/archive/v{0}.tar.gz'.format(version),

    author = 'Jens Henrik Goebbert',
    author_email = 'j.goebbert@fz-juelich.de',

    description = 'Xpra for JupyterLab',
    long_description = long_description,
    long_description_content_type = 'text/markdown',

    keywords = ['jupyter', 'xpra', 'jupyterhub', 'jupyter-server-proxy'],
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Jupyter',
    ],

    entry_points = {
        'jupyter_serverproxy_servers': [
            'xprahtml5 = jupyter_xprahtml5_proxy:setup_xprahtml5',
        ]
    },
    install_requires = ['jupyter-server-proxy>=1.4.0'],
    include_package_data = True,
    zip_safe = False
)
