# ----------------------------------------------------------------------
# Debian baseOS docker container to use with CTSM builds
# ----------------------------------------------------------------------

FROM gcc:6.5
MAINTAINER S.P. Serbin email: sserbin@bnl.gov

RUN useradd -ms /bin/bash prosail

# Set a few variables that can be used to control the docker build
#NONE

# Update the system and install initial dependencies
RUN apt-get update -y \
    && apt-get install -y \
    cmake \
    git \
    subversion \
    bzip2 \
    libgmp3-dev \
    m4 \
    wget \
    libcurl4-openssl-dev \
    zlib1g-dev \
    libncurses5-dev \
    libxml2 \
    libxml2-dev \
    csh \
    liblapack-dev \
    libblas-dev \
    liblapack-dev \
    libffi6 \
    libffi-dev \
    libxml-libxml-perl \
    libxml2-utils \
    vim \
    libudunits2-0 \
    libudunits2-dev \
    udunits-bin \
    htop \
    python2.7 \
    python-dev \
    python-pip \
    python3 \
    python3-pip \
    apt-utils \
    ftp \
    apt-transport-https \
    locales \
    libjson0 \
    libjson0-dev \
    libjson-perl \
    netcdf-bin \
    libnetcdf-dev \
    libhdf5-serial-dev \
    autopoint \
    gsl-bin \
    libgsl0-dev \
    llvm \
    clang

    ## Install program to configure locales
RUN dpkg-reconfigure locales && \
  locale-gen C.UTF-8 && \
    /usr/sbin/update-locale LANG=C.UTF-8
RUN echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen && \
      locale-gen
   ## Set default locale for the environment
ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

   ## check locales
RUN locale -a

## Compile Expat XML parser
RUN echo "*** Compiling Expat XML parser"
RUN cd / \
    && wget https://github.com/libexpat/libexpat/releases/download/R_2_2_6/expat-2.2.6.tar.bz2 \
    && tar -xvjf expat-2.2.6.tar.bz2 \
    && cd expat-2.2.6 \
    && ./configure \
    && make \
    && make install \
    && cd / \
    && rm -r expat-2.2.6 \
    && rm expat-2.2.6.tar.bz2

   ## build PROSAIL_D
RUN echo "*** Compiling PROSAIL_D "
RUN cd / \
    && wget http://teledetection.ipgp.jussieu.fr/prosail/PROSAIL_D_Fortran.zip \
    && unzip PROSAIL_D_Fortran.zip \
    && chown prosail -R /PROSAIL_D_FORTRAN \
    && chmod 775 -R /PROSAIL_D_FORTRAN \
    && cd PROSAIL_D_FORTRAN \
    && rm main_PROSAIL.f90 \
    && wget 
    && gfortran -o prosail.exe MODULE_PRO4SAIL.f90 dataSpec_PDB.f90 main_PROSAIL.f90 LIDF.f90 dladgen.f PRO4SAIL.f90 prospect_DB.f90 tav_abs.f90 volscatt.f90 \
    && ./prosail.exe 2 65 2 4 0 0.09 0.09 5 -0.35 -0.15 0.1

RUN cd / \
    && mkdir -p output \
    && chown prosail -R /output \
    && chmod 775 -R /output


### EOF
