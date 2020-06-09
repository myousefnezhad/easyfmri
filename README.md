easy fMRI project (V1.8B8500 beta)
==================================

### Introduction

Easy fMRI is an open source toolbox for the Human Brain Mapping and Decoding. This project is developing by [Muhammad Yousefnezhad](https://myousefnezhad.sourceforge.io), [iBRAIN Group](http://ibrain.nuaa.edu.cn), [Nanjing University of Aeronautics and Astronautics](http://iao.nuaa.edu.cn), China.

The project websites: 

[https://easyfmri.gitlab.io/](https://easyfmri.gitlab.io/) [preferred]

[https://easyfmri.github.io/](https://easyfmri.github.io/) 


Data repositories:

[https://easydata.gitlab.io](https://easydata.gitlab.io) [preferred]

[https://easyfmridata.github.io](https://easyfmridata.github.io)


### Dependencies

Easy fMRI needs following software:

  -Platform: Linux (recommended), Mac, Windows (via Linux Virtual Machine, or Bash for Windows 10 or above)

  -[Python3](https://anaconda.org/anaconda/python) (version=3.7.x)

  -[FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki) (version=5.0.1x or 6.0.0) for preprocessing steps

  -[AFNI & SUMA](https://afni.nimh.nih.gov/) (version=17.3.06 or above) for 3D visualization

  -[CUDA](https://developer.nvidia.com/cuda-toolkit) for GPU-based algorithms

  -[cuDNN](https://developer.nvidia.com/cudnn) for GPU-based algorithms

  -[PyTorch](https://pytorch.org/) for Gradient-based Optimization and Learning


## How to install easy fMRI

### Pre-install for Windows 10 users:

-- Install Windows Subsystem for Linux [https://docs.microsoft.com/en-us/windows/wsl/install-win10](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

NOTE: You have to install UBUNTU Linux from Windows Store.

-- Install Xming X Server for Windows: [https://sourceforge.net/projects/xming/files/latest/download](https://sourceforge.net/projects/xming/files/latest/download)

-- Open command prompt (press Windows key + R, then in run window type `cmd` and press enter)

-- Open bash via cmd:

```
bash
```

-- Set Display:

```
echo "export DISPLAY=:0.0" >> ~/.profile
source ~/.profile
```

Now you can install easy fMRI same as a linux system

#### STEP A) Copy Files

-- Download easy fMRI files:

From [GitLab](https://gitlab.com/easyfmri/easyfmri):

```
git clone https://gitlab.com/easyfmri/easyfmri.git  ~/.easyfmri
```

From [GitHub](https://github.com/easyfmri/easyfmri):

```
git clone https://github.com/easyfmri/easyfmri.git ~/.easyfmri
```

-- Apply easy fMRI environment: 

* Copy `ezfmri_scaled` and `ezfmri_scaled` to `/usr/local/bin`:
```
cd ~/.easyfmri/Script
./cp_script
```

* Set environment variables:

```
cd ~/.easyfmri/Script
./install_script_bashrc
source ~/.startupscript 
```
or
```
cd ~/.easyfmri/Script
./install_script_profile
source ~/.startupscript 
```

* Note 1: Since you did not install FSL and other related software, you may see some error on this stage such as `-bash: /usr/local/fsl/etc/fslconf/fsl.sh: No such file or directory`. Just skip them.


* Note 2: You must edit `~/.startupscript` and enable/disable different parameters based on your computer setting:
```
gedit ~/.startupscript
```
or
```
nano ~/.startupscript
```
or
```
vi ~/.startupscript
```

#### STEP B) Installing FSL 5.0.1x or 6.0.0

##### B.1) Installing FSL via [NeuroDebian](http://neuro.debian.net/) (For Debian or Ubuntu)

In `Get NeuroDebian` section, you must select Linux version and the closest resource location and then run the generated script. In `Select desired components`, you also must select `all software`.

For instance, this script for `Ubuntu 16.0.4` and `The University of Science and Technology of China (USTC)` is:
```
wget -O- http://neuro.debian.net/lists/xenial.cn-bj2.full | sudo tee /etc/apt/sources.list.d/neurodebian.sources.list
sudo apt-key adv --recv-keys --keyserver hkp://pool.sks-keyservers.net:80 0xA5D32F012649A5A9
sudo apt-get update
sudo apt install fsl-complete
```
and for `Ubuntu 18.0.4` and `The University of Science and Technology of China (USTC)` is:
```
wget -O- http://neuro.debian.net/lists/bionic.cn-bj2.full | sudo tee /etc/apt/sources.list.d/neurodebian.sources.list
sudo apt-key adv --recv-keys --keyserver hkp://pool.sks-keyservers.net:80 0xA5D32F012649A5A9
sudo apt-get update
sudo apt install fsl-complete
```

##### B.2) Installing FSL based on the [main source](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki)

-- Register on [FSL website](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki)

-- Download `fslinstaller.py`

-- Run following for downloading installation file (e.g. In version 6.0.0, the file name is `fsl-6.0.0-macOS_64.tar.gz` for Mac or `fsl-6.0.0-centos7_64.tar.gz` for all Linux distribution)

For Linux:
```
python2 fslinstaller.py -o
md5sum fsl-6.0.0-centos7_64.tar.gz
```

For Mac:
```
python2 fslinstaller.py -o
md5sum fsl-6.0.0-macOS_64.tar.gz
```

-- Install the downloaded file:

For Linux:
```
python2 fslinstaller.py -f fsl-6.0.0-centos7_64.tar.gz -M
export FSLDIR="/usr/local/fsl"
cd $FSLDIR/etc/fslconf
source fsl.sh
sudo ./install_fsleyes.sh
sudo ./make_applications_links.sh
sudo ./post_install.sh
```

For Mac:
```
python2 fslinstaller.py -f fsl-6.0.0-macOS_64.tar.gz -M
```

#### STEP D) Install AFNI 17.3.x or above

-- Download [AFNI](https://afni.nimh.nih.gov/):
* [Ubuntu 16+](https://afni.nimh.nih.gov/pub/dist/tgz/linux_ubuntu_16_64.tgz)
* [Ubuntu (<16), Fedora (< 21), Red Hat, etc.](https://afni.nimh.nih.gov/pub/dist/tgz/linux_openmp_64.tgz)
* [Fedora 21+](https://afni.nimh.nih.gov/pub/dist/tgz/linux_fedora_21_64.tgz)
* [Mac 10.7 (Lion) and higher](https://afni.nimh.nih.gov/pub/dist/tgz/macosx_10.7_Intel_64.tgz)


-- Extract AFNI to `~/abin`


##### Install linux packages for [AFNI](https://afni.nimh.nih.gov/pub/dist/doc/htmldoc/background_install/install_instructs/index.html)

-- Linux, Ubuntu 15.10 and earlier: The essential system setup
```
sudo apt-get install -y tcsh libxp6 xfonts-base python-qt4             \
                        libmotif4 libmotif-dev motif-clients           \
                        gsl-bin netpbm xvfb gnome-tweak-tool           \
                        libjpeg62 xterm gedit evince git
                        
                        
sudo apt-get install -y tcsh xfonts-base python-qt4 gedit evince       \
                        libmotif4 libmotif-dev motif-clients           \
                        gsl-bin netpbm xvfb gnome-tweak-tool libjpeg62
```

-- Linux, Ubuntu 16.04 - 17.10: The essential system setup
```
sudo apt-get install -y tcsh xfonts-base python-qt4       \
                        gsl-bin netpbm gnome-tweak-tool   \
                        libjpeg62 xvfb xterm vim curl     \
                        gedit evince                      \
                        libglu1-mesa-dev libglw1-mesa     \
                        libxm4 build-essential git


sudo apt-get install -y gnome-terminal nautilus          \
                        gnome-icon-theme-symbolic
```

--  Linux, Ubuntu 18.04: The essential system setup
```
sudo apt-get install -y tcsh xfonts-base python-qt4       \
                        gsl-bin netpbm gnome-tweak-tool   \
                        libjpeg62 xvfb xterm vim curl     \
                        gedit evince                      \
                        libglu1-mesa-dev libglw1-mesa     \
                        libxm4 build-essential            \
                        libcurl4-openssl-dev libxml2-dev  \
                        libssl-dev libgfortran3 git
  
                        
sudo apt-get install -y gnome-terminal nautilus          \
                        gnome-icon-theme-symbolic
```


-- Fedora 21 (and higher): The essential system setup
```
sudo yum install -y tcsh libXp openmotif gsl xorg-x11-fonts-misc       \
                    PyQt4 R-devel netpbm-progs gnome-tweak-tool ed     \
                    xorg-x11-server-Xvfb git
sudo yum update -y
```


-- CentOS/RHEL 7: The essential system setup
```
sudo yum install -y epel-release
sudo yum install -y tcsh libXp openmotif gsl xorg-x11-fonts-misc       \
                    PyQt4 R-devel netpbm-progs gnome-tweak-tool ed     \
                    libpng12 xorg-x11-server-Xvfb git
sudo yum update -y
```

#### STEP D) Install Python 3.7.x

-- Download [Anaconda3](https://anaconda.org/anaconda/python) for Python 3.7

* [Linux](https://www.anaconda.com/download/#linux)
* [Mac](https://www.anaconda.com/download/#macos)

Note: In Windows 10, you must install the linux version of Anaconda 3

-- Install Python 3.7

For Linux:

```
sh Anaconda3-<version>-Linux<platform>.sh
```

For Mac: click PKG file and continue installation.

Note 1: If you need to change the main repository of `pip`, then:
* Creating the `~/.pip` directory by using `mkdir ~/.pip`
* Then generate the setting file `~/.pip/pip.conf`. For instance, following setting can change the main repository to `The University of Science and Technology of China`:
```
[global]
timeout = 60
index-url  = https://mirrors.ustc.edu.cn/pypi/web/simple/

[install]
index-url = https://mirrors.ustc.edu.cn/pypi/web/simple/
```

Note 2: If you need to change the main repository of `conda`, then create setting file `~/.condarc`. For instance, following setting can change the main repository to `The University of Science and Technology of China`:
```
channels:
  - https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
  - https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
  - defaults
ssl_verify: true
show_channel_urls: true
```

-- Load environment variables: 
```
source ~/.startupscript
```

-- Update Conda Components: 
```
conda update --all
```

-- Update `pip`: 
```
pip install -U pip
```

-- Install `mpi4py`:
```
conda install -c conda-forge mpi4py
```

-- Install easy fMRI required python packages by using: 
```
pip install -U future nibabel nitime nilearn pyqode.core pyqode.qt pydicom
```

-- Install [PyTorch](https://pytorch.org/) package:

For CPU version:

In Mac OS:
```
conda install pytorch torchvision -c pytorch
```

In Linux:
```
conda install pytorch-cpu torchvision-cpu -c pytorch
```

For GPU Vesion: You must install [CUDA 10](https://developer.nvidia.com/cuda-toolkit) and [cuDNN 7.4.1](https://developer.nvidia.com/cudnn). Then, you can install [PyTorch](https://pytorch.org/)

```
conda install pytorch torchvision cudatoolkit=10.0
```

#### STEP E) Run easy fMRI

After restarting your computer, open a terminal and run easyfmri:

```
ezfmri
```

For computers with HiDPI display run following or just enable option in `~/.startupscript`.
```
ezfmri_scaled
```

### How to manually upgrade easy fMRI

For updating a new version, just replace the old files with the new files.

Note: default directory for easy fMRI is a hidden folder in `~/.easyfmri`

```
rm -rf ~/.easyfmri
git clone https://gitlab.com/easyfmri/easyfmri.git ~/.easyfmri
```


### How to uninstall easy fMRI

```
rm -rf ~/.easyfmri
```