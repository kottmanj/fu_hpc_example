# Tequila Example
```bash
pip install -r requirements.txt
sbatch run.sh
```

# Tequila with Madness Example
Tequila dependencies are as before.  
Madness is installed by following instructions on this [fork](https://github.com/kottmanj/madness).  
Unfortunately there is currently no support for package managers.  
Needs: GNU C++ Compilers version > 7 and the corresponding MPI compilers (MPICH usually works best).
After madness is compiled in the directory `MAD_ROOT_DIR` this information this variable should be exported:
```bash
export MAD_ROOT_DIR=/path/where/madness/was/compiled/
```
If available threads are more than 64, it's adviced to limit them with
```bash
export MAD_NUM_THREADS=64
python example_madness.py
```

