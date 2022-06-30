import tequila as tq

geometry = "Be 0.0 0 0.0 0.0\n H 0.0 0.0 1.5\n H 0.0 0.0 -1.5"
# needs madness from kottmanj fork installed and the variable MAD_ROOT_DIR (storing the path to the directory where madness was compiled) exported
mol = tq.Molecule(geometry=geom)
H = mol.make_hamiltonian()
U = mol.make_ansatz(name="UpCCGSD")
E = tq.ExpectationValue(H=H, U=U)

result = tq.minimize(E)
