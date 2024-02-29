import os

from setuptools import setup, find_packages


def read(f_name):
    return open(os.path.join(os.path.dirname(__file__), f_name)).read()


setup(
    name='nwg-shell',
    version='0.5.33',
    description='GTK3-based shell for sway Wayland compositor',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "": ["skel/stuff/*",
             "skel/config/nwg-bar/*",
             "skel/config/nwg-dock/*",
             "skel/config/nwg-dock-hyprland/*",
             "skel/config/nwg-drawer/*",
             "skel/config/nwg-panel/*",
             "skel/config/nwg-look/*",
             "skel/data/nwg-look/*",
             "skel/data/nwg-shell-config/*",
             "skel/config/sway/*",
             "skel/config/hypr/*",
             "skel/config/swaync/*",
             "skel/config/foot/*",
             "skel/config/gtklock/*",
             "skel/config/gtk-3.0/*",
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
