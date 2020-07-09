#!/usr/bin/env zsh
# For installing this script:
# 1. copy this file to home directory
# 2. Enable/Disable the features
# 3. Set the installation directory
# 4. Run following command for Linux:
# echo "source ~/.zstartupscript" >> ~/.zshrc

# We recommend install oh-my-zsh and powerlevel9k for command prompt in ZSH
# https://github.com/ohmyzsh/ohmyzsh
# https://github.com/Powerlevel9k/powerlevel9k


######################################
# Enable ("1") or Disable ("0") features #
######################################
# This enables easy fMRI environment variable ($EASYFMRI)
export EN_EZFMRI="1"
# This sets python base direcotry based on $ANACON_PATH
export EN_PYTHON="1"
# This enables iPython by default when you run python in terminal
export EN_PYTHON_ALIAS="0"
# This sets julia base direcotry
export EN_JULIA="0"
# This sets AFNI base directory based on $AFNI_PATH
export EN_AFNI="1"
# This sets FSL base directory based on $FSLDIR and then run fsl.sh script
export EN_FSL="1"
# This set FreeSurface base directory and run the setup scrip
export EN_FREESURFACE="0"
# This enables CUDA environment variables
export EN_CUDA="0"
# Turn it on for OLED/HiDPI display, if EN_SCALE_AUTO = 0 then default is 200x. It is related to easy fMRI setting.
export EN_SCALE="1"
# Turn it on for OLED/HiDPI display, default is 200x. It is related to easy fMRI setting.
export EN_SCALE_AUTO="1"
# Turn it on for OLED/HiDPI display, default is 200x. It is related to FSL setting.
export EN_SCALE_WISH="1" # Run FSL with Scale Factor
# Clean Screen
export EN_CLEAN_SCREEN="0"
# Latex (set LaTex Path as well)
export EN_LATEX="0"
######################################
# Proxy for terminal                 #
######################################
# Setup these parameters if you are using VPN to connect internet
alias proxyon='export http_proxy=http://127.0.0.1:3213 && export https_proxy=http://127.0.0.1:3213'
alias proxyoff='export http_proxy= && export https_proxy='
######################################
# Directories & Parameters           #
######################################
# This is base dir for Anaconda, easy fMRI, and AFNI
# For root user, you must set it to the normal user home directory such as export INSTALL_DIR="/home/tony", where
# we have install easy fMRI in the normal user home directory
export INSTALL_DIR="$HOME"
# Base directory of FSL
export FSLDIR="/usr/local/fsl"  # for FSL 5.0.1x
# Base directory of Anaconda (Python 3.7.x)
export ANACON_PATH="/opt/miniconda3/bin"
# Base directory of Julia
export JULIA_PATH="$INSTALL_DIR/julia/bin"
# Base direcory of AFNI
export AFNI_PATH="$INSTALL_DIR/abin"
# Base directory for FreeSurface
export FREESURFER_HOME="$INSTALL_DIR/freesurfer"
# Base directory of CUDA
export CUDA_HOME="/usr/local/cuda"
# Latex directory
export LATEX_DIR="/usr/local/texlive/2019/bin/x86_64-linux"
# Scale parameter for OLED/HiDPI display
export SCREEN_SCALE="2"     # Set it for OLED display, "2" means 200x for the first screen, "2;1.5" means 200x for 1st monitor and 150x for 2nd monitor
# Uncomment this item if you installed FSL via http://neuro.debian.net/
# export FSLDIR="/usr/share/fsl/5.0" # for FSL 5.0.9
# Uncomment this item if you are using an embedded linux in Windows 10 via WSL
# export DISPLAY=:0.0 # Enable for Windows 10
######################################
# Scripts                            #
######################################

## Julia
if (( $EN_JULIA != 0 )); then
  export PATH="$JULIA_PATH:$PATH"
fi

## LaTex
if (( $EN_LATEX != 0 )); then
  export PATH="$LATEX_DIR:$PATH"
fi

######## Easy fMRI
if (( $EN_EZFMRI != 0 )); then
  export EASYFMRI="$INSTALL_DIR/easyfmri"
  export PATH="$INSTALL_DIR/easyfmri/bin:$PATH"
fi

######## Python
if (( $EN_PYTHON != 0 )); then
  export PATH="$ANACON_PATH:$PATH"
fi
if (( $EN_PYTHON_ALIAS != 0 )); then
  alias python="python -m IPython"
  alias python3="python -m IPython"
fi
######## AFNI
if (( $EN_AFNI != 0 )); then
  export DYLD_LIBRARY_PATH=/opt/X11/lib/flat_namespace
  export DYLD_FALLBACK_LIBRARY_PATH="$HOME/abin"
  export PATH="/usr/local/bin:$AFNI_PATH:$PATH"
fi
####### FSL
if (( $EN_FSL != 0 )); then
  . $FSLDIR/etc/fslconf/fsl.sh
  export PATH="$FSLDIR/bin:$PATH"
fi
####### FreeSurface
if (( $EN_FREESURFACE != 0 )); then
    source $FREESURFER_HOME/SetUpFreeSurfer.sh
fi
######## QT Scale Factor
if (( $EN_SCALE != 0 )); then
   if (( $EN_SCALE_AUTO != 0 )); then
     export QT_AUTO_SCREEN_SCALE_FACTOR=1
   else
     export QT_SCALE_FACTOR=1
     export QT_AUTO_SCREEN_SCALE_FACTOR=0
     export QT_SCREEN_SCALE_FACTORS=$SCREEN_SCALE
   fi
   # Uncomment these parameters if you are using HiDPI with 100x scale in your Linux (GDK/Gnome) setting
   #export GDK_DPI_SCALE=$SCREEN_SCALE
   #export GDK_SCALE=$SCREEN_SCALE
   if (( $EN_SCALE_WISH != 0 )); then
        export FSLWISH="/usr/bin/wish"
   fi
fi
####### CUDA
if (( $EN_CUDA != 0 )); then
  export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:$CUDA_HOME/lib"
  export LD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:$CUDA_HOME/lib:/usr/local/cuda/lib64"
  export PATH="$CUDA_HOME/bin:$PATH"
  export CPLUS_INCLUDE_PATH=$CPLUS_INCLUDE_PATH:/usr/local/cuda/samples/common/inc
fi
###### Clean Screen
if (( $EN_CLEAN_SCREEN != 0 )); then
  clear
fi
