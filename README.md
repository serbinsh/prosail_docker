# prosail_docker
A repository of Docker containers of the PROSPECT+SAIL family of models, sourced from http://teledetection.ipgp.jussieu.fr/prosail/

This repo is very much a WIP


Initial run example
```
docker run -t -i -v ~/scratch:/output prosail:latest /bin/sh -c 'cd /output/ && /PROSAIL_D_FORTRAN/./prosail.exe 2 65 2 4 0 0.09 0.09 5 -0.35 -0.15 0.1'
```
