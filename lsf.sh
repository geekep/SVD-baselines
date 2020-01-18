#!/bin/sh                   

#BSUB -q normal

#BSUB -o %J.out

#BSUB -e %J.err

#BSUB -n 1 

#BSUB -J JOBNAME

#BSUB  -R span[ptile=1]   

#BSUB -m "user-g4a60"         

#BSUB  -gpu  num=8         

python videoprocess/deepfeatures_extraction.py --dataname svd
