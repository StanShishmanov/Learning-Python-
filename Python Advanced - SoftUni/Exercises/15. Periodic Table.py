n = int(input())

chem_compounds = set()
for i in range(n):
    chemicals = input().split()
    for i in chemicals:
        chem_compounds.add(i)

for i in chem_compounds:
    print(i)