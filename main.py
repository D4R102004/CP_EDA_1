from Clases_Practicas_EDA_I.Cp_4AVL.aBB import BinarySearchTree
from Clases_Practicas_EDA_I.Cp_4AVL.aVl import AVL
from Clases_Practicas_EDA_I.Cp_4AVL.physical_tree import AVLTree
from Clases_Practicas_EDA_I.Cp_4AVL.cPAVL import CP4
from Clases_Practicas_EDA_I.Cp_4AVL.sET import Set
from Clases_Practicas_EDA_I.Cp_6DSU.DSURank import DSURank as DSUR


def same_equivalence_class(ds: DSUR, a: int, b: int) -> bool:
    pa = ds.set_of(a)
    pb = ds.set_of(b)
    return pa == pb


elements = [i for i in range(1, 8)]
dsu = DSUR(7)
dsu.merge(1, 2)
dsu.merge(2, 3)
dsu.merge(4, 5)
dsu.merge(6, 7)
dsu.merge(5, 6)
dsu.merge(3, 7)
x = 3
y = 7
print(f"{1} and {6} are same equivalence class?: {same_equivalence_class(dsu, x, y)}")








