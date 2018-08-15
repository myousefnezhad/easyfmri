easy fMRI project (V1.8B4200 beta)
==================================

### Introduction

Easy fMRI is an open source toolbox for the Human Brain Mapping and Decoding. This project is developing by [Muhammad Yousefnezhad](https://myousefnezhad.sourceforge.io), [iBRAIN Group](http://ibrain.nuaa.edu.cn), [Nanjing University of Aeronautics and Astronautics](http://iao.nuaa.edu.cn), China.

The project website is [https://easyfmri.github.io/](https://easyfmri.github.io/) or [https://easyfmri.sourceforge.io/](https://easyfmri.sourceforge.io/).

### Dependencies

Easy fMRI needs following software:

  -Platform: Linux (recommended), Mac, Windows (via Linux Virtual Machine, or Bash for Windows 10 or above)

  -[Python3](https://anaconda.org/anaconda/python) (version=3.6.2 or above)

  -[FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki) (version=5.0.10 or above) for preprocessing steps

  -[AFNI & SUMA](https://afni.nimh.nih.gov/) (version=17.3.06 or above) for 3D visualization

  -[CUDA](https://developer.nvidia.com/cuda-toolkit) for GPU-based algorithms

  -[CUDNN](https://developer.nvidia.com/cudnn) for GPU-based algorithms

  -[Tensorflow](https://www.tensorflow.org/install/) for Gradient-based Optimization and Learning 


### How to install easy fMRI

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

From [GitHub](https://github.com/easyfmri/easyfmri):

```
git clone https://github.com/easyfmri/easyfmri.git ~/.easyfmri
```

From [SourceForge Git](https://sourceforge.net/p/easyfmri/code/ci/master/tree/):

```
git clone git://git.code.sf.net/p/easyfmri/code ~/.easyfmri
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


#### STEP B) Install FSL 5.0.10 or above

-- Register on [FSL website](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki)

-- Download `fslinstaller.py`

-- Run following for downloading installation file (e.g. In version 5.0.10, the file name is `fsl-5.0.10-macOS_64.tar.gz` for Mac or `fsl-5.0.10-centos7_64.tar.gz` for all Linux distribution)

For Linux:

```
python2 fslinstaller.py -o
md5sum fsl-5.0.10-centos7_64.tar.gz
```

For Mac:


```
python2 fslinstaller.py -o
md5sum fsl-5.0.10-macOS_64.tar.gz
```

-- Install the downloaded file:

For Linux:

```
python2 fslinstaller.py -f fsl-5.0.10-centos7_64.tar.gz -M
```

For Mac:

```
python2 fslinstaller.py -f fsl-5.0.10-macOS_64.tar.gz -M
```

-- Set environment variables (see example at the end)


#### STEP D) Install AFNI 17.3.06 or above

-- Download [AFNI](https://afni.nimh.nih.gov/)

-- Extract AFNI to `~/abin`

-- Set environment variables (see example at the end)

NOTE: For Ubuntu-based Linux, you have to install following packages:
```
sudo apt-get install -y tcsh xfonts-base python-qt4 gsl-bin netpbm gnome-tweak-tool libjpeg62 xvfb xterm vim curl

sudo apt-get install -y libglu1-mesa-dev libglw1-mesa libxm4 build-essential
```


#### STEP D) Install Python 3.6.x

-- Download [Anaconda3](https://anaconda.org/anaconda/python) and Install Python3 by using Anaconda3

For Linux:

```
sh Anaconda3-<version>-Linux<platform>.sh
```

For Mac: click PKG file and continue installation.

-- Set environment variables (see example at the end)

-- Install all packages in `~/.easyfmri/PyPackage` directory

```
cd ~/.easyfmri/PyPackage
pip install *
```

-- Install MPI packages:

```
conda install mpi4py
```

-- Install Tensorflow package:

For CPU version:

```
pip install tensorflow
```

For GPU Vesion: You must install [CUDA](https://developer.nvidia.com/cuda-toolkit) and [CuDNN](https://developer.nvidia.com/cudnn). Then, you can install [Tensorflow](https://www.tensorflow.org/install/)

Note: By employing `CUDA 9.0`, `CUDNN 7.0` and `Ubuntu 16.04.x`, you can use following command to install tensorflow:

```
pip install tensorflow-gpu
```


#### STEP E) Run easy fMRI

After restarting your computer, open a terminal and run easyfmri:

```
ezfmri
```

### How to upgrade easy fMRI

For updating a new version, just replace the old files with the new files.

Note: default directory for easy fMRI is a hidden folder in `~/.easyfmri`

```
rm -R ~/.easyfmri
git clone https://github.com/easyfmri/easyfmri.git ~/.easyfmri
```


### An example of environment variables

You can install this script automatically as follows:

For Linux:
```
cd ~/.easyfmri/Script
./install_script_linux
```

For Mac:
```
cd ~/.easyfmri/Script
./install_script_mac
```

Or just copy following to in `.profile` or `.bashrc` and restart your computer

```
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
export EN_MC="1"
export EN_COLOR="1"
######################################
# Directories                        #
######################################
export INSTALL_DIR="$HOME"      # Base dir for Anaconda, easy fMRI, and AFNI
export FSLDIR="/usr/local/fsl"  # for FSL 5.0.10
export ANACON_PATH="$INSTALL_DIR/anaconda3/bin"
export AFNI_PATH="$INSTALL_DIR/abin"
export CUDA_HOME="/usr/local/cuda"
# export FSLDIR="/usr/share/fsl/5.0" # for FSL 5.0.9
# export DISPLAY=:0.0 # Enable for Windows 10
######################################
# Scripts                            #
######################################

######## Easy fMRI
if (( $EN_EZFMRI != "0" )); then
  export EASYFMRI="$INSTALL_DIR/.easyfmri"
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
  export LD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:$CUDA_HOME/lib:/usr/local/cuda/lib64/"
  export PATH="$CUDA_HOME/bin:$PATH"
fi
####### BASH
if (( $EN_BASH != "0" )); then
  [ -f /usr/local/etc/bash_completion ] && . /usr/local/etc/bash_completion
fi
####### MC
if (( $EN_MC != "0" )); then
  alias mc=". /usr/local/opt/midnight-commander/libexec/mc/mc-wrapper.sh"
fi
####### BASH COLOR
if (( $EN_COLOR != "0" )); then
  # Define Colors
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
  # Set Terminal Colors
  export CLICOLOR=1
  export LSCOLORS=GxacCxDxBxegedabagaced
  alias ls='ls -GFh'
  export PS1="\n$C_LIGHTPURPLE\u$C_DEFAULT@$C_LIGHTCYAN\h$C_DEFAULT:$C_LIGHTBLUE\W$C_DEFAULT\$$C_LIGHTYELLOW "
  if (( $EUID != 0 )); then
    export LSCOLORS=GxacCxDxBxegedabagaced
    export PS1="\n$C_LIGHTGREEN\u$C_DEFAULT@$C_LIGHTCYAN\h$C_DEFAULT:$C_LIGHTBLUE\W$C_DEFAULT\$$C_LIGHTYELLOW "
  fi
fi
```