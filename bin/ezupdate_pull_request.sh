#!/bin/bash

cd $EASYFMRI
git checkout master
git pull origin master
git checkout developing
git pull origin developing
git checkout master