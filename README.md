
# Fixed version of [ds4drv](https://github.com/chrippa/ds4drv)
This repo provides a fixed and debugged version of an almost 8 year old package [ds4drv](https://github.com/chrippa/ds4drv).



## Dependencies
```bash
sudo pacman -S python-setuptools bluez-utils  bluez-deprecated-tools python-evdev python-pyudev
```
_Those packages will be installed by setup.py_

## Installation
Then run the installer:
```bash
git clone https://github.com/gothboiprncss/ds4drv-fixed.git
cd ds4drv-fixed
sudo python setup.py install
```
To allow ds4drv access to uinput run:
```bash
sudo nudevadm control --reload-rules
sudo rmmod uinput
sudo modprobe uinput
```
## Usage

```bash
ds4drv
```
Then press and hold the PS button on your conntroller.
If it will connects successfully, you should be good to go! 

_**Remeber to not close the terminal while using the program!**_
