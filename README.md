### You need to write:
make_mems.ipynb - creates bilayer from one molecule. 
You need to write guiding atoms for this, step from one molecule to another, size of layer n*n, and penetration distance..

Control density and size of membrane by theese parametres. 
After that, run optimization.

### How it works
Molecules and guide atoms are set to place the membrane along the axis. Further, the program itself optimizes their position so that the layer is as compact as possible.

The script arranges the molecules in the layer so that when flipped, the second layer does not overlap 234 conformations. After creating a layer, it is copied and flipped so as not to break the chiral isomerism.

Then the program goes through all the molecules and optimizes their position based on the Lennard Jones potential.