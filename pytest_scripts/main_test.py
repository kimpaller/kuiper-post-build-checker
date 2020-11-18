import pytest
import testinfra

def test_passwd_file(host):
    passwd = host.file("/etc/passwd")
    assert passwd.contains("root")
    assert passwd.contains("analog")
    assert passwd.user == "root"
    assert passwd.group == "root"
    assert passwd.mode == 0o644

def test_bashrc_file(host):
    passwd = host.file("/home/analog/.bashrc")
    assert passwd.contains("PYTHONPATH")

@pytest.mark.parametrize("name", [
    "libgdk-pixbuf2.0-dev",
    "libssl-dev",
    "libgtk2.0-dev",
    "gnuradio-dev",
    "libxml2",
    "libxml2-dev",
    "bison",
    "flex",
    "cmake",
    "git",
    "libaio-dev",
    "libboost-all-dev",
    "swig",
    "g++",
    "libboost-all-dev",
    "libgmp-dev",
    "python3-numpy",
    "python3-mako",
    "python3-sphinx",
    "python3-lxml",
    "python3-pyqt5",
    "python3-yaml",
    "python3-click",
    "python3-click-plugins",
    "python3-zmq",
    "python3-scipy",
    "python3-cheetah",
    "python3-lxml",
    "doxygen",
    "libfftw3-dev",
    "libsdl1.2-dev",
    "libgsl-dev",
    "libqt5opengl5-dev",
    "liblog4cpp5-dev",
    "libzmq3-dev",
    "libpthread-stubs0-dev",
    "sdcc",
    "guile-2.2-dev",
    "ccache",
    "libpython3.7-dev",
    "libcppunit-dev",
    "libboost1.67-dev",
    "libgsl0-dev",
    "libusb-dev",
    "alsa-base",
    "libasound2",
    "libasound2-dev",
    "libxml2-dev",
    "libxml2",
    "libpython3-all-dev",
    "libfftw3-bin",
    "libfftw3-3",
    "liblog4cpp5v5",
    "liblog4cpp5-dev",
    "autoconf",
    "libzip4",
    "libzip-dev",
    "libglib2.0-dev",
    "libsigc++-2.0-dev",
    "libglibmm-2.4-dev",
    "qt5-default",
    "qttools5-dev",
    "qttools5-dev-tools",
    "curl",
    "libgmp-dev",
    "libqt5svg5-dev",
    "libmatio-dev",
    "liborc-0.4-dev",
    "qtdeclarative5-dev",
    "locate",
    "libzmq3-dev",
    "gnuplot",
    "xterm",
    "libusb-1.0"
])
def test_packages(host, name):
    pkg = host.package(name)
    assert pkg.is_installed

@pytest.mark.parametrize("name", [
   "iiod"
])
def test_service(host, name):
    service = host.service(name)
    assert service.is_running