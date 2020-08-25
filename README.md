easy fMRI project (V1.8B8888 beta)
==================================

# Introduction

Easy fMRI is an open source toolbox for the Human Brain Mapping and Decoding — _i.e._, we analyze task-based and rest-mode fMRI datasets by using advanced machine learning approaches.
This project is developing by [Tony Yousefnezhad](https://myousefnezhad.gitlab.io/), [University of Albera](https://www.ualberta.ca), Canada.


* The project websites: 

    * [https://easyfmri.gitlab.io/](https://easyfmri.gitlab.io/) [preferred]

    * [https://easyfmri.github.io/](https://easyfmri.github.io/) 


* Data repositories:

    * [https://easydata.gitlab.io](https://easydata.gitlab.io) [preferred]

    * [https://easyfmridata.github.io](https://easyfmridata.github.io)


# Dependencies

Easy fMRI needs following software:

  * Platform: Linux (recommended), Mac, Windows (via Linux Virtual Machine, or Windows WSL)
  
    * Note: easy fMRI is natively developed on the last version of [Fedora](https://getfedora.org/) 
  
  * [Python3](https://anaconda.org/anaconda/python) (version=3.8.x [preferred] or 3.7.x)

  * [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki) (version=6.0.x [preferred] or 5.0.1x) for preprocessing steps

  * [AFNI & SUMA](https://afni.nimh.nih.gov/) (version=17.3.06 or above) for 3D visualization

  * [PyTorch](https://pytorch.org/) for Deep Learning and Gradient-based Optimization


# How to install easy fMRI

## Pre-install for Windows 10 users:

* Install Windows Subsystem for Linux [https://docs.microsoft.com/en-us/windows/wsl/install-win10](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

    * Note: You have to install UBUNTU Linux from Windows Store.

* Install Xming X Server for Windows: [https://sourceforge.net/projects/xming/files/latest/download](https://sourceforge.net/projects/xming/files/latest/download)

* Open command prompt (press Windows key + R, then in run window type `cmd` and press enter)

* Open bash via cmd:
    ```
    bash
    ```

* Set Display:
    ```
    echo "export DISPLAY=:0.0" >> ~/.profile
    source ~/.profile
    ```

   * Now you can install easy fMRI same as a linux system

## STEP A: Copy Files

* Download easy fMRI files:
    * Option 1: From [GitLab](https://gitlab.com/easyfmri/easyfmri):
        ```
        git clone https://gitlab.com/easyfmri/easyfmri.git  ~/easyfmri
        ```
    * Option 2: From [GitHub](https://github.com/easyfmri/easyfmri):
        ```
        git clone https://github.com/easyfmri/easyfmri.git ~/easyfmri
        ```

* Copy executable files (ezfmri, ezedit, etc.) to `/usr/local/bin`:
    * For Linux:
        ```
        cd ~/easyfmri/Script
        ./cp_script_linux
        ```
    * For Mac:
        ```
        cd ~/easyfmri/Script
        ./cp_script_mac
        ```
* Copy startup script:
    * For Linux (bash and ~/.bashrc) 
        ```
        cd ~/easyfmri/Script
        ./install_script_linux_bashrc
        ```

    * For Linux (bash and ~/.profile) 
        ```
        cd ~/easyfmri/Script
        ./install_script_linux_profile
        ```

    * For Linux (zsh and ~/.zshrc) 
        ```
        cd ~/easyfmri/Script
        ./install_script_linux_zshrc
        ```

    * For Mac (bash and ~/.bash_profile) 
        ```
        cd ~/easyfmri/Script
        ./install_script_mac
        ```
 
* You must edit `~/.startupscript` (for bash) or `~/.zstartupscript` (for zsh) and enable/disable different parameters based on your computer setting. Further, you have to setup the PATH for easy fMRI, FSL, AFNI, miniconda/anaconda, etc. Editing the startup script by using one of these editors:
    ```
    gedit ~/.startupscript # For bash
    gedit ~/.zstartupscript # For zsh
    ```
    or
    ```
    nano ~/.startupscript # For bash
    nano ~/.startupscript # For zsh
    ```
    or
    ```
    vi ~/.startupscript # For bash
    vi ~/.startupscript # For zsh
    ```


* Apply the environment variables for setup Python, FSL, AFNI, etc.:
    * For bash:
        ```
        source ~/.startupscript 
        ```
    * For zsh:
        ```
        source ~/.zstartupscript 
        ```
    * Note: Since you did not install FSL and other related software, you may see some error on this stage such as `-bash: /usr/local/fsl/etc/fslconf/fsl.sh: No such file or directory`. Just skip them.



## STEP B: Installing FSL 6.0.x [preferred] or 5.0.1x


### Option 1: Installing FSL based on the [main source](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki)

* Register on [FSL website](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki) (it is free)

* Download `fslinstaller.py`

* Run following for downloading installation file (e.g. In version 6.0.3, the file name is `fsl-6.0.3-macOS_64.tar.gz` for Mac or `fsl-6.0.3-centos7_64.tar.gz` for all Linux distribution)

    * For Linux:
        ```
        python2 fslinstaller.py -o
        md5sum fsl-6.0.3-centos7_64.tar.gz
        ```
    
    * For Mac:
        ```
        python2 fslinstaller.py -o
        md5sum fsl-6.0.3-macOS_64.tar.gz
        ```

* Install the downloaded file:

    * For Linux:
        ```
        python2 fslinstaller.py -f fsl-6.0.3-centos7_64.tar.gz -M
        export FSLDIR="/usr/local/fsl"
        cd $FSLDIR/etc/fslconf
        source fsl.sh
        sudo ./install_fsleyes.sh
        sudo ./make_applications_links.sh
        sudo ./post_install.sh
        ```

    * For Mac:
        ```
        python2 fslinstaller.py -f fsl-6.0.3-macOS_64.tar.gz -M
        ```



### Option 2: Installing FSL via [NeuroDebian](http://neuro.debian.net/) (For Debian or Ubuntu)

In `Get NeuroDebian` section, you must select Linux version and the closest resource location and then run the generated script. In `Select desired components`, you also must select `all software`.

* For instance, this script for `Ubuntu 16.0.4` and `The University of Science and Technology of China (USTC)` is:
    ```
    wget -O- http://neuro.debian.net/lists/xenial.cn-bj2.full | sudo tee /etc/apt/sources.list.d/neurodebian.sources.list
    sudo apt-key adv --recv-keys --keyserver hkp://pool.sks-keyservers.net:80 0xA5D32F012649A5A9
    sudo apt-get update
    sudo apt install fsl-complete
    ```
    for `Ubuntu 18.0.4` and `The University of Science and Technology of China (USTC)` is:
    ```
    wget -O- http://neuro.debian.net/lists/bionic.cn-bj2.full | sudo tee /etc/apt/sources.list.d/neurodebian.sources.list
    sudo apt-key adv --recv-keys --keyserver hkp://pool.sks-keyservers.net:80 0xA5D32F012649A5A9
    sudo apt-get update
    sudo apt install fsl-complete
    ```
    for `Ubuntu 20.04` and `The University of Science and Technology of China (USTC)` is:
    ```
    wget -O- http://neuro.debian.net/lists/focal.cn-hf.full | sudo tee /etc/apt/sources.list.d/neurodebian.sources.list
    sudo apt-key adv --recv-keys --keyserver hkp://pool.sks-keyservers.net:80 0xA5D32F012649A5A9    
    sudo apt-get update
    sudo apt install fsl-complete
    ```

## STEP C: Install AFNI 17.3.x or above


### Copy AFNI files
* Download [AFNI](https://afni.nimh.nih.gov/):
    * [Ubuntu (>= 16.04)](https://afni.nimh.nih.gov/pub/dist/tgz/linux_ubuntu_16_64.tgz)
    * [Ubuntu (<16), Fedora, Red Hat, etc.](https://afni.nimh.nih.gov/pub/dist/tgz/linux_openmp_64.tgz)
    * [CentOS, Red Hat (RHEL 7)](https://afni.nimh.nih.gov/pub/dist/tgz/linux_centos_7_64.tgz)
    * [Mac 10.12 and higher](https://afni.nimh.nih.gov/pub/dist/tgz/macos_10.12_local.tgz)
    * [Mac 10.7—10.11](https://afni.nimh.nih.gov/pub/dist/tgz/macosx_10.7_local.tgz)
    * [Other versions](https://afni.nimh.nih.gov/pub/dist/doc/htmldoc/background_install/download_links.html#b-downloading-a-set-of-the-newest-precompiled-afni-binaries)

* Extract [AFNI](https://afni.nimh.nih.gov/) files to `~/abin`


### Install Linux packages for [AFNI](https://afni.nimh.nih.gov/pub/dist/doc/htmldoc/background_install/install_instructs/index.html)

* Fedora (>= 32): The essential system setup
    ```
    sudo yum install -y tcsh libXp openmotif gsl xorg-x11-fonts-misc       \
                        PyQt5 R-devel netpbm-progs gnome-tweak-tool ed     \
                        xorg-x11-server-Xvfb git
    sudo yum update -y
    ```


* Fedora (<= 31): The essential system setup
    ```
    sudo yum install -y tcsh libXp openmotif gsl xorg-x11-fonts-misc       \
                        PyQt4 R-devel netpbm-progs gnome-tweak-tool ed     \
                        xorg-x11-server-Xvfb git
    sudo yum update -y
    ```


* CentOS/RHEL 7: The essential system setup
    ```
    sudo yum install -y epel-release
    sudo yum install -y tcsh libXp openmotif gsl xorg-x11-fonts-misc       \
                        PyQt4 R-devel netpbm-progs gnome-tweak-tool ed     \
                        libpng12 xorg-x11-server-Xvfb git
    sudo yum update -y
    ```



*  Linux, Ubuntu 20.04: The essential system setup
    ```
    sudo add-apt-repository universe
      
    sudo apt-get update

    sudo apt-get install -y tcsh xfonts-base libssl-dev       \
                            python-is-python3                 \
                            python3-matplotlib                \
                            gsl-bin netpbm gnome-tweak-tool   \
                            libjpeg62 xvfb xterm vim curl     \
                            gedit evince eog                  \
                            libglu1-mesa-dev libglw1-mesa     \
                            libxm4 build-essential            \
                            libcurl4-openssl-dev libxml2-dev  \
                            libgfortran-8-dev libgomp1        \
                            gnome-terminal nautilus           \
                            gnome-icon-theme-symbolic         \
                            firefox xfonts-100dpi             \
                            r-base-dev
    ```



*  Linux, Ubuntu 18.04: The essential system setup
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

* Linux, Ubuntu 16.04 - 17.10: The essential system setup
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



* Linux, Ubuntu 15.10 and earlier: The essential system setup
    ```
    sudo apt-get install -y tcsh libxp6 xfonts-base python-qt4             \
                            libmotif4 libmotif-dev motif-clients           \
                            gsl-bin netpbm xvfb gnome-tweak-tool           \
                            libjpeg62 xterm gedit evince git
                            
                            
    sudo apt-get install -y tcsh xfonts-base python-qt4 gedit evince       \
                            libmotif4 libmotif-dev motif-clients           \
                            gsl-bin netpbm xvfb gnome-tweak-tool libjpeg62
    ```



## STEP D: Install Python 

### Install Python 3.8.x via [Miniconda3](https://docs.conda.io/en/latest/miniconda.html)

* Download [Miniconda3](https://docs.conda.io/en/latest/miniconda.html) for Python **3.8**

    * Note: In Windows 10, you must install the linux version of Miniconda 3


* Install Python 3.8
    * Note: **DO NOT** add conda init to the startup, becuase you will handle conda via easy fMRI startup script. e.g., say no to this question:
      ```
      Do you wish the installer to initialize Miniconda3
      by running conda init? [yes|no]
      ```

    * For Linux ([download link](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh)):
        ```
        sh Miniconda3-latest-Linux-<platform>.sh
        ```
    
    * For Mac ([download link](https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg)): click PKG file and continue installation.
        * Note: [Miniconda3](https://docs.conda.io/en/latest/miniconda.html) will be installed in `/opt/miniconda3` by default in Mac.

* Load environment variables: 

    * You have to edit both `~/.startupscript` and `~/.zstartupscript` and set the [Miniconda3](https://docs.conda.io/en/latest/miniconda.html) path as `ANACON_PATH`. Then:

    * Then:
        ```
        source ~/.startupscript # for bash
        source ~/.zstartupscript # for zsh
        ```
* Update Python in the base environment:
    ```
    conda update --all
    ```

* Creating the easy fMRI environment:
    ```
    conda create --name easyfmri python=3.8
    ```

* Update Conda components and install easy fMRI required python packages by using: 
    ```
    conda activate easyfmri 
    conda update --all
    conda install numpy scipy qt pyqt ipython matplotlib pandas seaborn psutil statsmodels
    conda install -c conda-forge mpi4py scikit-learn
    pip install -U future nibabel nitime nilearn pyqode.core pyqode.qt pydicom matplotlib h5py
    ```

* Install [PyTorch](https://pytorch.org/) package:
    * In Linux (with [NVIDIA GPU](https://www.nvidia.com/en-us/)):
        ```
        conda install pytorch torchvision cudatoolkit=10.2 -c pytorch
        ```
    * In Linux (only CPU):
        ```
        conda install pytorch torchvision cpuonly -c pytorch
        ```
    * In Mac:
        ```
        conda install pytorch torchvision -c pytorch
        ```

### Change main repository of `pip` [recommended for China]

For changing the main repository of `pip`:

* Creating the `~/.pip` directory by using `mkdir ~/.pip`


* Then generate the setting file `~/.pip/pip.conf`. For instance, following setting can change the main repository to `The University of Science and Technology of China`:
    ```
    [global]
    timeout = 60
    index-url  = https://mirrors.ustc.edu.cn/pypi/web/simple/
    
    [install]
    index-url = https://mirrors.ustc.edu.cn/pypi/web/simple/
    ```

### Change main repository of `conda` [recommended for China]


For changing the main repository of `conda`: 

* Creating setting file `~/.condarc`. For instance, following setting can change the main repository to `The University of Science and Technology of China`:
    ```
    channels:
      - https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
      - https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
      - defaults
    ssl_verify: true
    show_channel_urls: true
    ```



## STEP E: Run easy fMRI

* After restarting your computer, open a terminal and run easyfmri:

    ```
    ezfmri
    ```

* For computers with HiDPI display run following or just enable option in `~/.startupscript`.
    ```
    ezfmri_scaled
    ```

# How to manually upgrade easy fMRI

## Option 1: Fast upgrading via `git`: 
```
cd $EASYFMRI
git checkout master
git pull
git checkout developing
git pull
git checkout master # If you want to swithch back to stable version
```

## Option 2: A fresh copy from `gitlab` repository:

```
rm -rf $EASYFMRI 
git clone https://gitlab.com/easyfmri/easyfmri.git $EASYFMRI
```

## Option 3: A fresh copy from `github` repository:

```
rm -rf $EASYFMRI 
git clone https://github.com/easyfmri/easyfmri.git $EASYFMRI
```


# How to uninstall easy fMRI

```
rm -rf ~/easyfmri
```