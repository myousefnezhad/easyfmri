easy fMRI project (0.0.1)
Created by Muhammad Yousefnezhad

-FSL Version=5.0.9
-FEAT Version=6.0.0
-AFNI Version=built Apr 12 2017
-Python Version=3.6.1
---Python Packages
-----ipython==6.1.0
-----jupyter==1.0.0
-----matplotlib==2.0.2
-----numpy==1.13.1
-----PyQt5==5.8.2
-----scikit-learn==0.18.2
-----scipy==0.19.1
-----sip==4.19.2
-----virtualenv==15.1.0
-----virtualenv-clone==0.2.6
-----virtualenvwrapper==4.7.2

How to install:

# Python3
brew install python3
pip3 install numpy scipy sklearn ipython jupyter matplotlib PyQt5 nipype nibabel

# Then respectively install pyqode.qt.zip and pyqode.core.zip from install directory

# Python3 ENV
export PATH="/usr/local/bin:$PATH"
export PIP_DOWNLOAD_CACHE=$HOME/.pip/cache
export WORKON_HOME=$HOME/.virtualenvs
export PIP_VIRTUALENV_BASE=$WORKON_HOME
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
export PATH="/home/linuxbrew/.linuxbrew/sbin:$PATH"

# FSL ENV
export FSLDIR="/usr/share/fsl/5.0"
. ${FSLDIR}/etc/fslconf/fsl.sh
export PATH="$FSLDIR/bin:$PATH"

# AFNI ENV
export PATH="$HOME/abin:/usr/lib/lightdm/lightdm:$PATH"

# easy fMRI ENV
export EASYFMRI="~/easyfMRI/"
export PATH="/usr/local/bin:$PATH"

# easy fMRI Link
source ~/.profile
chmod +x $EASYFMRI/easyfmri.sh
sudo ln -s $EASYFMRI/easyfmri.sh /usr/local/bin/easyfmri
