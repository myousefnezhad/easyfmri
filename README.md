easy fMRI project (V1.8B3000 beta)
===============

### Introduction

Easy fMRI is an open source toolbox for the Human Brain Mapping and Decoding. This project is developing by [Muhammad Yousefnezhad](https://myousefnezhad.sourceforge.io), [iBRAIN Group](http://ibrain.nuaa.edu.cn), [Nanjing University of Aeronautics and Astronautics](http://iao.nuaa.edu.cn), China.

The project website is https://easyfmri.sourceforge.io/.

### Dependencies

Easy fMRI needs following software:

  -Platform: Linux, Mac (NOTE: you can use virtual machine for Windows platform)

  -[Python3](https://anaconda.org/anaconda/python) (version=3.6.2 or above)

  -[FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki) (version=5.0.10 or above) for preprocessing steps

  -[AFNI & SUMA](https://afni.nimh.nih.gov/) (version=17.3.06 or above) for 3D visualization

  -[CUDA](https://developer.nvidia.com/cuda-toolkit) for GPU-based algorithms

  -[CUDNN](https://developer.nvidia.com/cudnn) for GPU-based algorithms

  -[Tensorflow](https://www.tensorflow.org/install/) for Gradient-based Optimization and Learning 


### How to install easy fMRI


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
sudo cp ~/.easyfmri/Script/ezfmri  /usr/local/bin/
```

-- Set environment variables (see example at the end)


#### STEP B) Install Python 3.6.x 

-- Download [Anaconda3](https://anaconda.org/anaconda/python) and Install Python3 by using Anaconda3

For Linux:

```
sudo sh Anaconda3-<version>-Linux<platform>.sh
```

For Mac: click PKG file and continue installation.

-- Install all packages in `~/.easyfmri/PyPackage` directory

```
cd ~/.easyfmri/PyPackage
sudo pip install *
```

-- Install Tensorflow package:

For CPU version:

```
pip install tensorflow
```

For GPU Vesion: You must install [CUDA](https://developer.nvidia.com/cuda-toolkit) and [CUDNN](https://developer.nvidia.com/cudnn). Then, you can install [Tensorflow](https://www.tensorflow.org/install/)

Note: By employing `CUDA 9.0`, `CUDNN 7.0` and `Ubuntu 16.04.x`, you can use following command to install tensorflow:

```
pip install tensorflow-gpu
```

-- Set environment variables (see example at the end)


#### STEP C) Install FSL 5.0.10 or above

-- Register on [FSL website](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki)

-- Download `fslinstaller.py`

-- Run following for downloading installation file (Mac: `fsl-<version>-macOS_64.tar.gz` or Linux: `fsl-<version>-centos7_64.tar.gz`)

```
python2 fslinstaller.py -o
md5sum fsl-5.x.x-centosY_64.tar.gz
```


-- Install the downloaded file:

```
python2 fslinstaller.py -f <downloaded file name, e.g. fsl-5.x.x-centosY_64.tar.gz> -M
```

-- Set environment variables (see example at the end)


#### STEP D) Install AFNI 17.3.06 or above

-- Download [AFNI](https://afni.nimh.nih.gov/)

-- Extract AFNI to `~/abin`

-- Set environment variables (see example at the end)


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

Copy following to in `.profile` or `.bashrc` and restart your computer

```
# Easy fMRI
export EASYFMRI="$HOME/.easyfmri"         # This is the default directory of easy fMRI
export PATH="/usr/local/bin:$PATH"        # This is for binary file for running "ezfmri" command

# Python
export PATH="$HOME/anaconda3/bin:$PATH"   # This must be matched by your anaconda installation directory
alias python3="python3 -m IPython"

# FSL
export FSLDIR="/usr/local/fsl"            # This must be matched by FSL installation directory
. ${FSLDIR}/etc/fslconf/fsl.sh
export PATH="$FSLDIR/bin:$PATH"

# AFNI
export PATH="$HOME/abin:/usr/lib/lightdm/lightdm:$PATH" # This must be matched by AFNI installation directory
```

NOTE: We also provide another example of Environment Variables in `~/.easyfmri/Script/linuxshell.tar.gz`
