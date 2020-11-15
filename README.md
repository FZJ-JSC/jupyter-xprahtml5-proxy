![build](https://github.com/FZJ-JSC/jupyter-xprahtml5-proxy/workflows/build/badge.svg)

# jupyter-xprahtml5-proxy
Integrate Xpra in your Jupyter environment for an fast, feature-rich and easy to use remote desktop in the browser.

## Requirements
- Python 3.6+
- Jupyter Notebook 6.0+
- JupyterLab 2.1+

This package executes the `xpra` command. This command assumes the `xpra` command is available in the environment's PATH.


### Xpra
[Xpra](https://xpra.org/) is an open-source multi-platform persistent *remote display* solution for forwarding applications and desktop screens. It allows you to run X11 programs, usually on a remote host, and direct their display to your local machine.  
Best of it. It is fast, fast, fast and comes with a build-in html5 client to allow remote.

### Jupyter-Server-Proxy
[Jupyter-Server-Proxy](https://jupyter-server-proxy.readthedocs.io) lets you run arbitrary external processes (such as Xpra-HTML5) alongside your notebook, and provide authenticated web access to them.

## Install 

#### Create and Activate Environment
```
virtualenv -p python3 venv
source venv/bin/activate
```

#### Install jupyter-xprahtml5-proxy
```
pip install git+https://github.com/FZJ-JSC/jupyter-xprahtml5-proxy.git
```

#### Enable jupyter-xprahtml5-proxy Extensions
For Jupyter Classic, activate the jupyter-server-proxy extension:
```
jupyter serverextension enable --sys-prefix jupyter_server_proxy
```

For Jupyter Lab, install the @jupyterlab/server-proxy extension:
```
jupyter labextension install @jupyterlab/server-proxy
jupyter lab build
```

#### Start Jupyter Classic or Jupyter Lab
Click on the Xpra icon from the Jupyter Lab Launcher or the Xpra item from the New dropdown in Jupyter Classic.  
Connect to your database as instructed in the Quickstart section.

## Configuration
This package calls `xpra` with a bunch of settings. Please read the [Xpra manual](https://xpra.org/manual.html) if you want to now the details.  
You have to modify `setup_xprahtml5()` in `jupyter_xprahtml5_proxy/__init__.py` for change.

## Credits
- Xpra
- jupyter-server-proxy

## License
BSD 3-Clause
