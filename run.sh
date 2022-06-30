#!/bin/bash

#SBATCH --job-name=tq_test                
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=12
#SBATCH --nodes=1                      
#SBATCH --time=0-00:10:00              
#SBATCH --mem-per-cpu=2G               
#SBATCH --output=tq_test_%j.out           
#SBATCH --error=tq_test_%j.err           

export OMP_NUM_THREADS=12
python example.py
