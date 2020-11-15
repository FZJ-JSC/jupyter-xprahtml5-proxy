from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, "README.md"), "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="jupyter-xprahtml5-proxy",
    packages=find_packages(),
    version='0.2.1',

    author_email="j.goebbert@fz-juelich.de",
    description="Xpra for JupyterLab",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FZJ_JSC/jupyter-xprahtml5-proxy",

    keywords=["jupyter", "xpra", "jupyterhub", "jupyter-server-proxy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Jupyter",
    ],

    entry_points={
        'jupyter_serverproxy_servers': [
            'xprahtml5 = jupyter_xprahtml5:setup_xprahtml5',
        ]
    },
    install_requires=['jupyter-server-proxy>=1.4.0'],
    include_package_data=True,
    zip_safe=False
)
