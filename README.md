easy fMRI project (V1.8B6100 beta)
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

  -[FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki) (version=5.0.1x) for preprocessing steps

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

From [SourceForge](https://sourceforge.net/projects/easyfmri/files/) as a zip file
```
unzip easyfMRI.<version>.zip
mv easyfmri .easyfmri
```


-- Copy `ezfmri` to `/usr/bin/local`

```
cd ~/.easyfmri/Script
./cp_script
```

-- Set environment variables (see example at the end)


#### STEP B) Installing FSL 5.0.1x

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

-- Run following for downloading installation file (e.g. In version 5.0.10, the file name is `fsl-5.0.11-macOS_64.tar.gz` for Mac or `fsl-5.0.11-centos7_64.tar.gz` for all Linux distribution)

For Linux:
```
python2 fslinstaller.py -o
md5sum fsl-5.0.11-centos7_64.tar.gz
```

For Mac:
```
python2 fslinstaller.py -o
md5sum fsl-5.0.11-macOS_64.tar.gz
```

-- Install the downloaded file:

For Linux:
```
python2 fslinstaller.py -f fsl-5.0.11-centos7_64.tar.gz -M
```

For Mac:
```
python2 fslinstaller.py -f fsl-5.0.11-macOS_64.tar.gz -M
```

-- Set environment variables (see example at the end).


#### STEP D) Install AFNI 17.3.x or above

-- Download [AFNI](https://afni.nimh.nih.gov/):
* [Ubuntu 16+](https://afni.nimh.nih.gov/pub/dist/tgz/linux_ubuntu_16_64.tgz)
* [Ubuntu (<16), Fedora (< 21), Red Hat, etc.](https://afni.nimh.nih.gov/pub/dist/tgz/linux_openmp_64.tgz)
* [Fedora 21+](https://afni.nimh.nih.gov/pub/dist/tgz/linux_fedora_21_64.tgz)
* [Mac 10.7 (Lion) and higher](https://afni.nimh.nih.gov/pub/dist/tgz/macosx_10.7_Intel_64.tgz)


-- Extract AFNI to `~/abin`

-- Set environment variables (see example at the end)

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

-- Set environment variables (see example at the end)

-- Load environment variables: `source ~/.startupscript`

-- Update Conda: `conda update --all`

-- Update `pip`: `pip install -U pip`


-- Install `MPICH`, `OpenMPI`, and then `MPI4PY`:

For Ubuntu:
```
sudo apt install libmpich-dev libopenmpi-dev
env MPICC=/usr/bin pip install mpi4py
```

For Fedora: 
```
sudo dnf install openmpi openmpi-devel mpich mpich-devel
echo 'export PATH="/usr/lib64/openmpi/bin:/usr/lib64/mpich/bin:$PATH"' >> ~/.bashrc 
export PATH="/usr/lib64/openmpi/bin:/usr/lib64/mpich/bin:$PATH"
source ~/.bashrc 
env MPICC=/usr/lib64/openmpi/bin pip install mpi4py
```

For RedHat or CentOS: 
```
sudo yum install openmpi openmpi-devel mpich mpich-devel
echo 'export PATH="/usr/lib64/openmpi/bin:/usr/lib64/mpich/bin:$PATH"' >> ~/.bashrc 
export PATH="/usr/lib64/openmpi/bin:/usr/lib64/mpich/bin:$PATH"
source ~/.bashrc 
env MPICC=/usr/lib64/openmpi/bin pip install mpi4py
```

For Mac:
```
conda install mpi4py
```

-- Install Easy fMRI python packages by using `pip install -U future nibabel pyqode.core pyqode.qt`

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

For GPU Vesion: You must install [CUDA](https://developer.nvidia.com/cuda-toolkit) and [cuDNN](https://developer.nvidia.com/cudnn). Then, you can install [PyTorch](https://pytorch.org/)

Note: By employing `CUDA 9.2`, `CUDNN 7.2.1`, you can use following command to install PyTorch:

```
conda install pytorch torchvision cuda92 -c pytorch
```


#### STEP E) Run easy fMRI

After restarting your computer, open a terminal and run easyfmri:

```
ezfmri
```

### How to manually upgrade easy fMRI

For updating a new version, just replace the old files with the new files.

Note: default directory for easy fMRI is a hidden folder in `~/.easyfmri`

```
rm -R ~/.easyfmri
git clone https://gitlab.com/easyfmri/easyfmri.git ~/.easyfmri
```


### An example of environment variables

You can install this script automatically as follows:

```
cd ~/.easyfmri/Script
./install_script_bashrc
```
or
```
cd ~/.easyfmri/Script
./install_script_profile
```

Or just copy following to in `.profile` or `.bashrc` and restart your computer

```
# For installing this script:
# 1. copy this file to home directory
# 2. Enable/Disable the features
# 3. Set the installation directory
# 4. Run following command for Linux:
# echo "source ~/.startupscript" >> ~/.bashrc
# for Mac:
# echo "source ~/.startupscript" >> ~/.profile

######################################
# Enable ("1") or Disable ("0") features #
######################################
export EN_EZFMRI="1"
export EN_PYTHON="1"
export EN_PYTHON_ALIAS="1"
export EN_AFNI="1"
export EN_FSL="1"
export EN_CUDA="1"
export EN_BASH="1"
export EN_MC="0"
export EN_COLOR="1"
export EN_SCALE="0"  # Turn it on for OLED display, default is 200x
export EN_GIT="1"
export EN_AENV="1"
export RUN_AENV="0"
######################################
# Proxy for terminal                 #
######################################
alias proxyon='export http_proxy=http://127.0.0.1:3213 && export https_proxy=http://127.0.0.1:3213'
alias proxyoff='export http_proxy= && export https_proxy='
######################################
# Directories & Parameters           #
######################################
export INSTALL_DIR="$HOME"      # Base dir for Anaconda, easy fMRI, and AFNI
export FSLDIR="/usr/local/fsl"  # for FSL 5.0.1x
export ANACON_PATH="$INSTALL_DIR/anaconda3/bin"
export AFNI_PATH="$INSTALL_DIR/abin"
export CUDA_HOME="/usr/local/cuda"
export SCREEN_SCALE=2     # Set it for OLED display, 2 means 200x
# export FSLDIR="/usr/share/fsl/5.0" # for FSL 5.0.9
# export DISPLAY=:0.0 # Enable for Windows 10
######################################
# Scripts                            #
######################################

######## Easy fMRI
if (( $EN_EZFMRI != "0" )); then
  export EASYFMRI="$INSTALL_DIR/.easyfmri"
fi

######## QT Scale Factor
if (( $EN_SCALE != "0" )); then
    export QT_SCALE_FACTOR=1
    export QT_AUTO_SCREEN_SCALE_FACTOR=0
    export QT_SCREEN_SCALE_FACTORS=$SCREEN_SCALE
fi

######## Python
if (( $EN_PYTHON != "0" )); then
  export PATH="$ANACON_PATH:$PATH"
fi
if (( $EN_PYTHON_ALIAS != "0" )); then
  alias python="python -m IPython"
  alias python3="python -m IPython"
fi
######## AFNI
if (( $EN_AFNI != "0" )); then
  export DYLD_LIBRARY_PATH=/opt/X11/lib/flat_namespace
  export DYLD_FALLBACK_LIBRARY_PATH="$HOME/abin"
  export PATH="/usr/local/bin:$AFNI_PATH:$PATH"
fi
####### FSL
if (( $EN_FSL != "0" )); then
  . $FSLDIR/etc/fslconf/fsl.sh
  export PATH="$FSLDIR/bin:$PATH"
fi
####### CUDA
if (( $EN_CUDA != "0" )); then
  export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:$CUDA_HOME/lib"
  export LD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:$CUDA_HOME/lib:/usr/local/cuda/lib64"
  export PATH="$CUDA_HOME/bin:$PATH"
  export CPLUS_INCLUDE_PATH=$CPLUS_INCLUDE_PATH:/usr/local/cuda/samples/common/inc
fi

####### BASH
if (( $EN_BASH != "0" )); then
  [ -f /usr/local/etc/bash_completion ] && . /usr/local/etc/bash_completion
fi
####### MC
if (( $EN_MC != "0" )); then
  alias mc=". /usr/local/opt/midnight-commander/libexec/mc/mc-wrapper.sh"
fi
####### Define Colors
  C_DEFAULT="\[\033[m\]"
  C_WHITE="\[\033[1m\]"
  C_BLACK="\[\033[30m\]"
  C_RED="\[\033[31m\]"
  C_GREEN="\[\033[32m\]"
  C_YELLOW="\[\033[33m\]"
  C_BLUE="\[\033[34m\]"
  C_PURPLE="\[\033[35m\]"
  C_CYAN="\[\033[36m\]"
  C_LIGHTGRAY="\[\033[37m\]"
  C_DARKGRAY="\[\033[1;30m\]"
  C_LIGHTRED="\[\033[1;31m\]"
  C_LIGHTGREEN="\[\033[1;32m\]"
  C_LIGHTYELLOW="\[\033[1;33m\]"
  C_LIGHTBLUE="\[\033[1;34m\]"
  C_LIGHTPURPLE="\[\033[1;35m\]"
  C_LIGHTCYAN="\[\033[1;36m\]"
  C_BG_BLACK="\[\033[40m\]"
  C_BG_RED="\[\033[41m\]"
  C_BG_GREEN="\[\033[42m\]"
  C_BG_YELLOW="\[\033[43m\]"
  C_BG_BLUE="\[\033[44m\]"
  C_BG_PURPLE="\[\033[45m\]"
  C_BG_CYAN="\[\033[46m\]"
  C_BG_LIGHTGRAY="\[\033[47m\]"

###### Anaconda envs
if (( $EN_AENV != "0" )); then
env_var=""
## Activate env (default env = base)
aenv() {

    if [ -z $1 ];
    then
        ENV="base"
    else
        ENV="${1}"
    fi

    source activate ${ENV}

    env_var="${ENV}"
}

## Deactivate env
denv() {
    source deactivate
    env_var=""
}

## Information env
ienv() {
    if [[ ${env_var} == "" ]]
    then
        echo ""
    else
        echo "${env_var}"
    fi
}
fi

####### Git Prompt
if (( $EN_GIT != "0" )); then
parse_git_branch() {
 git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}

git_info() {
   echo "$(parse_git_branch)"
}
fi


####### BASH SETUP
if (( $EN_COLOR != "0" )); then
  export PS1=""
# Set Terminal Colors
  export CLICOLOR=1
  alias ls='ls -GFh'
  export LSCOLORS=GxacCxDxBxegedabagaced
# Root User
  if (( $EUID != 0 )); then
    export LSCOLORS=GxacCxDxBxegedabagaced
    export PS1+="$C_LIGHTGREEN\u$C_DEFAULT@$C_LIGHTCYAN\h$C_DEFAULT:$C_LIGHTBLUE\W"
  else
    export PS1+="$C_LIGHTPURPLE\u$C_DEFAULT@$C_LIGHTCYAN\h$C_DEFAULT:$C_LIGHTBLUE\W"
  fi
  if (( $EN_GIT != "0" )); then
# Git Information
    PS1+='\[\033[01;31m\]$(parse_git_branch)'
  fi
# Prompot Symbol
  PS1+="$C_DEFAULT\$$C_LIGHTYELLOW "
fi

####### Run Anaconda env in startup
if (( $RUN_AENV != "0" )); then
  aenv
fi
```
