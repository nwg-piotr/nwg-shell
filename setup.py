import os

from setuptools import setup, find_packages


def read(f_name):
    return open(os.path.join(os.path.dirname(__file__), f_name)).read()


setup(
    name='nwg-shell',
    version='0.3.7',
    description='GTK3-based shell for sway Wayland compositor',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "": ["skel/stuff/*",
             "skel/config/nwg-bar/*",
             "skel/config/nwg-dock/*",
             "skel/config/nwg-drawer/*",
             "skel/config/nwg-panel/*",
             "skel/data/nwg-look/*",
             "skel/config/sway/*",
             "skel/config/swaync/*",
             "skel/config/foot/*",
             "skel/config/gtklock/*",
             "skel/*"]
    },
    url='https://github.com/nwg-piotr/nwg-shell',
    license='MIT',
    author='Piotr Miller',
    author_email='nwg.piotr@gmail.com',
    python_requires='>=3.6.0',
    install_requires=[],
    entry_points={
        'gui_scripts': [
            'nwg-shell = nwg_shell.main:main',
            'nwg-shell-installer = nwg_shell.installer:main',
            'nwg-shell-check-updates = nwg_shell.check_updates:main'
        ]
    }
)
