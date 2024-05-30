#!/usr/bin/env python

from setuptools import setup

readme = open("README.rst").read()
history = open("HISTORY.rst").read()

setup(name="ds4drv",
      version="1.0",
      description="A Sony DualShock 4 driver for Linux",
      url="https://github.com/gothboiprncss/ds4drv-fixed",
      author="gothboiprncss aka based god",
      author_email="gbp@mol.gb",
      license="MIT",
      long_description=readme + "\n\n" + history,
      entry_points={
        "console_scripts": ["ds4drv=ds4drv.__main__:main"]
      },
      packages=["ds4drv",
                "ds4drv.actions",
                "ds4drv.backends",
                "ds4drv.packages"],
      install_requires=["python-setuptools" "bluez-utils"  "bluez-deprecated-tools" "python-evdev" "python-pyudev"],
      classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Topic :: Games/Entertainment"
      ]
)

