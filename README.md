# Membrana create

### You need to write:
make_mems.ipynb - creates bilayer from one molecule. 
You need to write guiding atoms for this, step from one molecule to another, size of layer n*n, and penetration distance..

Control density and size of membrane by theese parametres. 
After that, run optimization.

### How it works
Molecules and guide atoms are set to place the membrane along the axis. Further, the program itself optimizes their position so that the layer is as compact as possible.

The script creates a pattern so that when turning W conformations do not overlap.

Then the program goes through all the molecules and optimizes their position based on the Lennard Jones potential.
readers_writers.py - help file with functions for read and write coords files

# Calc density

Reads membrane files and calculates integral density. Adds them to the graph with membrane oxygen densities and water density.

# Water del 

delete water in membrane
