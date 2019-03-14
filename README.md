# PROSAIL Docker Repository
A repository of Docker containers of the PROSPECT+SAIL family of models, sourced from http://teledetection.ipgp.jussieu.fr/prosail/

This repo is very much a WIP


Initial run example
```
docker run -t -i -v ~/scratch:/output prosail:latest /bin/sh -c 'cd /output/ && /PROSAIL_D_FORTRAN/./prosail.exe 2 65 2 4 0 0.09 0.09 5 -0.35 -0.15 0.1'
```

```
cd ~/scratch
vi Refl_CAN_PDB.txt
 400  0.019004
 401  0.019021
 402  0.019037
 403  0.019054
 404  0.019069
 405  0.019085
 406  0.019075
 407  0.019064
 408  0.019057
 409  0.019045
 410  0.019033
 ...
 ```
