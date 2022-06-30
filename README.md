# Tequila Example
## Install dependencies for this example
```bash
pip install pyscf
```
## Install tequila (newest version)
```bash
pip install git+https://github.com/aspuru-guzik-group/tequila.git@devel
```

## Example Script
```bash
python example.py
```
where example.py has followign content
```python
import tequila as tq

mol = tq.Molecule(geometry=geom)
H = mol.make_hamiltonian()
U = mol.make_ansatz(name="SPA")
E = tq.ExpectationValue(H=H, U=U)

result = tq.minimize(E)
```


# Tequila with Madness Example
Tequila dependencies are as before.  
Madness is installed by following instructions on this [fork](https://github.com/kottmanj/madness).  
Needs: GNU C++ Compilers version > 7 and the corresponding MPI compilers (MPICH usually works best).
After madness is compiled in the directory `MAD_ROOT_DIR` this information this variable should be exported:
```bash
export MAD_ROOT_DIR=/path/where/madness/was/compiled/
```
If available threads are more than 64, it's adviced to limit them with
```bash
export MAD_NUM_THREADS=64
```  

Here is an example script executed with python:  
```python
import tequila as tq

mol = tq.Molecule(geometry=geom)
H = mol.make_hamiltonian()
U = mol.make_ansatz(name="SPA")
E = tq.ExpectationValue(H=H, U=U)

result = tq.minimize(E)
```
