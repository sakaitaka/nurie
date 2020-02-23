#!/bin/bash

yum install -y git gcc bzip2 bzip2-devel openssl openssl-devel readline readline-devel sqlite-devel
yum install -y cmake libjpeg-devel libtiff-devel libpng-devel jasper-devel
yum install -y mesa-libGL-devel libXt-devel libgphoto2-devel nasm libtheora-devel
yum install -y autoconf automake gcc-c++ libtool yasm openal-devel blas blas-devel atlas atlas-devel lapack lapack-devel
yum install -y tbb-devel
yum install -y libgtk-x11-2.0.so.0 libgdk-x11-2.0.so.0 libXi.so.6 libXcursor.so.1 libXcomposite.so.1 libXtst.so.6 libXss.so.1 libgconf-2.so.4 libasound.so.2 libcups.so.2

