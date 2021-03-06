import tequila as tq

geometry = "Be 0.0 0 0.0 0.0\nH 0.0 0.0 1.5\nH 0.0 0.0 -1.5"
# needs pyscf or psi4 installed
mol = tq.Molecule(geometry=geometry, basis_set="sto-3g")
H = mol.make_hamiltonian()
U = mol.make_ansatz(name="UpCCGSD")
E = tq.ExpectationValue(H=H, U=U)

result = tq.minimize(E)
